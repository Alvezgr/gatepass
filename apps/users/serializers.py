"""Module for users serializers."""

# Utilities
from typing import Dict
import jwt

# Django
from django.contrib.auth import password_validation, authenticate
from django.conf import settings

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Model
from apps.users.models import User


# Simple Token
from rest_framework_simplejwt.tokens import RefreshToken


class UserModelSerializer(serializers.ModelSerializer):
    """Model user serializers"""

    class Meta:
        """Meta options."""
        model = User
        fields = (
            'username',
            'email',
            'is_verified',
        )


class UserLoggedInSerializer(serializers.Serializer):
    """User Logged in serializers, represent a logged in user."""
    token = serializers.CharField(max_length=500)
    user = UserModelSerializer()


class UserSignUpSerializer(serializers.Serializer):
    """User signup Serializer
    handle sign up data validation and user/padron creation.
    """
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,

        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    # Password
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data: Dict) -> Dict:
        """verify that the passwords match."""
        passwd = data['password']
        passwd_conf = data['password_confirmation']

        if passwd != passwd_conf:
            raise serializers.ValidationError("Las contraseñas no coinciden.")
        password_validation.validate_password(passwd)
        return data

    def create(self, validated_data: Dict) -> User:
        validated_data.pop('password_confirmation')
        user = User.objects.create_user(**validated_data, is_verified=False)
        return user


class UserLoginSerializer(serializers.Serializer):
    """User login serializer"""
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data: Dict) -> Dict:
        """Verify that a user exist and can be authenticated."""
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Credenciales invalidas")
        if not user.is_verified:
            raise serializers.ValidationError("La cuenta no fue verificada aún!")
        self.context['user'] = user
        return data

    def create(self, data: Dict) -> Dict:
        """Generate or retrieve new token."""
        user = self.context['user']
        token = RefreshToken.for_user(user).access_token
        data = {
            'token': str(token),
            'user': UserModelSerializer(user).data
        }
        return data


class AccountVerificationSerializer(serializers.Serializer):
    """Account verification serializer."""

    token = serializers.CharField()

    def validate_token(self, data: str) -> str:
        """Verify that a token is valid."""
        try:
            payload = jwt.decode(data, settings.SECRET_KEY, algorithms=['HS256',])
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError("El token ha expirado.")
        except jwt.PyJWTError:
            raise serializers.ValidationError("Token invalido.")
        if payload['type'] != 'email_confirmation':
            raise serializers.ValidationError("Token invalido.")

        self.context['payload'] = payload
        return data

    def save(self) -> None:
        """Update user's verified status."""
        payload = self.context['payload']
        user = User.objects.get(username=payload['user'])
        if user.is_verified:
            raise serializers.ValidationError({"message": "Este token ya fue usado."})
        user.is_verified = True
        user.save()
