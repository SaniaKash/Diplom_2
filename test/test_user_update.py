import allure
from methods.user import User
import pytest
from data import Data, DataResponse


class TestUpdateUserData:

    @allure.title('Проверка успешного изменения данных для авторизованного пользователя')
    @allure.description('Проводится поочередная проверка измененных полей имейл и логин пользователя')
    @pytest.mark.parametrize('data_input, data_response',
                             [[Data.UPDATE_USER_DATA_EMAIL, DataResponse.RESPONSE_TEXT_UPDATE_USER_DATA_WITH_LOGIN_EMAIL],
                             [Data.UPDATE_USER_DATA_NAME, DataResponse.RESPONSE_TEXT_UPDATE_USER_DATA_WITH_LOGIN_NAME]])
    def test_update_user_data_with_login_or_email_user_success(self, data_input, data_response):
        user = User()
        headers = {'Authorization': user.create_user(Data.CREATE_USER_BODY).json()['accessToken']}
        response = user.update_user_data(headers, data_input)
        assert response.status_code == 200
        assert response.json() == data_response
        user.delete_user(headers)

    @allure.title('Проверка неуспешного изменения данных для неавторизованного пользователя')
    @allure.description('Проводится поочередная проверка измененных полей имейл и логин пользователя')
    @pytest.mark.parametrize('data_input', (Data.UPDATE_USER_DATA_EMAIL, Data.UPDATE_USER_DATA_NAME))
    def test_update_user_data_without_login_user_failed(self, data_input):
        user = User()
        response = user.update_user_data(Data.UPDATE_HEADERS_WITHOUT_AUTH, data_input)
        assert response.status_code == 401
        assert response.json() == DataResponse.RESPONSE_TEXT_UPDATE_USER_DATA_WITHOUT_LOGIN
