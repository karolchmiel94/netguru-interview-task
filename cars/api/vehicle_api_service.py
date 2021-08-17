import json
import urllib


class ModelNotFoundError(Exception):
    """"""
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def fetch_data_for_maker(make):
    url = 'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{f}?format=json'.format(f=make)
    models_request = urllib.request.urlopen(url)
    models_response = models_request.read().decode('utf-8')
    return json.loads(models_response)


def get_car_model(maker, model):
    response = fetch_data_for_maker(maker)
    models = response.get('Results')
    if len(models) == 0:
        return Exception('No data. Check if Make name is valid.')
    else:
        for model_obj in models:
            if model_obj.get('Model_Name').lower() == model:
                return {
                    'make': model_obj.get('Make_Name'),
                    'model': model_obj.get('Model_Name')
                }
    return Exception('Car with given Model does not exist for this Maker.')
