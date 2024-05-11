"""main URL's for neighborhoods."""

# Django REST framework
from rest_framework.routers import DefaultRouter

# Views
from apps.neighborhood.views import NeighborhoodViewset, GateViewset

router = DefaultRouter()
router.register(r"neighborhoods", NeighborhoodViewset, basename="neighborhoods")
router.register(r"gates", GateViewset, basename="gates")
urlpatterns = router.urls
