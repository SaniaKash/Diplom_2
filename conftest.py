import allure
import pytest
from helpers import data_user
from data import Data
import requests


@allure.step('Фикстура метода запроса POST для создания пользователя и последующего его удаления')
@pytest.fixture(scope='function')
def create_user():
    data = data_user()
    response = requests.post(f'{Data.URL}/api/auth/register', json=data)
    headers = {'Authorization': response.json()['accessToken']}
    yield response, data, headers
    requests.delete(f'{Data.URL}/api/auth/user', headers=headers)
