import allure
import requests
from data import Data
import json


class User:

    # Ручка для создания пользователя
    CREATE_USER_ENDPOINT = '/api/auth/register'
    # Ручка для регистрации пользователя
    LOGIN_USER_ENDPOINT = '/api/auth/login'
    # Ручка для обновления данных пользователя
    UPDATE_USER_DATA_ENDPOINT = '/api/auth/user'
    # Ручка удаления пользователя
    DELETE_USER = '/api/auth/user'

    @allure.step('Метод запроса POST для создания пользователя')
    def create_user(self, data):
        response = requests.post(f'{Data.URL}{self.CREATE_USER_ENDPOINT}', json=data)
        return response

    @allure.step('Метод запроса POST для регистрации пользователя')
    def login_user(self, data_login):
        response = requests.post(f'{Data.URL}{self.LOGIN_USER_ENDPOINT}', json=data_login)
        return response

    @allure.step('Метод запроса PATCH для обновлении данных пользователя')
    def update_user_data(self, data_update, update_user_data):
        response = requests.patch(f'{Data.URL}{self.UPDATE_USER_DATA_ENDPOINT}',
                                  headers=data_update, json=update_user_data)
        return response

    @allure.step('Метод запроса DELETE для удаления пользователя')
    def delete_user(self, data):
        response = requests.delete(f'{Data.URL}{self.DELETE_USER}', headers=data)
        return response




