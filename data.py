from helpers import login, password, email


class Data:
    URL = 'https://stellarburgers.nomoreparties.site'
    CREATE_USER_BODY = {"email": f"{email()}",
                        "password": f"{password()}",
                        "name": f"{login()}"}
    LOGIN_USER_BODY = {"email": CREATE_USER_BODY["email"],"password": CREATE_USER_BODY["password"]}
    LOGIN_USER_BODY_WRONG_LOGIN = {"email": f'{CREATE_USER_BODY["email"]}abc',
                                   "password": CREATE_USER_BODY["password"]}

    LOGIN_USER_BODY_WRONG_PASSWORD = {"email": f'{CREATE_USER_BODY["email"]}',
                                      "password": f'{CREATE_USER_BODY["password"]}123'}
    CREATE_USER_BODY_WITHOUT_NAME = {"email": f"{email()}", "password": f"{password()}"}
    CREATE_USER_BODY_WITHOUT_EMAIL = {"password": f"{password()}", "name": f"{login()}"}
    CREATE_USER_BODY_WITHOUT_PASSWORD = {"email": f"{email()}", "name": f"{login()}"}
    UPDATE_USER_DATA_EMAIL = {"email": f"abc{email()}"}
    UPDATE_USER_DATA_NAME = {"name": f"BCA{login()}"}
    UPDATE_HEADERS_WITHOUT_AUTH = {'Authorization': ''}
    UPDATE_USER_DATA_WITHOUT_LOGIN = {"email": f"abccc{email()}", "name": f"BCAaaa{login()}"}


class DataOrder:
    REAL_BURGER_BODY = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}
    WITHOUT_INGREDIENTS_BODY = {"ingredients": ''}
    WRONG_INGREDIENTS_HASH_BODY = {"ingredients": ["12345678910", "10987654321"]}


class OrderResponse:
    RESPONSE_TEXT_ORDER_WITHOUT_INGREDIENTS = {"success": False, "message": "Ingredient ids must be provided"}


class DataResponse(Data):
    RESPONSE_TEXT_CREATE_USER = {"email": Data.CREATE_USER_BODY["email"], "name": Data.CREATE_USER_BODY["name"]}
    RESPONSE_TEXT_CREATE_SAME_USER = {"success": False, "message": "User already exists"}
    RESPONSE_TEXT_CREATE_USER_WITHOUT_FIELD = {"success": False,
                                               "message": "Email, password and name are required fields"}
    RESPONSE_TEXT_LOGIN_USER_WRONG_LOGIN_OR_PASSWORD = {"success": False, "message": "email or password are incorrect"}

    RESPONSE_TEXT_UPDATE_USER_DATA_WITH_LOGIN_EMAIL = {"success": True, "user":
                                {"email": Data.UPDATE_USER_DATA_EMAIL['email'], "name": Data.CREATE_USER_BODY['name']}}
    RESPONSE_TEXT_UPDATE_USER_DATA_WITH_LOGIN_NAME = {"success": True, "user":
                                {"email": Data.CREATE_USER_BODY['email'], "name": Data.UPDATE_USER_DATA_NAME['name']}}
    RESPONSE_TEXT_UPDATE_USER_DATA_WITHOUT_LOGIN = {"success": False, "message": "You should be authorised"}