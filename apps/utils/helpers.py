"""
Main helpers module
Here are the commond utilities between all apps.
"""

# Jwt
import jwt

# django imports
from django.utils import timezone
from django.conf import settings

# Utils imports
from datetime import timedelta

# Users imports
from apps.users.models import User


def gen_verification_token(user: User) -> str:
    """Generate a JWT token that the user can use to verify its account."""
    exp_date = timezone.now() + timedelta(days=3)
    payload = {
        'user': user.username,
        'exp': int(exp_date.timestamp()),
        'type': 'email_confirmation',
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token

