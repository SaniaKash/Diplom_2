import allure
from data import Data, DataResponse, DataOrder
from methods.order import Order
from conftest import create_user


class TestGetOrderUser:

    @allure.title('Проверка успешного получения списка заказов конкретного пользователя, который зарегистрирован')
    def test_get_order_user_with_login(self, create_user):
        order = Order()
        response = order.get_order_real_user(create_user[2], DataOrder.WITHOUT_INGREDIENTS_BODY)
        assert response.json()['success']
        assert response.json()['orders'] == []
        assert response.status_code == 200

    @allure.title('Проверка неполучения списка заказов конкретного пользователя, который не зарегистрирован')
    def test_get_order_user_without_login(self):
        order = Order()
        response = order.get_order_real_user(Data.UPDATE_HEADERS_WITHOUT_AUTH, DataOrder.WITHOUT_INGREDIENTS_BODY)
        assert response.json() == DataResponse.RESPONSE_TEXT_UPDATE_USER_DATA_WITHOUT_LOGIN
        assert response.status_code == 401