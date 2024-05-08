"""module for a custom authorization."""

# Simple JWT
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken


class JWTAuthenticationSafe(JWTAuthentication):
    """This is a default custom JWT authorization for users views."""

    def authenticate(self, request):
        """authenticate overrider."""
        try:
            return super().authenticate(request=request)
        except InvalidToken:
            return None
