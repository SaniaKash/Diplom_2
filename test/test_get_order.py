import allure
from methods.user import User
from data import Data, DataResponse, DataOrder
from methods.order import Order


class TestGetOrderUser:

    @allure.title('Проверка успешного получения списка заказов конкретного пользователя, который зарегистрирован')
    def test_get_order_user_with_login(self):
        order = Order()
        headers = {'Authorization': User().create_user(Data.CREATE_USER_BODY).json()['accessToken']}
        response = order.get_order_real_user(headers, DataOrder.WITHOUT_INGREDIENTS_BODY)
        assert response.json()['success']
        assert response.json()['orders'] == []
        assert response.status_code == 200
        User().delete_user(headers)

    @allure.title('Проверка неполучения списка заказов конкретного пользователя, который не зарегистрирован')
    def test_get_order_user_without_login(self):
        order = Order()
        response = order.get_order_real_user(Data.UPDATE_HEADERS_WITHOUT_AUTH, DataOrder.WITHOUT_INGREDIENTS_BODY)
        assert response.json() == DataResponse.RESPONSE_TEXT_UPDATE_USER_DATA_WITHOUT_LOGIN
        assert response.status_code == 401