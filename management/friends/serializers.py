#from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
    
from rest_framework import serializers
from friendship.models import Friend, FriendshipRequest, Follow


User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'email')


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')

class FriendSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Friend
        fields = ('url', 'from_user_id')

class FriendshipRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FriendshipRequest
        fields = ('id', 'from_user', 'to_user', 'message', 'created', 'rejected', 'viewed')
