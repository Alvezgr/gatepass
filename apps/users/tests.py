"""Testing module for users app"""

# Django REST Framework
from apps.users.helpers import gen_verification_token
from rest_framework import status
from rest_framework.test import APITestCase

# Django imports
from django.urls import reverse

# Models
from apps.users.models import User


class UserTest(APITestCase):
    """Tests cases for users."""
    
    def setUp(self):
        """Default setting for testing person."""
        self.anonymous_user = User.objects.create(
            username='gera', email='gera@gatepass.com.ar'
        )
        self.anonymous_user.set_password("salto en largo")
        self.anonymous_user.save()
        self.anonymous_user_2 = User.objects.create(
            username="gera2",
            email="gera2@gatepass.com.ar",
            is_verified=False
        )
        self.signup_user = User.objects.create(
            username='gera_logged', email='gera_logged@gatepass.com.ar'
        )
        self.signup_user.set_password("salto en largo")
        self.signup_user.save()


    def test_signup(self):
        """Ensures an user can signup."""
        url = reverse('users:users-signup')
        data = {
            "email": "testmania@gatepass.com.ar",
            "username": "testing",
            "password": "salto en largo",
            "password_confirmation": "salto en largo",
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_fail_signup(self):
        """Ensures that an already signup user can't signup again."""
        url = reverse('users:users-signup')
        data = {
            "email": "gera@gatepass.com.ar",
            "username": "gera",
            "password": "salto en largo",
            "password_confirmation": "salto en largo",
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.data['email'][0], 'This field must be unique.')
        self.assertEqual(response.data['username'][0], 'This field must be unique.')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_verify(self):
        """Ensures an user can verify his account."""
        token = gen_verification_token(self.anonymous_user_2)
        path = reverse('users:users-verify')
        url = path + f'?token={token}'

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_fail_verify(self):
        """Ensures a verified user can't verify again."""
        token = gen_verification_token(self.anonymous_user)
        path = reverse('users:users-verify')
        url = path + f'?token={token}'

        response = self.client.get(url, format='json')

        self.assertEqual(response.data['message'], 'Este token ya fue usado.')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login(self):
        """Ensures an user can log in."""
        url = reverse('users:users-login')
        data = {
            "email": "gera@gatepass.com.ar",
            "password": "salto en largo",
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_fail_login(self):
        """Ensures an invalid user can't log in."""
        url = reverse('users:users-login')
        data = {
            "email": "gera@gatepass.com",
            "password": "salto en corto",
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.data['non_field_errors'][0], 'Credenciales invalidas')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_fail_list_users(self):
        """Ensures that an anonymous user can't list users."""
        url = reverse('users:users-list')
        response = self.client.get(url, format='json')
        self.assertEqual(
            response.data['detail'],
            'Authentication credentials were not provided.'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_users(self):
        """Ensures that we can list users."""
        url = reverse('users:users-list')
        self.client.force_authenticate(user=self.signup_user)
        response = self.client.get(url, format='json')
        self.assertEqual(
            response.data['results'][0]['username'],
            'gera_logged'
        )
        self.assertEqual(
            response.data['results'][0]['email'],
            'gera_logged@gatepass.com.ar'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
