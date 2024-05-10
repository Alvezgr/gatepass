"""main URL's for users."""

# Django

# Django REST framework
from rest_framework.routers import DefaultRouter

# Views
from apps.users.views import UsersViewset

router = DefaultRouter()
router.register(r"users", UsersViewset, basename="users")
urlpatterns = router.urls
