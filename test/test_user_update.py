import allure
from methods.user import User
import pytest
from data import Data, DataResponse
from conftest import create_user


class TestUpdateUserData:

    @allure.title('Проверка успешного изменения данных для авторизованного пользователя')
    @allure.description('Проводится поочередная проверка измененных полей имейл и логин пользователя')
    @pytest.mark.parametrize('data_input',
                             [Data.UPDATE_USER_DATA_EMAIL, Data.UPDATE_USER_DATA_NAME, ])
    def test_update_user_data_with_login_or_email_user_success(self, create_user, data_input, ):
        user = User()
        response = user.update_user_data(create_user[2], data_input)
        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Проверка неуспешного изменения данных для неавторизованного пользователя')
    @allure.description('Проводится поочередная проверка измененных полей имейл и логин пользователя')
    @pytest.mark.parametrize('data_input', (Data.UPDATE_USER_DATA_EMAIL, Data.UPDATE_USER_DATA_NAME))
    def test_update_user_data_without_login_user_failed(self, data_input):
        user = User()
        response = user.update_user_data(Data.UPDATE_HEADERS_WITHOUT_AUTH, data_input)
        assert response.status_code == 401
        assert response.json() == DataResponse.RESPONSE_TEXT_UPDATE_USER_DATA_WITHOUT_LOGIN
