from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from FooFi_api import serializers
from FooFi_api import models
from FooFi_api import permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
   """Handles creating user authentication tokens"""
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class TaskEntryViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating task entries"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.TaskEntrySerializer
    queryset = models.TaskEntry.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    ordering_fields = ('created_on', 'due_date')
    search_fields = ('title', 'description')

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
