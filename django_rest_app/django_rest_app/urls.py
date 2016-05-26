from django.conf.urls import include, url

urlpatterns = [
        url('^authentication/', include('rest_framework.urls', namespace='rest_framework')),
        url('^registration/', include('registration.urls')),
        url('^league/', include('league.urls')),
]
