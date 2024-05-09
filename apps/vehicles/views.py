"""Main module for vehicles view."""

# DRF imports
from rest_framework import viewsets

# Serializers imports
from apps.vehicles.serializers import VehicleKindSerializer, VehiclesSerializer

# models imports
from apps.vehicles.models import VehicleKind, Vehicle


class VehicleKindViewset(viewsets.ModelViewSet):
    """
    A view set to retrieve and modify kind of vehicles.
    """

    filterset_fields = "__all__"
    serializer_class = VehicleKindSerializer
    queryset = VehicleKind.objects.all()


class VehiclesViewset(viewsets.ModelViewSet):
    """
    A view set to retrieve create, and modify vehicles.
    """

    filterset_fields = "__all__"
    serializer_class = VehiclesSerializer
    queryset = Vehicle.objects.all()
