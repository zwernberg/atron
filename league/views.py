from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from django.views.decorators.cache import cache_page


from atron import settings
from league import serializers

import requests
# Create your views here.

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


def fetch(endpoint, leagueId, seasonId = settings.YEAR):
    params = {
        'leagueId' : leagueId,
        'seasonId': seasonId
    }

    return requests.get(settings.ENDPOINT + endpoint, params=params)