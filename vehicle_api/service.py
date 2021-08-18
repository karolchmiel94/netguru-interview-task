import json
import urllib

from django.core.cache import cache

from .exceptions import NoResultsError, ModelNotFoundError, VehicleAPIError


def fetch_data_for_maker(make):
    models = cache.get(make.lower())
    if not models:
        url = 'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{f}?format=json'.format(
            f=make
        )
        try:
            models_request = urllib.request.urlopen(url)
            models_response = json.loads(models_request.read().decode('utf-8'))
            models = models_response.get('Results')
            if len(models) != 0:
                cache.set(make.lower(), models)
            return models
        except:
            raise VehicleAPIError()
    else:
        return models


def get_car_model(maker, model):
    models = fetch_data_for_maker(maker)
    if len(models) == 0:
        raise NoResultsError()
    else:
        for model_obj in models:
            if model_obj.get('Model_Name').lower() == model:
                return {
                    'make': model_obj.get('Make_Name'),
                    'model': model_obj.get('Model_Name'),
                }
    raise ModelNotFoundError()
