from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserRegister(BaseCase):

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

