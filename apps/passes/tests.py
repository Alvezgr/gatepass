"""Module for brand testing."""

# Django
from django.urls import reverse

# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Models
from apps.passes.models import Pass
from apps.users.models import User
from apps.neighborhood.models import Neighborhood, Gate
from apps.vehicles.models import VehicleKind, Vehicle


class PassTests(APITestCase):
    """Test cases for pass"""

    def setUp(self):
        """Default setting for testing passs."""
        self.vehicle_kind = VehicleKind.objects.create(name="auto")
        self.vehicle = Vehicle.objects.create(
            kind=self.vehicle_kind,
            brand="chevi",
            color="brown",
            model="2012",
            license_plate="ARD 1233B",
            insurer="libre seguros",
            insurance_expiration="2025-03-02",
        )
        self.vehicle2 = Vehicle.objects.create(
            kind=self.vehicle_kind,
            brand="Ford",
            color="red",
            model="2013",
            license_plate="ADD 1233B",
            insurer="libre",
            insurance_expiration="2025-03-02",
        )
        self.neighborhood = Neighborhood.objects.create(
            name="La emilia",
            address="Road 12",
            max_vehicles=10
        )
        self.gate = Gate.objects.create(
            number=1,
            code="AG22",
            neighborhood=self.neighborhood
        )
        self.passe = Pass.objects.create(
            gate=self.gate,
            vehicle=self.vehicle,
            action='ingress'
        )
        self.user = User.objects.create(
            username="gera", email="gera@alertpass.com.ar"
        )

    def test_fail_unathorized_user_create_pass(self):
        """
        Ensure an unauthorized user can't create a pass.
        """
        url = reverse("passes:passes-list")
        data = {
            "gate": self.gate.pk,
            "vehicle": self.vehicle.pk,
            "action": "ingress"
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_fail_create_pass_without_a_gate(self):
        """
        Ensure we must provide a kind to create a pass.
        """
        url = reverse("passes:passes-list")

        data = {
            "vehicle": self.vehicle.pk,
            "action": "ingress"
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["gate"][0], "This field is required.")

    def test_pass_created_generate_alert(self):
        """
        Ensure a pass with same information created an alert.
        """
        url = reverse("passes:passes-list")

        data = {
            "gate": self.gate.pk,
            "vehicle": self.vehicle.pk,
            "action": "ingress"
        }

        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(
            response.data["warning"][0],
            [
                "Se creo una alerta, el vehiculo ya salio.",
                "Se creo una alerta, el vehiculo ya entro.",
            ],
        )

    def test_create_pass(self):
        """
        Ensure we can create a pass.
        """
        url = reverse("passes:passes-list")
        
        data = {
            "gate": self.gate.pk,
            "vehicle": self.vehicle2.pk,
            "action": "ingress"
        }

        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], data["name"])

    def test_update_pass(self):
        """
        Ensure we can update a pass.
        """
        url = reverse("passes:passes-detail", kwargs={"pk": self.passe.pk})

        data = {"action": "egress"}

        self.client.force_authenticate(user=self.user)
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["action"], data["egress"]
        )

    def test_list_passes(self):
        """Ensure we can list passes."""
        url = reverse("passes:passes-list")
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AlertTests(APITestCase):
    """Test cases for alerts"""

    def setUp(self):
        """Default setting for testing alerts passs."""
        self.vehicle_kind = VehicleKind.objects.create(name="auto")
        self.vehicle = Vehicle.objects.create(
            kind=self.vehicle_kind,
            brand="chevi",
            color="brown",
            model="2012",
            license_plate="ARD 1233B",
            insurer="libre seguros",
            insurance_expiration="2025-03-02",
        )
        self.vehicle2 = Vehicle.objects.create(
            kind=self.vehicle_kind,
            brand="Ford",
            color="red",
            model="2013",
            license_plate="ADD 1233B",
            insurer="libre",
            insurance_expiration="2025-03-02",
        )
        self.neighborhood = Neighborhood.objects.create(
            name="La emilia",
            address="Road 12",
            max_vehicles=10
        )
        self.gate = Gate.objects.create(
            number=1,
            code="AG22",
            neighborhood=self.neighborhood
        )
        self.passe = Pass.objects.create(
            gate=self.gate,
            vehicle=self.vehicle,
            action='ingress'
        )
        self.user = User.objects.create(
            username="gera",
            email="gera@alertpass.com.ar"

        )

    def test_fail_create_alert(self):
        """
        Ensure noone can created alert by it self.
        Alerts are authomatic
        """
        url = reverse("passes:alerts-list")

        data = {
            "gate": self.gate.pk,
            "vehicle": self.vehicle.pk,
            "alert": "inside"
        }

        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data["error"][0],
            "No se puede crear una alerta, las alertas son automaticas.",
        )

    def test_list_alerts(self):
        """Ensure we can list alerts."""
        url = reverse("passes:alerts-list")
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

