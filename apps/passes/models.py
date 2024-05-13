"""Main module for passes model."""

# Django imports
from django.db import models

# Local imports
from apps.utils.models import GPBaseModel
from apps.vehicles.models import Vehicle
from apps.neighborhood.models import Gate


class Pass(GPBaseModel):
    """
    Pass model map data for passes of vehicles on a gate of the neighborhood.
    """
    ACTIONS_PASS = (
        ('ingress', 'Ingreso'),
        ('egress', 'Egreso')
    )
    gate = models.ForeignKey(Gate, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    action = models.CharField(choices=ACTIONS_PASS, max_length=7)

    def __str__(self):
        return f'{self.action} for {self.vehicle} on gate {self.gate}'


class Alert(GPBaseModel):
    """
    Alert model record data Alert of vehicles on a gate of the neighborhood.
    alerts are authomatics and readonly.
    """
    ACTIONS_ALERT = (
        ('outside', 'Ya salio'),
        ('inside', 'Ya entro'),
        ('insurance', 'Poliza expirada')
    )
    gate = models.ForeignKey(Gate, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    alert = models.CharField(
        help_text="Se alerta si el vehículo ya esta adentro o ya salio.",
        choices=ACTIONS_ALERT,
        max_length=9
    )

    def __str__(self):
        return f'{self.alert} for {self.vehicle} on gate {self.gate}'
