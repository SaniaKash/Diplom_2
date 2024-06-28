import random
from faker import Faker

fake = Faker()


def login():
    login_user = fake.name()
    return login_user


def password():
    password_user = random.randrange(100000, 999999)
    return password_user


def email():
    email_user = fake.email()
    return email_user


def data_user():
    data = {"email": f'{email()}',
            "password": f'{password()}',
            "name": f'{login()}'}
    return data
