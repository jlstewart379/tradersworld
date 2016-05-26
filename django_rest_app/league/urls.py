from django.conf.urls import url
from league import views


urlpatterns = [
    url(r'^create/$', views.CreateLeague.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.GetLeague.as_view()),
    url(r'^add_user/(?P<pk>[0-9]+)/$', views.AddUserLeague.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.LeagueParticipantDetail.as_view(), name='league_participant-detail'),
]
