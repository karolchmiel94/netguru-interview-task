import urllib

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins, viewsets


from .serializers import CarPopularitySerializer, CarSerializer, RatingSerializer
from ..models import Car, CarMaker, Rating
from .vehicle_api_service import get_car_model


class CarViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
):
    model = Car
    queryset = Car.objects.select_related('make')
    serializer_class = CarSerializer

    def create(self, request, *args, **kwargs):
        maker = request.data.get('make')
        if not maker:
            return Response(
                'Make name cannot be empty.', status=status.HTTP_400_BAD_REQUEST
            )
        maker
        model = request.data.get('model').lower()
        if not model:
            return Response(
                'Model name cannot be empty.', status=status.HTTP_400_BAD_REQUEST
            )
        try:
            car = get_car_model(urllib.parse.quote(maker), model)
        except Exception as error:
            return Response(error.message, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        serializer = self.get_serializer(data=car)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    model = Rating
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class CarPopularityViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    model = Car
    queryset = Car.objects.order_by('-rates_number')
    serializer_class = CarPopularitySerializer
