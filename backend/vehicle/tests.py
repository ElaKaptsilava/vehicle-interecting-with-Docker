import json

from django.urls import reverse
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.test import APITestCase

from .models import Vehicle, Rate
from .views import VehicleViewSet
import responses


class TestApiVehicle(APITestCase):
    def setUp(self):
        self.url = r'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformakeyear/make/Ford/vehicleType/car?format=json'
        self.mock_data = {
            "Count": 2,
            "Message": "Response returned successfully",
            "SearchCriteria": "Make:Ford",
            "Results": [
                {
                    "Make_ID": 460,
                    "Make_Name": "Ford",
                    "Model_Name": "Mustang"
                },
                {
                    "Make_ID": 460,
                    "Make_Name": "Ford",
                    "Model_Name": "Fiesta"
                }
            ]
        }

        self.vehicle1 = Vehicle.objects.create(make_ID=460, make_name='Ford', model_name='vehicle1')
        self.vehicle2 = Vehicle.objects.create(make_ID=470, make_name='Ford', model_name='vehicle2')
        self.vehicle3 = Vehicle.objects.create(make_ID=480, make_name='Ford', model_name='vehicle3')

        self.rate_vehicle_1 = Rate.objects.create(rate=3)
        self.rate_vehicle_2 = Rate.objects.create(rate=5)
        self.rate_vehicle_3 = Rate.objects.create(rate=4)

        self.rate_vehicle_1.vehicle.set([self.vehicle1])
        self.rate_vehicle_2.vehicle.set([self.vehicle2])
        self.rate_vehicle_3.vehicle.set([self.vehicle2])

    @responses.activate
    def test_create_vehicle_from_link(self):
        responses.add(responses.GET, self.url, json=self.mock_data, status=200)

        data = VehicleViewSet.create_from_link("Mustang", "Ford")

        self.assertEqual(data, {
            'make_ID': 460, 'make_name': 'Ford', 'model_name': 'Mustang'
        })

    @responses.activate
    def test_create_vehicle_from_link_should_return_exception(self):
        responses.add(responses.GET, self.url, json=self.mock_data, status=200)
        with self.assertRaises(APIException):
            VehicleViewSet.create_from_link('hon', 'Ford')

    @responses.activate
    def test_post_vehicle(self):
        responses.add(responses.GET, self.url, json=self.mock_data, status=200)
        vehicle_data = {"make_name": "Ford",
                        "model_name": "Mustang"}

        response = self.client.post('/vehicles/', json.dumps(vehicle_data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {
            'make_ID': 460, 'make_name': 'Ford', 'model_name': 'Mustang'})

    def test_get_vehicle_rate(self):
        response = self.client.get(reverse('vehicles-rate', kwargs={'pk': self.vehicle1.pk, }),
                                   content_type='application/json')

        result = response.json()

        self.assertEqual(len(result), 1)

    def test_get_popular_vehicle(self):
        response = self.client.get(reverse('vehicles-popular'), content_type='application/json')

        expected_value = {'make_ID': 470, 'make_name': 'Ford', 'model_name': 'vehicle2'}

        self.assertEqual(response.json(), expected_value)

    def test_get_popular_vehicle_by_bayesian(self):
        response = self.client.get(reverse('vehicles-popular-by-bayesian'), content_type='application/json')

        expected_value = {'make_ID': 460, 'make_name': 'Ford', 'model_name': 'vehicle1'}

        self.assertEqual(response.json(), expected_value)
