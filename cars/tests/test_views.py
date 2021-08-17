from django.test import TestCase, Client
from django.test.client import RequestFactory
from django.urls import reverse

from cars.models import Car, CarMaker, Rating


class TestViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.factory = RequestFactory()

    def setUp(self):
        self.cars_list_url = reverse('cars:cars-list')
        self.cars_detail_url = reverse("cars:cars-detail", args=[1])
        self.popular_url = reverse('cars:popular-list')
        self.rating_url = reverse('cars:rating-list')

        self.car_maker1 = CarMaker.objects.create(name='TOYOTA')
        self.car1 = Car.objects.create(make=self.car_maker1, model='Yaris')

    def test_cars_list_GET(self):
        response = self.client.get(self.cars_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.data), 1)

    def test_car_list_POST_valid_data(self):
        response = self.client.post(
            self.cars_list_url, {'make': 'TOYOTA', 'model': 'Corolla'}
        )

        self.assertEquals(response.status_code, 201)
        self.assertEquals(response.data.get('make'), 'TOYOTA')
        self.assertEquals(response.data.get('model'), 'Corolla')

    def test_car_detail_DELETE(self):
        response = self.client.delete(self.cars_detail_url)

        self.assertEquals(response.status_code, 204)

    def test_popular_list_GET(self):
        response = self.client.get(self.popular_url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.data), 1)

    def test_rating_list_POST_valid_data(self):
        response = self.client.post(self.rating_url, {'car_id': 1, 'rating': 3})

        self.assertEquals(response.status_code, 201)
        self.assertEquals(response.data.get('car_id'), 1)
        self.assertEquals(response.data.get('rating'), 3)

    def test_rating_list_POST_invalid_car_id(self):
        response = self.client.post(self.rating_url, {'car_id': 2, 'rating': 3})

        self.assertEquals(response.status_code, 400)
        self.assertEquals(response.data.get('car_id')[0].code, 'does_not_exist')

    def test_rating_list_POST_invalid_rating(self):
        response = self.client.post(self.rating_url, {'car_id': 2, 'rating': 3.5})

        self.assertEquals(response.status_code, 400)
        self.assertEquals(response.data.get('rating')[0].code, 'invalid')
