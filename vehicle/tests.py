from rest_framework import status
from rest_framework.test import APITestCase


class VehicleTestCase(APITestCase):
    def setUp(self):
        pass

    def test_create_car(self):
        data = {
            'title': 'Car',
            'description': 'Car description',
        }

        response = self.client.post('/cars/', data=data)
        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
