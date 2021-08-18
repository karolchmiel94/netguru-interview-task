import json
import urllib

from django.core.cache import cache


class ModelNotFoundError(Exception):
    """No model has been found."""

    def __init__(self, message='Car with given Model does not exist for this Maker.'):
        self.message = message
        super().__init__()


class NoResultsError(Exception):
    """Car maker has not been found."""

    def __init__(self, message='No data. Check if Make name is valid.'):
        self.message = message
        super().__init__()


class VehicleAPIError(Exception):
    """Vehicle API returned error"""

    def __init__(self, message='Vehicle API returned error. Check if data is valid.'):
        self.message = message
        super().__init__()


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
                print('saving {f} to cache'.format(f=make))
                cache.set(make.lower(), models)
            return models
        except:
            raise VehicleAPIError()
    else:
        print('retrieved models from cache')
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
