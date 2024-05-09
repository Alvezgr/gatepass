"""main URL's for vehicles."""

# Django REST framework
from rest_framework.routers import DefaultRouter

# Views
from apps.vehicles.views import VehicleKindViewset

router = DefaultRouter()
router.register(r'vehicles-kind', VehicleKindViewset, basename='vehicles-kind')
urlpatterns = router.urls

