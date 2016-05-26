from django.contrib.auth.models import User
from rest_framework import serializers
from registration.models import UserProfile
from rest_framework.authtoken.models import Token


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile

class UserSerializer(serializers.ModelSerializer):

    profile = UserProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'profile')
        extra_kwargs = {'password':{'write_only': True}, 'profile':{'read_only': True} }

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], email=validated_data['email'], password=validated_data['password'])
        token = Token.objects.create(user=user)
        UserProfile.objects.create(user=user)
        return user
