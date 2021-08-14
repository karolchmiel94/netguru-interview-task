from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Car, Rating

@receiver(post_save, sender=Rating)
def update_car_rating(sender, instance, *args, **kwargs):
    car: Car = instance.car_id
    car.update_rating(instance.rating)

@receiver(post_delete, sender=Rating)
def remove_car_rating(sender, instance, *args, **kwargs):
    car: Car = instance.car_id
    car.update_rating(instance, True)
