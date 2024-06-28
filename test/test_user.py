import allure
from methods.user import User
import pytest
from data import Data, DataResponse
from conftest import create_user


class TestCreateUser:
    @allure.title('Проверка успешного создания уникального пользователя')
    def test_create_new_user_success(self, create_user):
        response = create_user
        assert response[0].status_code == 200
        assert response[0].json()['success'] is True
        assert response[0].json()['accessToken']
        assert response[0].json()['refreshToken']

    @allure.title('Проверка неуспешного создания пользователя , который уже зарегистрирован')
    def test_create_user_who_is_already_registered_failed(self, create_user):
        user = User()
        response_new_user = user.create_user(create_user[1])
        assert response_new_user.status_code == 403
        assert response_new_user.json() == DataResponse.RESPONSE_TEXT_CREATE_SAME_USER

    @allure.title('Проверка неуспешного создания пользователя , '
                  'при отсутствии одного из обязательных полей в теле запроса')
    @pytest.mark.parametrize('data', (Data.CREATE_USER_BODY_WITHOUT_EMAIL, Data.CREATE_USER_BODY_WITHOUT_NAME,
                                      Data.CREATE_USER_BODY_WITHOUT_PASSWORD))
    def test_create_user_without_one_field_failed(self, data):
        user = User()
        response = user.create_user(data)
        assert response.status_code == 403
        assert response.json() == DataResponse.RESPONSE_TEXT_CREATE_USER_WITHOUT_FIELD


class TestLoginUser:

    @allure.title('Проверка успешной авторизации пользователя')
    def test_login_user_with_created_user_success(self, create_user):
        user = User()
        response_login = user.login_user(create_user[1])
        assert response_login.status_code == 200
        assert response_login.json()['success'] is True
        assert response_login.json()['accessToken']
        assert response_login.json()['refreshToken']


    @allure.title('Проверка неуспешной авторизации пользователя при неверном заполнении имени и пароля в теле запроса')
    def test_login_user_with_wrong_login_or_password_failed(self, create_user):
        user = User()
        response_login = user.login_user(Data.LOGIN_USER_BODY_WRONG_PASSWORD_NAME)
        print(response_login)
        assert response_login.status_code == 401
        assert response_login.json() == DataResponse.RESPONSE_TEXT_LOGIN_USER_WRONG_LOGIN_OR_PASSWORD






