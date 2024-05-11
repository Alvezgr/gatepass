# Generated by Django 4.2.13 on 2024-05-11 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Neighborhood",
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
                        help_text="El nombre de la urbanización", max_length=255
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        help_text="La dirección de la urbanización", max_length=255
                    ),
                ),
                (
                    "max_vehicles",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="La maxima cantidad de vehículo que pueden ingresar",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Gate",
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
                ("number", models.PositiveIntegerField(help_text="Número de puerta")),
                (
                    "code",
                    models.CharField(help_text="El código de la puerta", max_length=10),
                ),
                (
                    "neighborhood",
                    models.ForeignKey(
                        help_text="La urbanización a la que pertenece la puerta",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="neighborhood.neighborhood",
                    ),
                ),
            ],
            options={
                "unique_together": {("number", "neighborhood")},
            },
        ),
    ]
