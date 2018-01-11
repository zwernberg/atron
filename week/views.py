from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.cache import cache_page


from atron import settings
from league.models import League, Season, Note
from league.serializers import NoteSerializer

import week.service as service
import pdb

@cache_page(20)
@api_view(['GET',])
def matchups_view(request, week=''):
    season = Season.objects.prefetch_related('notes').prefetch_related('leagues').first()
    leagues = season.leagues.all()
    notes = season.notes.filter(week=week).all()
    notes_serialized = NoteSerializer(notes, many=True)
    response = service.fetchMatchups(leagues, week, settings.YEAR)
    response['data']['notes'] = notes_serialized.data
    return Response(response['data'], response['status_code'])  