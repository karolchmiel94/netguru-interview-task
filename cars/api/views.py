import urllib
import json
import time

from django.db import transaction
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins, viewsets


from .serializers import (
    CarPopularitySerializer, CarSerializer, RatingSerializer
)
from ..models import (Car, CarMaker, Rating)
from .vehicle_api_service import get_car_model


class CarViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin):
    model = Car
    # queryset = Car.objects.all()
    queryset = Car.objects.select_related('make')
    serializer_class = CarSerializer

    def create(self, request, *args, **kwargs):
        maker = urllib.parse.quote_plus(request.data.get('make'))
        if not maker:
            return Response('Make name cannot be empty.', status=status.HTTP_400_BAD_REQUEST)
        model = request.data.get('model').lower()
        if not model:
            return Response('Model name cannot be empty.', status=status.HTTP_400_BAD_REQUEST)
        try:
            car = get_car_model(maker, model)
        except Exception as error:
            return Response(error.message, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # call CarAPIService and get data about available models for given maker
        url = 'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{f}?format=json'.format(f=maker)
        models_request = urllib.request.urlopen(url)
        models_response = models_request.read().decode('utf-8')
        data = json.loads(models_response)

        # find model within results
        models = data.get('Results')
        for model_obj in models:
            if model_obj.get('Model_Name').lower() == model:
                print('found pair')
                # if model is found, create model and maker if necessary
                serializer = self.get_serializer(data={'make': model_obj.get('Make_Name'), 'model': model_obj.get('Model_Name')})
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response('Car with given Make and Model does not exist', status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    model = Rating
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class CarPopularityViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    model = Car
    queryset = Car.objects.order_by('-rates_number')
    serializer_class = CarPopularitySerializer