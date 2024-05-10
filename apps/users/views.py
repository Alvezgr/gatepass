"""User Views."""

# Utilities
from apps.users.authorization import JWTAuthenticationSafe

# Django REST Framework
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated

# Serializers
from apps.users.serializers import (
    UserModelSerializer,
    UserSignUpSerializer,
    UserLoginSerializer,
    AccountVerificationSerializer,
)

# Models
from apps.users.models import User


class UsersViewset(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet
):
    """View to handle Users requests."""

    serializer_class = UserModelSerializer
    queryset = User.objects.all()
    lookup_field = "username"
    authentication_classes = [JWTAuthenticationSafe]

    def get_permissions(self):
        """Assign permissions base on actions."""
        if self.action in ["signup", "login", "verify"]:
            permissions = [AllowAny]
        elif self.action in ["retrieve"]:
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def list(self, request, *args, **kwargs):
        """List all users."""
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["post"])
    def signup(self, requests):
        """Allow users to sign up."""
        serializer = UserSignUpSerializer(data=requests.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["post"])
    def login(self, requests):
        """User Log in"""
        serializer = UserLoginSerializer(data=requests.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(data, status=status.HTTP_202_ACCEPTED)

    @action(detail=False, methods=["get"])
    def verify(self, requests):
        """Allow a user to verify his account."""
        serializer = AccountVerificationSerializer(data=requests.GET)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {"message": "Gracias por verificar tu cuenta"}
        return Response(data, status=status.HTTP_200_OK)
