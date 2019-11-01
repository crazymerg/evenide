import pytest


def test_random_even(api):
    random_even = api.get_random_even(2, 1337)
    
    assert random_even['status'] == 200
    assert random_even['body']['result'] % 2 == 0

@pytest.mark.parametrize('number, expected', [(10, True), (9, False)])
def test_is_even(api, number, expected):
    is_even = api.check_is_even(number)

    assert is_even['status'] == 200
    assert is_even['body']['result'] is expected


def test_select_even(api):
    response = api.select_even([1,2,3,4,5])

    assert response['body']['result']==[2,4]
