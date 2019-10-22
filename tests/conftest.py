import requests
import pytest
import json


class Api:
    _base_url = 'http://localhost:8080'
    _check_one_url = '/check_is_even'
    _select_even_url = '/select_even_numbers'
    _get_random_url = '/get_random_even'
    
    def get_random_even(self, number_range):
        r = requests.get(f'{self._base_url}{self._get_random_url}/{number_range}')

        return r.json()
    
    def check_is_even(self, number):
        r = requests.get(f'{self._base_url}{self._check_one_url}/{number}')

        return r.json()['result']

    def select_even(self, arr):
        headers = {'Content-Type': 'application/json'}
        params = json.dumps(arr)
        
        r = requests.post(f'{self._base_url}{self._select_even_url}', params=params, headers=headers)
        print(r.text)
        return r.text


@pytest.fixture
def api():
    api = Api()

    return api
