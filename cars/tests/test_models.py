from django.test import TestCase

from cars.models import Car, CarMaker, Rating


class TestModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.car_maker = CarMaker.objects.create(name='BMW')
        cls.car = Car.objects.create(make=cls.car_maker, model='series 5')

    def test_rating_creation(self):
        rating = Rating.objects.create(car_id=self.car, rating=3)

        self.assertEquals(self.car.avg_rating, 3)
        self.assertEquals(self.car.rates_number, 1)

    def test_removing_rating(self):
        rating = Rating.objects.create(car_id=self.car, rating=5)
        rating.delete()

        self.assertIsNone(self.car.avg_rating)
        self.assertEquals(self.car.rates_number, 0)
