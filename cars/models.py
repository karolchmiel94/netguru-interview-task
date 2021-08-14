from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from utils.model_utils import TimeStampMixin

class CarMaker(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Car(models.Model):
    make = models.ForeignKey(CarMaker, on_delete=models.CASCADE)
    model = models.CharField(max_length=255)
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    rates_number = models.PositiveIntegerField(default=0)

    def update_rating(self, rating, remove_rating=False):
        if remove_rating:
            self.rates_number -= 1
        else:
            self.rates_number += 1
        if remove_rating:
            if self.rates_number == 0:
                self.avg_rating = None
            else:
                self.avg_rating = self.avg_rating - ((rating - self.avg_rating) / self.rates_number)
        else:
            if self.avg_rating:
                self.avg_rating = self.avg_rating + ((rating - self.avg_rating) / self.rates_number)
            else:
                self.avg_rating = rating
        self.save()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['make', 'model'], name='unique model for maker')
        ]


class Rating(TimeStampMixin):
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])