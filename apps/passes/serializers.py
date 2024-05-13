"""Main serializers for vehicles."""

# Utils imports
import datetime
from typing import Dict

# Django REST Framework imports
from rest_framework import serializers

# Models imports
from apps.passes.models import Pass, Alert


class PassesSerializer(serializers.ModelSerializer):
    """Passes main serializer"""

    def create(self, validated_data: Dict) -> Dict:
        """Custom validate to ensure alerts creation"""
        vehicle = validated_data.get("vehicle")
        gate = validated_data.get("gate")
        action = validated_data.get("action")
        today = datetime.date.today()

        last_action = Pass.objects.filter(
            vehicle=vehicle,
            gate=gate,
            action=action
        ).last()
        alert_type = "outside" if action == "egress" else "inside"

        if last_action and action == last_action.action:
            Alert.objects.create(
                vehicle=vehicle,
                gate=gate,
                alert="outside" if action == "egress" else "inside"
            )

            raise serializers.ValidationError(
                f"Se creo una alerta, el vehiculo {dict(Alert.ACTIONS_ALERT)[alert_type].lower()}."
            )
        if vehicle.insurance_expiration < today:
            Alert.objects.create(
                vehicle=vehicle,
                gate=gate,
                alert="insurance"
            )
            raise serializers.ValidationError(
                "Se creo una alerta, el vehiculo tiene la poliza vencida."
            )
        return validated_data

    class Meta:
        """Meta class"""

        model = Pass
        fields = "__all__"


class AlertSerializer(serializers.ModelSerializer):
    """Alert serializer"""

    class Meta:
        """Meta class for alert serializer."""
        model = Alert
        fields = "__all__"
