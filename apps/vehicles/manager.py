"""Manager for vehicles."""

# Django imports
from django.db import models
from django.db.models import Count


class VehicleManager(models.Manager):
    """
    Custom manager to add aggregation functionalities.
    Adds a methods aggregate_by to performs aggregation on
    the queryset based on the specified field_name.
    """
    
    def aggregate_by(self, field_name: str):
        """
        Custom method to aggregate by a field_name
        Example:
        # Get a queryset aggregated by 'color' field
        aggregated_data = Vehicle.objects.aggregate_by('color')
        """

        summarized = self.get_queryset().values(
            field_name
        ).annotate(count=Count(field_name)).order_by()
        return summarized
