import allure
import requests
from data import Data
import json


class Order:
    # Ручка для создания заказа/ получения данных о заказе конкретного пользователя
    ORDER_ENDPOINT = '/api/orders'


    @allure.step('Метод запроса POST для создания заказа')
    def create_order(self, auth_data, ingredients):
        response = requests.post(f'{Data.URL}{self.ORDER_ENDPOINT}', headers=auth_data, json=ingredients)
        return response

    @allure.step('Метод запроса GET для получения списка заказов конкретного пользователя')
    def get_order_real_user(self, auth_data, ingredients):
        response = requests.get(f'{Data.URL}{self.ORDER_ENDPOINT}', headers=auth_data, json=ingredients)
        return response
