import pytest
import requests
from variables import breweries_url


class TestBrewery:

    def test_brewery_list_not_empty(self, response_brewery_list):
        """
        Тест проверяет, что пришел список пивоварен
        """
        if response_brewery_list is not None:
            assert response_brewery_list
        elif response_brewery_list is not None:
            assert False, response_brewery_list
        else:
            assert False, 'Something wrong'

    @pytest.mark.parametrize('state', ["Alabama", "Alaska", "Arkansas"])
    def test_brewery_by_state(self, state, state_url):
        """
        Тест проверяет по выбранному штату
        """
        response_brewery_state = requests.get(state_url).json()
        if state in response_brewery_state[0]['state']:
            assert f'State: {state}'
        elif state not in response_brewery_state[0]['state']:
            assert f'State: {state}'
        else:
            assert False, 'Something wrong'

    @pytest.mark.parametrize('name', [
        "Trim Tab Brewing", "Yellowhammer Brewery", "Mudshark Brewing Co"])
    def test_brewery_by_name(self, name):
        """
        Тест проверяет по выбранному имени пивоварни
        """
        response_brewery_name = requests.get(breweries_url).json()
        if name in response_brewery_name[0]['name']:
            assert f'Name: {name}'
        elif name not in response_brewery_name[0]['name']:
            assert f'Name: {name}'
        else:
            assert False, 'Something wrong'

    @pytest.mark.parametrize('city', [
        "Tucson", "Lake Havasu City", "Chandler", "Phoenix", "Paragould"])
    def test_brewery_by_city(self, city):
        """
        Тест проверяет по выбранному городу
        """
        response_brewery_name = requests.get(breweries_url).json()
        if city in response_brewery_name[0]['city']:
            assert f'Name: {city}'
        elif city not in response_brewery_name[0]['city']:
            assert f'Name: {city}'
        else:
            assert False, 'Something wrong'

    @pytest.mark.parametrize('tag', ["Patio"])
    def test_brewery_by_tag(self, tag):
        """
        Тест проверяет по выбранному тегу
        """
        response_brewery_name = requests.get(breweries_url).json()
        if tag in response_brewery_name[0]['tag_list']:
            assert f'Name: {tag}'
        elif tag not in response_brewery_name[0]['tag_list']:
            assert f'Name: {tag}'
        else:
            assert False, 'Something wrong'
