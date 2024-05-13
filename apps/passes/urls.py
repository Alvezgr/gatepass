"""main URL's for vehicles."""

# Django REST framework
from rest_framework.routers import DefaultRouter

# Views
from apps.passes.views import PassesViewset, AlertViewset

router = DefaultRouter()
router.register(r"passes", PassesViewset, basename="passes")
router.register(r"alerts", AlertViewset, basename="alerts")
urlpatterns = router.urls
