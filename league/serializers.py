from rest_framework import serializers

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
