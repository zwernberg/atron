from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from django.views.decorators.cache import cache_page


from atron import settings
from league import serializers

from league.models import Team, Player

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
    r = fetch('leagueSettings', settings.BOB_ID)
    status = r.status_code
    data = r.json()

    return Response(data, status)

@cache_page(20)
@api_view(['GET',])
def scoreboard_view(request):
    params = {
        'leagueId': settings.BOB_ID,
        'seasonId': settings.YEAR
    }
    r = fetch('scoreboard', settings.BOB_ID)
    status = r.status_code
    data = r.json()

    return Response(data, status)

@cache_page(60 * 5)
@api_view(['GET',])
def standings_view(request):

    bob = fetch('leagueSettings', settings.BOB_ID)
    dot = fetch('leagueSettings', settings.DOT_ID)
    bob_teams = bob.json()['leaguesettings']['teams'].values()
    dot_teams = dot.json()['leaguesettings']['teams'].values()
    bob_serialized = serializers.TeamSerializer(bob_teams, many=True)
    dot_serialized = serializers.TeamSerializer(dot_teams, many=True)
    data = {
        'dot': dot_serialized.data,
        'bob': bob_serialized.data
    }
    return Response(data, bob.status_code)


## @cache_page(10)
@api_view(['GET',])
def championship_view(request):
    data = []
    teams = Team.objects.all().prefetch_related('players')
    for team in teams:
        players = []
        for player in team.players.all():
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
        # pdb.set_trace()
        results = serializers.smallTeamSerializer(team_obj)
        data.append(results.data)
        
    return Response(data, 302)