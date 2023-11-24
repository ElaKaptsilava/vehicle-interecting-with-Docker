import json

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Vehicle, Rate
from .serializers import VehicleSerializer, RateSerializer
from .views import VehicleViewSet
import responses


class TestPostVehicle(APITestCase):
    def test_post_vehicle(self):
        vehicle_data = {"make_name": "hon",
                        "model_name": "Accord"}

        response = self.client.post('/vehicles/', json.dumps(vehicle_data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['model_name'], 'Accord')

    def test_post_should_return_400_if_queryset_not_submitted(self):
        vehicle_data = {"make_name": None,
                        "model_name": None}

        response = self.client.post('/vehicles/', json.dumps(vehicle_data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data,
                         {"message": "Model_name: None, "
                                     "make_name: None, are required parameters"})

    def test_post_should_return_exception_when_ObjectDoesNotExist(self):
        with self.assertRaises(ObjectDoesNotExist):
            VehicleViewSet.create_from_link('hon', 'hon')


class TestCreateFromLink(APITestCase):
    @responses.activate
    def test_get_link_should_return_valid_data(self):
        url = r'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformakeyear/make/ford/vehicleType/car?format=json'
        mock_data = {
            "Count": 2,
            "Message": "Response returned successfully",
            "SearchCriteria": "Make:Ford",
            "Results": [
                {
                    "Make_ID": 460,
                    "Make_Name": "Ford",
                    "Model_ID": 1860,
                    "Model_Name": "Mustang"
                },
                {
                    "Make_ID": 460,
                    "Make_Name": "Ford",
                    "Model_ID": 1861,
                    "Model_Name": "Fiesta"
                }
            ]
        }
        responses.add(responses.GET, url, json=mock_data, status=200)

        data = VehicleViewSet.create_from_link("Mustang", "ford")

        self.assertEqual(data, {
            'make_ID': 460, 'make_name': 'Ford', 'model_name': 'Mustang'
        })

    def test_should_return_True_when_post_vehicle_exist(self):
        vehicle_data = VehicleViewSet.create_from_link('Accord', 'hon')

        self.assertTrue(vehicle_data)


class TestPopularVehicle(APITestCase):
    def setUp(self):
        self.civic = Vehicle.objects.create(**{"make_ID": 474, "make_name": "HONDA", "model_name": "Civic"})
        self.hon = Vehicle.objects.create(**{"make_ID": 454, "make_name": "HONDA", "model_name": "Hon"})

        self.rate_civic = Rate.objects.create(rate=5)
        self.rate_hon = Rate.objects.create(rate=1)

        self.rate_civic.vehicle.set([self.civic])
        self.rate_hon.vehicle.set([self.hon])

    def test_get_vehicle_rate(self):
        vehicle = Vehicle.objects.get(id=5)
        rate_serializer = RateSerializer(vehicle.rate_set, many=True)

        response = self.client.get(f'/vehicles/{vehicle.id}/rate/', content_type='application/json', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, rate_serializer.data)

    def test_get_popular_vehicle_by_bayesian(self):
        response_popular = self.client.get(f'/vehicles/popular/', content_type='application/json', format='json')

        self.assertEqual(response_popular.status_code, status.HTTP_200_OK)

    def test_get_popular_vehicle(self):
        vehicle = Vehicle.objects.get(id=1)
        vehicle_serializer = VehicleSerializer(vehicle)

        response_popular = self.client.get(f'/vehicles/max_rate/', content_type='application/json', format='json')

        self.assertEqual(response_popular.status_code, status.HTTP_200_OK)
        self.assertEqual(response_popular.data, vehicle_serializer.data)
