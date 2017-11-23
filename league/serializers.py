from rest_framework import serializers


class TeamSerializer(serializers.Serializer):
    divisionStanding = serializers.IntegerField()
    overallStanding = serializers.IntegerField()
    rank = serializers.IntegerField()
    teamId = serializers.IntegerField()
    teamLocation = serializers.CharField()
    teamNickname = serializers.CharField()
    teamAbbrev = serializers.CharField()
