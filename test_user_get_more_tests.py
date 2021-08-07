from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserGet(BaseCase):
    def setup(self):
        data = {
            "email": 'vinkotov@example.com',
            "password": '1234'
        }
        response1 = MyRequests.post("/user/login", data=data)
        self.auth_sid = self.get_cookies(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id = self.get_json_value(response1, "user_id")

    # тест на просомтр пользователя будучи неавторизованным
    def test_get_user_details_not_auth(self):
        response = MyRequests.get("/user/2")

        unexpected_fields = ["email", "firstName", "lastName"]

        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_keys(response, unexpected_fields)

    # тест на просмотр пользователя будучи авторизованным под тем же id
    def test_get_user_details_auth_as_same_user(self):

        response2 = MyRequests.get(
            f"/user/{self.user_id}",
        headers={"x-csrf-token": self.token},
        cookies={"auth_sid": self.auth_sid}
        )

        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response2, expected_fields)

    # тест на просмотр пользователя будучи авторизованным под другим id
    def test_get_user_details_auth_as_other_user(self):
        other_user_id = int(self.user_id) - 1

        response4 = MyRequests.get(
            f"/user/{other_user_id}",
        headers={"x-csrf-token": self.token},
        cookies={"auth_sid": self.auth_sid}
        )

        unexpected_fields = ["email", "firstName", "lastName"]

        Assertions.assert_json_has_key(response4, "username")
        Assertions.assert_json_has_not_keys(response4, unexpected_fields)