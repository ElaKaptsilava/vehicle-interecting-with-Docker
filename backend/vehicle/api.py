from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet, RateViewSet


router = DefaultRouter()

router.register(r'vehicles', VehicleViewSet, basename='vehicles')
router.register(r'rates', RateViewSet, basename='rates')

vehicle_urlpatterns = router.urls
