from rest_framework.routers import DefaultRouter
from .views import OrderItemViewSet

router = DefaultRouter()
router.register(r'items', OrderItemViewSet, basename="items")


urlpatterns = router.urls
