from django.contrib import admin

from .models import Car, CarMaker, Rating

admin.site.index_template = 'memcache_status/admin_index.html'


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    model = Car
    list_display = ('id', 'make', 'model', 'avg_rating', 'rates_number')


@admin.register(CarMaker)
class CarMakerAdmin(admin.ModelAdmin):
    model = CarMaker
    list_display = ('id', 'name')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    model = Rating
    list_display = ('id', 'car_id', 'rating')
