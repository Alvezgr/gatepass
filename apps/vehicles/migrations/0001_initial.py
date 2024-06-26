# Generated by Django 5.0.6 on 2024-05-09 20:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="VehicleKind",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="El nombre del tipo de vehiculo si es auto, velero, bicicleta... etc",
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Vehicle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "brand",
                    models.CharField(help_text="La marca del vehiculo", max_length=255),
                ),
                (
                    "model",
                    models.CharField(
                        help_text="El modelo del vehiculo", max_length=255
                    ),
                ),
                (
                    "color",
                    models.CharField(help_text="El color del vehiculo", max_length=255),
                ),
                (
                    "license_plate",
                    models.CharField(
                        help_text="La patente del vehiculo", max_length=15
                    ),
                ),
                ("insurer", models.CharField(help_text="El nombre de la aseguradora")),
                (
                    "insurance_expiration",
                    models.DateField(
                        help_text="Fecha de vencimiento de la poliza de seguros en el formato DD/MM/YYYY"
                    ),
                ),
                (
                    "kind",
                    models.ForeignKey(
                        help_text="El tipo de vehiculo (auto, velero, bicicleta)",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="vehicles.vehiclekind",
                    ),
                ),
            ],
        ),
    ]
