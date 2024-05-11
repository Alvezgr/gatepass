"""
URL configuration for gatepass project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Django imports
from django.urls import path, include

# REST Framework imports
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Gate pass API",
        default_version="v1",
        description=f"API Documentation of gatepass.",
        terms_of_service="https://www.gatepass.com.ar/policies/terms/",
        contact=openapi.Contact(email="contact@gatepass.com.ar"),
        license=openapi.License(name="Rights reserves License"),
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path("api/v1/", include(("apps.users.urls", "users"), namespace="users")),
    path("api/v1/", include(("apps.vehicles.urls", "vehicles"), namespace="vehicles")),
    path("api/v1/", include(("apps.neighborhood.urls", "neighborhoods"), namespace="neighborhoods")),
    path("docs/", schema_view.with_ui("redoc", cache_timeout=0), name="openapiurl"),
]
