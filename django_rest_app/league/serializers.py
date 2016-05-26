from django.contrib.auth.models import User
from league.models import League, LeagueParticipant
from registration.serializers import UserSerializer
from registration.models import UserProfile
from rest_framework import serializers




class LeagueParticipantSerializer(serializers.ModelSerializer):

    name = serializers.ReadOnlyField(source='participant.user.username')

    class Meta:
        model = LeagueParticipant
        fields = ('name', 'weekWins', 'weekLosses', 'overallWins', 'overallLosses' )

class LeagueSerializer(serializers.ModelSerializer):

    participants = LeagueParticipantSerializer(source='leagueparticipant_set', many=True)

    class Meta:
        model = League
        fields = ('id', 'password', 'name', 'commissioner', 'participants')
        extra_kwargs = {
                'password': {'write_only': True},
                }

    def create(self, validated_data):
        password = validated_data['password']
        name = validated_data['name']
        league = League.objects.create(name=name, password=password, commissioner=validated_data['commissioner'])
        profile = UserProfile.objects.get(user=validated_data['commissioner']) 
        
        participant = LeagueParticipant.objects.filter(participant=profile)
        if not participant:
            participant = LeagueParticipant.objects.create(league=league, participant=profile)

        return league

class UpdateLeagueSerializer(LeagueSerializer):

    class Meta:
        model = League
        fields = ('id', 'name', 'commissioner')
        extra_kwargs = {
                'commissioner': {'read_only': True},
                'name': {'read_only': True},
                }

