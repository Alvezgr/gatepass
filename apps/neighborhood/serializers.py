"""Main serializers for vehicles."""

# Django REST Framework imports
from typing import Dict
from rest_framework import serializers

# Models imports
from apps.neighborhood.models import Gate, Neighborhood


class GateSerializer(serializers.ModelSerializer):
    """Gate serializer"""

    def validate(self, data: Dict) -> Dict:
        gate = Gate.objects.filter(
            number=data.get("number"),
            neighborhood=data.get("neighborhood"),
        )
        if gate.exists():
            raise serializers.ValidationError(
                {
                    "error": ["Ya existe una puerta creada para este vecindario.",]
                }

            )
        return data

    class Meta:
        """Meta class"""

        model = Gate
        validators = []
        fields = "__all__"


class NeighborhoodSerializer(serializers.ModelSerializer):
    """Neighborhoods main serializer"""

    def validate_name(self, value: str) -> str:
        """Ensure that this name is taken"""
        neighborhood = Neighborhood.objects.filter(name=value)
        if neighborhood.exists():
            raise serializers.ValidationError(
                "Este vecindario ya existe.",
            )
        return value

    class Meta:
        """Meta class"""

        model = Neighborhood
        fields = "__all__"
