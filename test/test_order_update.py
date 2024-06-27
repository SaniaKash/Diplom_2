import allure
from methods.user import User
from data import Data, DataOrder, OrderResponse
from methods.order import Order


class TestCreateOrder:

    @allure.title('Проверка успешного создания заказа с указание реальных ингредиентов '
                  'в теле запроса без регистрации пользователя')
    def test_create_order_without_auth_success(self):
        order = Order()
        response = order.create_order(Data.UPDATE_HEADERS_WITHOUT_AUTH, DataOrder.REAL_BURGER_BODY)
        assert response.status_code == 200
        assert response.json()['success']
        assert response.json()['name'] == "Бессмертный флюоресцентный бургер"
        assert response.json()['order']

    @allure.title('Проверка успешного создания заказа с указание реальных ингредиентов '
                  'в теле запроса зарегистрированного пользователя')
    def test_create_order_with_auth_success(self):
        order = Order()
        headers = {'Authorization': User().create_user(Data.CREATE_USER_BODY).json()['accessToken']}
        response = order.create_order(headers, DataOrder.REAL_BURGER_BODY)
        assert response.status_code == 200
        assert response.json()['success']
        assert response.json()['name'] == "Бессмертный флюоресцентный бургер"
        assert response.json()['order']
        User().delete_user(headers)

    @allure.title('Проверка неуспешного создания заказа с указание неверных хэш ингредиентов в теле запроса ')
    def test_create_order_with_wrong_hash_failed(self):
        order = Order()
        response = order.create_order(Data.UPDATE_HEADERS_WITHOUT_AUTH, DataOrder.WRONG_INGREDIENTS_HASH_BODY)
        assert response.status_code == 500

    @allure.title('Проверка неуспешного создания заказа без указания ингредиентов в теле запроса ')
    def test_create_order_without_ingredient_failed(self):
        order = Order()
        response = order.create_order(Data.UPDATE_HEADERS_WITHOUT_AUTH, DataOrder.WITHOUT_INGREDIENTS_BODY)
        print(response.text)
        assert response.status_code == 400
        assert response.json() == OrderResponse.RESPONSE_TEXT_ORDER_WITHOUT_INGREDIENTS


