"""Main module for vehicles view."""

# DRF imports
from rest_framework import viewsets

# Serializers imports
from apps.vehicles.serializers import VehicleKindSerializer, VehiclesSerializer

# models imports
from apps.vehicles.models import VehicleKind, Vehicle


class VehicleKindViewset(viewsets.ModelViewSet):
    """
    API endopoint for managing vehicle kinds.
    """

    filterset_fields = "__all__"
    serializer_class = VehicleKindSerializer
    queryset = VehicleKind.objects.all()


class VehiclesViewset(viewsets.ModelViewSet):
    """
    API endopoint for managing vehicles.
    """

    filterset_fields = "__all__"
    serializer_class = VehiclesSerializer
    queryset = Vehicle.objects.all()
