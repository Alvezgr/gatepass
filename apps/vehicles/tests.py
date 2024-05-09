"""Module for brand testing."""

# Django
from django.urls import reverse

# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Models
from apps.vehicles.models import VehicleKind
from apps.users.models import User


class VehiclesKindTests(APITestCase):
    """Vehicle kind test cases."""

    def setUp(self):
        """Default setting for testing vehicles kinds."""
        self.name = 'auto'
        self.user = User.objects.create(username='gera', email='gera@gatepass.com.ar')
        self.vehicle_camion = VehicleKind.objects.create(name='camion')

    def test_fail_unathorized_user_create_vehicle_kind(self):
        """
        Ensure  can create a vehicle kind.
        """
        url = reverse('vehicles:vehicles-kind-list')
        data = {
            "name": "auto",
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_fail_create_vehicle_kind(self):
        """
        Ensure we must provide a name to create a vehicle kind.
        """
        url = reverse('vehicles:vehicles-kind-list')
        data = {
            "non_field": "auto",
        }

        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['name'][0], 'This field is required.')

    def test_fail_create_vehicle_camion(self):
        """
        Ensure an already exist vehicle kind can't be created again.
        """
        url = reverse('vehicles:vehicles-kind-list')
        data = {
            "name": "camion",
        }

        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['name'][0],
            'Este nombre de vehiculo ya existe.'
        )

    def test_create_vehicle_kind(self):
        """
        Ensure we can create a vehicle kind.
        """
        url = reverse('vehicles:vehicles-kind-list')
        data = {
            "name": "auto",
        }

        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], data['name'])

