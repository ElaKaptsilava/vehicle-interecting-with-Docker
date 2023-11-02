from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from vehicle import api as vehicle_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema', SpectacularAPIView.as_view(), name="schema"),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema'))
]

urlpatterns += vehicle_api.vehicle_urlpatterns
