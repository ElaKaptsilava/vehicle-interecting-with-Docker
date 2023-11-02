from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet, RateViewSet


router = DefaultRouter()

router.register(r'vehicles', VehicleViewSet, basename='vehicle')
router.register(r'rates', RateViewSet, basename='rate')

vehicle_urlpatterns = router.urls
