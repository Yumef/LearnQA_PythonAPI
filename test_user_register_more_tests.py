from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import pytest

class TestUserRegister(BaseCase):

    exclude_params = [
        ('no_email'),
        ('no_password'),
        ('no_username'),
        ('no_firstName'),
        ('no_lastName')
    ]

    # позитивный тест
    def test_create_user_successfully(self):
        data = self.prepare_registrations_data()  # не передается email

        response = MyRequests.post("/user/", data=data)
        # проверка, что с email выдает код 200
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    # негативный тест
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registrations_data(email)   # передается email

        response = MyRequests.post("/user/", data=data)
        # проверка, что с сущ. email выдает код 400
        # иначе ошибка, что код другой и следующий асерт не проверяется
        Assertions.assert_code_status(response, 400)
        # если 400, проверка текста ошибки
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    def test_create_user_with_incorrect_email_without_at(self):
        data = self.prepare_registrations_incorrect_email_without_at()
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "Invalid email format"


    @pytest.mark.parametrize('condition', exclude_params)
    def test_create_user_without_params(self, condition):
        if condition == "no_email":
            data = self.prepare_registrations_without_params(param_exclude='email')
            response = MyRequests.post("/user/", data=data)
            Assertions.assert_code_status(response, 400)
            assert response.content.decode("utf-8") == "The following required params are missed: email"
        elif condition == "no_password":
            data = self.prepare_registrations_without_params(param_exclude='password')
            response = MyRequests.post("/user/", data=data)
            Assertions.assert_code_status(response, 400)
            assert response.content.decode("utf-8") == "The following required params are missed: password"
        elif condition == "no_username":
            data = self.prepare_registrations_without_params(param_exclude='username')
            response = MyRequests.post("/user/", data=data)
            Assertions.assert_code_status(response, 400)
            assert response.content.decode("utf-8") == "The following required params are missed: username"
        elif condition == "no_firstName":
            data = self.prepare_registrations_without_params(param_exclude='firstName')
            response = MyRequests.post("/user/", data=data)
            Assertions.assert_code_status(response, 400)
            assert response.content.decode("utf-8") == "The following required params are missed: firstName"
        elif condition == "no_lastName":
            data = self.prepare_registrations_without_params(param_exclude='lastName')
            response = MyRequests.post("/user/", data=data)
            Assertions.assert_code_status(response, 400)
            assert response.content.decode("utf-8") == "The following required params are missed: lastName"


    def test_create_user_with_short_name(self):
        data = self.prepare_registrations_with_short_name()
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "The value of 'firstName' field is too short"

    def test_create_user_with_long_name(self):
        data = self.prepare_registrations_with_long_name()
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "The value of 'firstName' field is too long"