from rest_framework import status
from rest_framework.test import APITestCase

from vehicle.models import Car


class VehicleTestCase(APITestCase):
    def setUp(self):
        pass

    def test_create_car(self):
        """
        Тест создания автомобиля путем отправки POST-запроса на конечную точку '/cars/' с указанными данными,
        а затем проверка кода состояния ответа, JSON-данных и существования созданного объекта Car.
        """

        data = {
            'title': 'Car',
            'description': 'Car description',
        }

        response = self.client.post('/cars/', data=data)
        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(
            response.json(),
            {'id': 1, 'milage': [], 'title': 'Car', 'description': 'Car description', 'owner': None}
        )

        self.assertTrue(Car.objects.exists())

    def test_list_cars(self):
        """
        Тест получения списка автомобилей путем отправки GET-запроса на конечную точку '/cars/'.
        """

        Car.objects.create(title='Car list', description='Car description list')

        response = self.client.get('/cars/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            [{'id': 2, 'milage': [], 'title': 'Car list', 'description': 'Car description list', 'owner': None}]
        )
