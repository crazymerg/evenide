import requests
import pytest
import json
import os


class Api:
    _port = os.environ['APP_PORT']
    _base_url = f'http://localhost:{_port}'
    _check_one_url = '/check_is_even'
    _select_even_url = '/select_even'
    _get_random_url = '/get_random_even'

    def get_random_even(self, min, max):
        r = requests.get(f'{self._base_url}{self._get_random_url}?min={min}&max={max}')

        return r.json()
    
    def check_is_even(self, number):
        r = requests.get(f'{self._base_url}{self._check_one_url}/{number}')

        return r.json()

    def select_even(self, array):
        headers = {'Content-Type': 'application/json'}

        r = requests.post(f'{self._base_url}{self._select_even_url}', data=json.dumps(array), headers=headers)
        return r.json()


@pytest.fixture
def api():
    api = Api()

    return api
