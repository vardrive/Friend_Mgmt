# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

#from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import detail_route, list_route
from management.friends.serializers import UserSerializer, FriendSerializer, FriendshipRequestSerializer
from friendship.models import Friend, FriendshipRequest, Follow

try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
    Group = get_user_model()
except ImportError:
    from django.contrib.auth.models import User
    user_model = User

class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

class FriendViewSet(viewsets.ViewSet):
    
    serializer_class = UserSerializer

    def list(self, request, email):
		user = get_object_or_404(User, email=email)
		friends = Friend.objects.friends(user)
		return Response(UserSerializer(friends, many=True).data)

    @list_route()
    def requests(self, request):
        friend_requests = Friend.objects.unrejected_requests(user=request.user)
        return Response(FriendshipRequestSerializer(friend_requests, many=True).data)

    @list_route()
    def sent_requests(self, request):
        friend_requests = Friend.objects.sent_requests(user=request.user)
        return Response(FriendshipRequestSerializer(friend_requests, many=True).data)

    @list_route()
    def rejected_requests(self, request):
        friend_requests = Friend.objects.rejected_requests(user=request.user)
        return Response(FriendshipRequestSerializer(friend_requests, many=True).data)

    def create(self, request, email):
        """
        Creates a friend request
        POST data:
        - user_id
        - message
        """
        # user = get_object_or_404(User, email=email)
        friend_obj = Friend.objects.add_friend(
            request.user,                             											# The sender
            get_object_or_404(get_user_model(), pk=request.data['user_id']), 					# The recipient
            message=request.data['message']
        )

        return Response(
            FriendshipRequestSerializer(friend_obj).data,
            status.HTTP_201_CREATED
        )


class FriendshipRequestViewSet(viewsets.ViewSet):

    @detail_route(methods=['post'])
    def accept(self, request, pk=None):
        friendship_request = get_object_or_404(FriendshipRequest, pk=pk)
        friendship_request.accept()
        return Response(
            FriendshipRequestSerializer(friendship_request).data,
            status.HTTP_201_CREATED
        )

    @detail_route(methods=['post'])
    def reject(self, request, pk=None):
        friendship_request = get_object_or_404(FriendshipRequest, pk=pk)
        friendship_request.reject()
        return Response(
            FriendshipRequestSerializer(friendship_request).data,
            status.HTTP_201_CREATED
        )

class FollowersViewSet(viewsets.ViewSet):
	def list(self, request, email):
		user = get_object_or_404(User, email=email)
		followers = Follow.objects.followers(user)
		return Response(UserSerializer(followers, many=True).data)

