from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from ..models import Car, CarMaker, Rating


class CarPopularitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'rates_number']


class CarSerializer(serializers.ModelSerializer):
    make = serializers.CharField()
    avg_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'avg_rating']

    def validate(self, data):
        """Validate whether standarised make and model data exists"""
        try:
            make = CarMaker.objects.get(name=data.get('make'))
            model = Car.objects.get(make=make, model=data.get('model'))
            raise serializers.ValidationError(
                'Car with this Model and Make already exists.'
            )
        except ObjectDoesNotExist:
            return data

    def create(self, validated_data):
        make_data = validated_data.pop('make')
        make = CarMaker.objects.get_or_create(name=make_data)[0]
        car = Car.objects.create(make=make, **validated_data)
        return car


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'car_id', 'rating']
