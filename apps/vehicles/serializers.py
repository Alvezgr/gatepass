"""Main serializers for vehicles."""

# Django REST Framework imports
from rest_framework import serializers

# Models imports
from apps.vehicles.models import VehicleKind


class VehicleKindSerializer(serializers.ModelSerializer):
    """Vehicle kind serializer"""

    def validate_name(self, value: str) -> str:
        """Ensure that this name is taken"""
        vehicle_kind = VehicleKind.objects.filter(name=value)
        if vehicle_kind.exists():
            raise serializers.ValidationError(
                "Este nombre de vehiculo ya existe."
            )
        return value

    class Meta:
        """Meta class"""
        model = VehicleKind
        fields = '__all__'
