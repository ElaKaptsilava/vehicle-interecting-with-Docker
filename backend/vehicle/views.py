import requests

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction, models
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Vehicle, Rate
from .serializers import VehicleSerializer, RateSerializer


class RateViewSet(ModelViewSet):
    serializer_class = RateSerializer
    queryset = Rate.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['rate', 'vehicle']


class VehicleViewSet(ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['model_name', 'make_name']

    def create(self, request, *args, **kwargs):
        model_name = request.data.get('model_name', None)
        make_name = request.data.get('make_name', None)
        if model_name is not None and make_name is not None:
            vehicle_data = self.create_from_link(model_name_params=model_name, make_name_params=make_name)
            with transaction.atomic():
                serializer_vehicle = self.serializer_class(data=vehicle_data)
                if serializer_vehicle.is_valid():
                    serializer_vehicle.save()
                    return Response(serializer_vehicle.data)
                else:
                    return Response(
                        data={'message': f'{serializer_vehicle} is not valid'},
                        status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": f"Model_name: {model_name}, make_name: {make_name}, are required parameters"},
                        status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def create_from_link(model_name_params, make_name_params):
        url = r'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformakeyear/make/{0}/vehicleType/car?format=json'.format(
            make_name_params)
        get_link = requests.get(url)
        vpic_data = get_link.json()
        for item in vpic_data['Results']:
            if model_name_params == item['Model_Name']:
                data = {
                    'make_ID': item['Make_ID'], 'make_name': item['Make_Name'], 'model_name': item['Model_Name']
                }
                return data
        raise ObjectDoesNotExist(
            f'Vehicle with model name:{model_name_params}, make name:{make_name_params} dose not exist.'
            f'into link {url}'
        )

    @action(methods=['GET', ], detail=True, url_path='rate')
    def get_rate(self, request, pk=None):
        vehicle = Vehicle.objects.get(pk=pk)
        vehicle_rates = vehicle.rate_set.all()
        rate_serializer = RateSerializer(instance=vehicle_rates, many=True)
        return Response(rate_serializer.data)

    @action(methods=['GET'], detail=False, url_path='popular')
    def get_popular(self, request):
        vehicle_avg = self.queryset.aggregate(models.Avg('rate__rate'))['rate__rate__avg'] or 0
        max_value = 5
        popular = self.queryset.annotate(
            score=(max_value * vehicle_avg + models.Sum('rate__rate') + (max_value * models.Count('rate')))
        ).order_by('score')[:1]
        serializer = VehicleSerializer(instance=popular, many=True)
        return Response(serializer.data)
