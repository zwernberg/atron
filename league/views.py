from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from django.views.decorators.cache import cache_page


from atron import settings
from league import serializers

import league.service as service
from league.models import Team, Player, League

import requests

import pdb
# Create your views here.


def fetch(endpoint, leagueId, seasonId = settings.YEAR, extra_params = {}):
    params = {
        'leagueId' : leagueId,
        'seasonId': seasonId
    }
    params.update(extra_params)
    return requests.get(settings.ENDPOINT + endpoint, params=params)


@cache_page(60 * 5)
@api_view(['GET',])
def league_settings(request):
    params = {
        'leagueId': settings.BOB_ID,
        'seasonId': settings.YEAR
    }
    r = service.fetch('leagueSettings', settings.BOB_ID)
    status = r.status_code
    data = r.json()

    return Response(data, status)

@cache_page(20)
@api_view(['GET',])
def scoreboard_view(request):
    leagues = League.objects.all()
    matchupPeriodId = request.GET.get('matchupPeriodId', '')
   
    response = service.fetchWeek(leagues, matchupPeriodId, settings.YEAR)

    return Response(response.data, response.status_code)

@cache_page(10)
@api_view(['GET',])
def standings_view(request):

    data = {}
    leagues = League.objects.all()
    status_code = ''
    for league in leagues:
        res = fetch('leagueSettings', league.league_id)
        val = res.json()['leaguesettings']['teams'].values()
        team_serialized = serializers.TeamSerializer(val, many=True)
        data[league.league_id] = team_serialized.data
        status_code = res.status_code
    return Response(data, status_code)


@api_view(['GET',])
def team_view(request):
    data = {}
    leagues = League.objects.all()
    status_code = ''
    for league in leagues:
        teams = range(1, league.size + 1)
        params = {
            'leagueId': league.league_id,
            'seasonId': request.GET.get('year', settings.YEAR),
            'matchupPeriodId': request.GET.get('matchupPeriodId', ''),
            'teamIds': teams
        }
        res = fetch('rosterInfo', league.league_id, extra_params = params)
        val = res.json().values()
        
        #team_serialized = serializers.TeamSerializer(val, many=True)
        #data[league.league_id] = team_serialized.data
        status_code = res.status_code
        data[league.division] = val

    return Response(data, status_code)

@cache_page(10)
@api_view(['GET',])
def championship_view(request):
    data = []
    status_code = ''
    teams = Team.objects.all().prefetch_related('players')
    for team in teams:
        players = []
        for player in team.players.filter(starting=True):
            players.append(player.player_Id)
        params = {
            'playerId': ",".join(players),
            'useCurrentPeriodProjectedStats': True,
            'useCurrentPeriodRealStats': True
        }
        team_result = fetch('playerInfo', team.league_id, extra_params= params)
        players_result = team_result.json()['playerInfo']['players']
        team_obj = {
            'team_name': team.team_name,
            'team_owner': team.team_owner,
            'league_id': team.league_id,
            'division': team.division,
            'avatarUrl': team.avatarUrl,
            'players': players_result,

        }
        status_code = team_result.status_code
        results = serializers.smallTeamSerializer(team_obj)
        data.append(results.data)
        
    return Response(data, status_code)