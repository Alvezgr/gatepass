"""Main serializers for vehicles."""

# Django REST Framework imports
from typing import Dict
from rest_framework import serializers

# Models imports
from apps.vehicles.models import VehicleKind, Vehicle


class VehicleKindSerializer(serializers.ModelSerializer):
    """Vehicle kind serializer"""

    def validate_name(self, value: str) -> str:
        """Ensure that this name is taken"""
        vehicle_kind = VehicleKind.objects.filter(name=value)
        if vehicle_kind.exists():
            raise serializers.ValidationError("Este nombre de vehiculo ya existe.")
        return value

    class Meta:
        """Meta class"""

        model = VehicleKind
        fields = "__all__"


class VehiclesSerializer(serializers.ModelSerializer):
    """Vehicles main serializer"""

    def validate_license_plate(self, value: str) -> str:
        """Ensure that this name is taken"""
        vehicle = Vehicle.objects.filter(license_plate=value)
        if vehicle.exists():
            raise serializers.ValidationError(
                "Esta patente ya existe para un vehiculo."
            )
        return value

    class Meta:
        """Meta class"""

        model = Vehicle
        fields = "__all__"


class QuerySummarizerSerializer(serializers.Serializer):
    field_name = serializers.CharField(
        help_text="Parametro sobre el cual se agrupan datos"
    )

    def validate(self, data: Dict) -> Dict:
        field_name = data.get("field_name")
        if not field_name:
            raise serializers.ValidationError(
                "Se requiere un atributo sobre el cual sumarizar."
            )
        if field_name not in [field.name for field in Vehicle._meta.fields]:
            raise serializers.ValidationError(
                f"{field_name} no es un atrributo valido para sumarizar. pruebe"
                f"con uno de los siguientes: {[field.name for field in Vehicle._meta.fields]}"
            )

        return data
