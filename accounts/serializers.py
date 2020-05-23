from django.contrib.auth import authenticate
from django.contrib.auth.models import Group, Permission
from rest_framework import serializers

from contacts.serializers import ContactSerializer
from .models import User, UserInformation


class GroupMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name"]


class UserSerializer(serializers.ModelSerializer):
    """
    User Serializer
    """
    groups = GroupMinimalSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups')
        depth = 1


class RegisterSerializer(serializers.ModelSerializer):
    """
    Register Serializer
    """

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])

        return user


class LoginSerializer(serializers.Serializer):
    """
    Login Serializer
    """
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class UserInformationSerializer(serializers.ModelSerializer):
    """"
    get All User Info
    """
    user = UserSerializer(read_only=True)
    contact = ContactSerializer(read_only=True)

    class Meta:
        model = UserInformation
        fields = ["user", "contact"]


class GroupSerializer(serializers.ModelSerializer):
    """
    Django groups
    https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.Group
    """

    class Meta:
        model = Group
        fields = "__all__"
        depth = 1


class PermissionSerializer(serializers.ModelSerializer):
    """
    Django Permissions
    https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.Permission
    """

    def create(self, validated_data):
        raise serializers.ValidationError("Permissions cannot be edited")

    def update(self, instance, validated_data):
        raise serializers.ValidationError("Permissions cannot be edited")

    class Meta:
        model = Permission
        fields = "__all__"
        depth = 1
