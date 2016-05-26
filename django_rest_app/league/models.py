from django.db import models
from django.contrib.auth.models import User
from registration.models import UserProfile


class League(models.Model):

    name = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    commissioner = models.ForeignKey(User, related_name='+')
    participants = models.ManyToManyField(UserProfile, through='LeagueParticipant')

    
class LeagueParticipant(models.Model):
    league = models.ForeignKey(League)
    participant = models.ForeignKey(UserProfile)
    weekWins = models.IntegerField(default=0)
    weekLosses = models.IntegerField(default=0)
    overallWins = models.IntegerField(default=0)
    overallLosses = models.IntegerField(default=0)
