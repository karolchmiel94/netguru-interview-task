from django.urls import path
from django.urls.conf import include
from rest_framework import urlpatterns

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('cars', views.CarViewSet, basename='cars')
router.register('rate', views.RatingViewSet)
router.register('popular', views.CarPopularityViewSet, basename='popular')

app_name = 'cars'
urlpatterns = [
    path('', include(router.urls)),
]