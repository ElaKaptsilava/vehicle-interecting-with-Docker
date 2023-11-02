from django.contrib import admin
from django.urls import path
from vehicle.api import api as vehicle_api

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += vehicle_api.vehicle_urlpatterns
