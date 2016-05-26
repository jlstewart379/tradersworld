from league import serializers
from league.models import League, LeagueParticipant
from rest_framework import generics
from league import serializers


class CreateLeague(generics.CreateAPIView):
    queryset = League.objects.all()
    serializer_class = serializers.LeagueSerializer

class GetLeague(generics.RetrieveAPIView):
    queryset = League.objects.all()
    serializer_class = serializers.LeagueSerializer

class AddUserLeague(generics.UpdateAPIView):
    queryset = League.objects.all()
    serializer_class = serializers.UpdateLeagueSerializer

class LeagueParticipantDetail(generics.RetrieveAPIView):
    queryset = LeagueParticipant.objects.all()
    serializer_class = serializers.LeagueParticipantSerializer
