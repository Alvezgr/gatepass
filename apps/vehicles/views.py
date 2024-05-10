"""Main module for vehicles view."""

# django imports
from django.db.models import Count

# DRF imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action

# Django Rest Framework YASG
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Serializers imports
from apps.vehicles.serializers import QuerySummarizerSerializer, VehicleKindSerializer, VehiclesSerializer

# models imports
from apps.vehicles.models import VehicleKind, Vehicle


class VehicleKindViewset(viewsets.ModelViewSet):
    """
    API endopoint for managing vehicle kinds.
    """

    filterset_fields = "__all__"
    serializer_class = VehicleKindSerializer
    queryset = VehicleKind.objects.all()


class VehiclesViewset(viewsets.ModelViewSet):
    """
    API endopoint for managing vehicles.
    """

    filterset_fields = "__all__"
    serializer_class = VehiclesSerializer
    queryset = Vehicle.objects.all()

    @swagger_auto_schema(
        query_serializer=QuerySummarizerSerializer(),
        responses={
            "200": openapi.Response(
                description="Response",
                examples={
                    "application/json": {
                        "color": "brown",
                        "count": "40012",
                    }
                }
            ),
        }
    )
    @action(detail=False, methods=["get"], filter_backends=None, pagination_class=None)
    def summarizer(self, request):
        """
        This method aggregates data from a
        given model based on a specified attribute.

        """
        serializer = QuerySummarizerSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)

        sumarized = Vehicle.objects.values(
            'color'
        ).annotate(count=Count('color')).order_by()

        return Response(sumarized, status=status.HTTP_200_OK)
