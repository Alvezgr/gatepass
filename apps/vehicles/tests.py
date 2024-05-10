"""Module for brand testing."""

# Django
from django.urls import reverse

# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Models
from apps.vehicles.models import VehicleKind, Vehicle
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
        Ensure can create a vehicle kind.
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
        Ensure an already created vehicle kind can't be created again.
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


class VehicleTests(APITestCase):
    """Test cases for vehicle"""

    def setUp(self):
        """Default setting for testing vehicles."""
        self.vehicle_kind = VehicleKind.objects.create(name="auto")
        self.vehicle = Vehicle.objects.create(
            kind=self.vehicle_kind,
            brand="chevi",
            color="brown",
            license_plate="ARD 1233B",
            insurer="libre seguros",
            insurance_expiration="2025-03-02"
        )
        self.user = User.objects.create(username='gera', email='gera@gatepass.com.ar')

    def test_fail_unathorized_user_create_vehicle(self):
        """
        Ensure an unauthorized user can't create a vehicle.
        """
        url = reverse('vehicles:vehicles-list')
        data = {
            "kind": self.vehicle_kind.pk,
            "brand": "ford",
            "color": "redblue",
            "license_plate": "ADB 1334A",
            "insurer": "libre seguros",
            "insurance_expiration": "2025-03-02"
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_fail_create_vehicle_without_kind(self):
        """
        Ensure we must provide a kind to create a vehicle.
        """
        url = reverse('vehicles:vehicles-list')
        data = {
            "brand": "ford",
            "color": "redblue",
            "license_plate": "ADB 1334A",
            "insurer": "libre seguros",
            "insurance_expiration": "2025-03-02"
        }

        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['kind'][0], 'This field is required.')

    def test_fail_create_vehicle_created(self):
        """
        Ensure an already created with a license plate vehicle can't be created again.
        """
        url = reverse('vehicles:vehicles-list')

        data = {
            "kind": self.vehicle_kind.pk,
            "brand": "chevi",
            "color": "brown",
            "license_plate": "ARD 1233B",
            "insurer": "libre seguros",
            "insurance_expiration": "2025-03-02"
        }

        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['license_plate'][0],
            'Esta patente ya existe para un vehiculo.'
        )

    def test_create_vehicle(self):
        """
        Ensure we can create a vehicle.
        """
        url = reverse('vehicles:vehicles-list')

        data = {
            "kind": self.vehicle_kind.pk,
            "brand": "grand",
            "color": "red",
            "license_plate": "ARF 1233B",
            "insurer": "libre seguros",
            "insurance_expiration": "2025-03-02"
        }

        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['license_plate'], data['license_plate'])

    def test_update_vehicle(self):
        """
        Ensure we can update a vehicle.
        """
        url = reverse('vehicles:vehicles-detail', kwargs={'pk': self.vehicle.pk})

        data = {
            "insurance_expiration": "2026-03-02"
        }

        self.client.force_authenticate(user=self.user)
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['insurance_expiration'], data['insurance_expiration'])

    def test_summarize_vehicles(self):
        """
        Ensure we can sumarize vehicles by an attribute.
        """
        Vehicle.objects.create(
            kind=self.vehicle_kind,
            brand="ford",
            color="brown",
            license_plate="ARR 8239L",
            insurer="libre seguros",
            insurance_expiration="2025-03-02"
        )
        path = reverse('vehicles:vehicles-summarizer')

        url = path + '?field_name=color'

        self.client.force_authenticate(user=self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["count"], 2)
