"""Main module for neighborhoods view."""

# DRF imports
from rest_framework import viewsets

# Serializers imports
from apps.neighborhood.serializers import (
    NeighborhoodSerializer,
    GateSerializer,
)

# models imports
from apps.neighborhood.models import Neighborhood, Gate


class GateViewset(viewsets.ModelViewSet):
    """
    API endopoint for managing gates.
    """

    filterset_fields = "__all__"
    serializer_class = GateSerializer
    queryset = Gate.objects.all()


class NeighborhoodViewset(viewsets.ModelViewSet):
    """
    API endopoint for managing neighborhoods.
    """

    filterset_fields = "__all__"
    serializer_class = NeighborhoodSerializer
    queryset = Neighborhood.objects.all()
