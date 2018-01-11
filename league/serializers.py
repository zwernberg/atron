from rest_framework import serializers

from league.models import Team, Note
from decimal import Decimal

class RecordSerializer(serializers.Serializer):
    pointsFor = serializers.DecimalField(max_digits=10, decimal_places=3)
    pointsAgainst = serializers.DecimalField(max_digits=10, decimal_places=3)
    overallWins = serializers.IntegerField()
    overallLosses = serializers.IntegerField()
    overallTies = serializers.IntegerField()

class OwnerSerializer(serializers.Serializer):
    firstName = serializers.CharField()
    lastName = serializers.CharField()
    primaryOwner = serializers.BooleanField()
    ownerId = serializers.IntegerField()
    userProfileId = serializers.IntegerField()

class TeamSerializer(serializers.Serializer):
    divisionStanding = serializers.IntegerField()
    overallStanding = serializers.IntegerField()
    rank = serializers.IntegerField()
    teamId = serializers.IntegerField()
    teamLocation = serializers.CharField()
    teamNickname = serializers.CharField()
    teamAbbrev = serializers.CharField()
    record = RecordSerializer()
    owners = serializers.SerializerMethodField()
    teamName = serializers.SerializerMethodField()
    fullRecord = serializers.SerializerMethodField()

    def get_owners(self, obj):
        return OwnerSerializer(obj['owners'][0]).data

    def get_teamName(self, obj):
        return (obj['teamLocation'] + " " + obj['teamNickname'])

    def get_fullRecord(self, obj):
        return (str(obj['record']['overallWins'])+'-'+ str(obj['record']['overallLosses']))

class PlayerSerializer(serializers.Serializer):
    projectedPoints = serializers.SerializerMethodField()
    actualPoints = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()
    firstName = serializers.SerializerMethodField()
    lastName = serializers.SerializerMethodField()
    fullName = serializers.SerializerMethodField()
    def get_position(self, obj):
        return (obj['player']['defaultPositionId'])

    def get_firstName(self, obj):
        return (obj['player']['firstName'])
    def get_lastName(self, obj):
        return (obj['player']['lastName'])

    def get_fullName(self, obj):
        return ((obj['player']['firstName'])) + " " + (obj['player']['lastName'])

    def get_projectedPoints(self, obj):
        return (round(obj['currentPeriodProjectedStats']['appliedStatTotal'],2))
    
    def get_actualPoints(self, obj):
        if (not obj['currentPeriodRealStats'] or not obj['currentPeriodRealStats']['appliedStatTotal']):
            return 0
        return (round(obj['currentPeriodRealStats']['appliedStatTotal'], 2))

class smallTeamSerializer(serializers.Serializer):
    team_name = serializers.CharField()
    team_owner = serializers.CharField()
    league_id = serializers.CharField()
    avatarUrl = serializers.CharField()
    division = serializers.CharField()
    projected_total = serializers.SerializerMethodField()
    actual_total = serializers.SerializerMethodField()
    players = PlayerSerializer(many=True)


    def get_projected_total(self, obj):
        total = 0
        for player in obj['players']:
            temp = 0
            if (player['currentPeriodRealStats'] and player['currentPeriodRealStats']['appliedStatTotal']):
                temp = max(player['currentPeriodProjectedStats']['appliedStatTotal'], player['currentPeriodRealStats']['appliedStatTotal'])
            else:
                temp = player['currentPeriodProjectedStats']['appliedStatTotal']
            total += temp
        return round(total, 2)

    def get_actual_total(self, obj):
        total = 0
        for player in obj['players']:
                if (player['currentPeriodRealStats'] and player['currentPeriodRealStats']['appliedStatTotal']):
                    total += (player['currentPeriodRealStats']['appliedStatTotal'])
        return round(total, 2)

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('author', 'week', 'text')