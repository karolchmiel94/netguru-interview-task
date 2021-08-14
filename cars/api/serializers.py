from django.db import IntegrityError

from rest_framework import serializers

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

    def create(self, validated_data):
        make_data = validated_data.pop('make')
        make = None
        try:
            make = CarMaker.objects.get(name=make_data)
        except CarMaker.DoesNotExist:
            make = CarMaker.objects.create(name=make_data)
        try:
            car = Car.objects.create(make=make, **validated_data)
        except IntegrityError as e:
            # this error has to be handled properly
            return e
        return car


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ['id', 'car_id', 'rating']