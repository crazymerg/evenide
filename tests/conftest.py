import requests
import pytest
import json


class Api:
    _base_url = 'http://localhost:8080'
    _check_one_url = '/check_is_even'
    _select_even_url = '/select_even_numbers'
    _get_random_url = '/get_random_even'
    
    def get_random_even(self, min, max):
        r = requests.get(f'{self._base_url}{self._get_random_url}?min={min}&max={max}')

        return r.json()
    
    def check_is_even(self, number):
        r = requests.get(f'{self._base_url}{self._check_one_url}/{number}')

        return r.json()


@pytest.fixture
def api():
    api = Api()

    return api
