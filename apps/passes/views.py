"""Main module for passes view."""

# DRF imports
from rest_framework import viewsets
from rest_framework import serializers


# Serializers imports
from apps.passes.serializers import (
    PassesSerializer,
    AlertSerializer,
)

# models imports
from apps.passes.models import Alert, Pass


class AlertViewset(viewsets.ReadOnlyModelViewSet):
    """
    API endopoint for reading alerts.
    """

    filterset_fields = "__all__"
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

    def http_method_not_allowed(self, request, *args, **kwargs):
        if request.method.lower() == "post":
            raise serializers.ValidationError(
                "No se puede crear una alerta, las alertas son automaticas.",
            )
        return super().http_method_not_allowed(request, *args, **kwargs)




class PassesViewset(viewsets.ModelViewSet):
    """
    API endopoint for managing passes.
    """

    filterset_fields = "__all__"
    serializer_class = PassesSerializer
    queryset = Pass.objects.all()
