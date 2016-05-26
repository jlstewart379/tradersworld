from django.conf.urls import url
from registration import views
from rest_framework.authtoken.views import obtain_auth_token 

urlpatterns = [
    url(r'^users/(?P<pk>[0-9]+)/$', views.GetUser.as_view(), name='user-detail'),
    url(r'^users/new/$', views.NewUser.as_view()),
    url(r'^users/current/$', views.CurrentUser.as_view()),
    url(r'^auth_token/$', obtain_auth_token),
]
