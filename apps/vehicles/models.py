"""Main module for vehicles models"""

# Django imports
from django.db import models


class Vehicle(models.Model):
    """
    Model for mapping data to vehicles
    """

    kind = models.ForeignKey(
        "VehicleKind",
        help_text="El tipo de vehiculo (auto, velero, bicicleta)",
        on_delete=models.DO_NOTHING
    )
    brand = models.CharField(help_text='La marca del vehiculo', max_length=255)
    color = models.CharField(help_text='El color del vehiculo', max_length=255)
    licence_plate = models.CharField(help_text='La patente del vehiculo', max_length=15)
    insurer = models.CharField(help_text='El nombre de la aseguradora')
    insurance_expiration = models.DateField(
        help_text='Fecha de vencimiento de la poliza de seguros en el formato DD/MM/YYYY'
    )

    def __str__(self):
        """str representation of a vehicle"""
        return f'{self.kind}: {self.color} Patente: {self.licence_plate}'


class VehicleKind(models.Model):
    """
    Model for mapping data of kind of vehicles
    """

    name = models.CharField(
        help_text="El nombre del tipo de vehiculo si es auto, velero, bicicleta... etc",
        max_length=20
    )

    def __str__(self):
        """str representation of a vehicle kind"""
        return self.name