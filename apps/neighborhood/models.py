"""Main module for vehicles models"""

# Django imports
from django.db import models


class Neighborhood(models.Model):
    """
    Model for mapping data to neighborhood
    Neighborhood are private urbanizations where vehicles ingress and egreess from
    """
    name = models.CharField(help_text="El nombre de la urbanización", max_length=255)
    address = models.CharField(help_text="La dirección de la urbanización", max_length=255)
    max_vehicles = models.PositiveIntegerField(
        help_text="La maxima cantidad de vehículo que pueden ingresar", default=0
    )

    def __str__(self):
        """str representation of a neighborhood"""
        return f"Vecindario: {self.name}"


class Gate(models.Model):
    """
    Model for mapping data to neighborhood gates
    Gates belongs to a private urbanizations from which vehicles ingress and egreess from
    """
    number = models.PositiveIntegerField(help_text="Número de puerta")
    code = models.CharField(help_text="El código de la puerta", max_length=10)
    neighborhood = models.ForeignKey(
        "Neighborhood",
        help_text="La urbanización a la que pertenece la puerta",
        on_delete=models.CASCADE
    )

    class Meta:
        """Meta class for constraint definitions."""
        unique_together = ('number', 'neighborhood',)

    def __str__(self):
        """str representation of a neighborhood gate"""
        return f"Puerta: {self.number} código: {self.code}"
