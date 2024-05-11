"""Module for brand testing."""

# Django
from django.urls import reverse

# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Models
from apps.neighborhood.models import Neighborhood
from apps.users.models import User


class NeighborhoodTests(APITestCase):
    """Test cases for neighborhood"""

    def setUp(self):
        """Default setting for testing neighborhoods."""
        self.neighborhood = Neighborhood.objects.create(
            name="La emilia",
            address="Road 12",
            max_vehicles=10
        )
        self.user = User.objects.create(username="gera", email="gera@gatepass.com.ar")

    def test_fail_unathorized_user_create_neighborhood(self):
        """
        Ensure an unauthorized user can't create a neighborhood.
        """
        url = reverse("neighborhoods:neighborhoods-list")
        data = {
            "name": "Toro roso",
            "address": "Ruta 66",
            "max_vehicles": 20,
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_fail_create_neighborhood_without_name(self):
        """
        Ensure we must provide a kind to create a neighborhood.
        """
        url = reverse("neighborhoods:neighborhoods-list")

        data = {
            "address": "Ruta 66",
            "max_vehicles": 20,
        }

        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["name"][0], "This field is required.")

    def test_fail_create_neighborhood_created(self):
        """
        Ensure an already created with a license plate neighborhood can't be created again.
        """
        url = reverse("neighborhoods:neighborhoods-list")

        data = {
            "name": "La emilia",
            "address": "Ruta 66",
            "max_vehicles": 20,
        }

        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data["license_plate"][0],
            "Este vecindario ya existe.",
        )

    def test_create_neighborhood(self):
        """
        Ensure we can create a neighborhood.
        """
        url = reverse("neighborhoods:neighborhoods-list")
        
        data = {
            "name": "Toro rosos",
            "address": "Ruta 66",
            "max_vehicles": 20,
        }

        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["license_plate"], data["license_plate"])

    def test_update_neighborhood(self):
        """
        Ensure we can update a neighborhood.
        """
        url = reverse("neighborhoods:neighborhoods-detail", kwargs={"pk": self.neighborhood.pk})

        data = {"max_vehicles": 32}

        self.client.force_authenticate(user=self.user)
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["max_vehicles"], data["max_vehicles"]
        )
