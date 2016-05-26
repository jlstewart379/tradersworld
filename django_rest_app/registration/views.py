from django.contrib.auth.models import User
from registration import serializers 
from registration.models import UserProfile
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

class NewUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class GetUser(generics.RetrieveAPIView):
    authentication_classes = (TokenAuthentication, )
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class CurrentUser(GetUser):
    authentication_classes = (TokenAuthentication, )
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def retrieve(self, request, pk=None):
        return Response(serializers.UserSerializer(request.user).data)
