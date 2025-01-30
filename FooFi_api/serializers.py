from rest_framework import serializers
from FooFi_api import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes user profile objects, including user creation and updates."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Creates and returns a new user with a hashed password."""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class TaskEntrySerializer(serializers.ModelSerializer):
    """Serializes task entry objects"""

    class Meta:
        model = models.TaskEntry
        fields = ('id', 'user_profile', 'title', 'description', 'due_date',
        'completed', 'created_on', 'updated_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
