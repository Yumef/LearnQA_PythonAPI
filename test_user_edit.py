from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserEdit(BaseCase):
    # REGISTER
    # для этого в BaseCase создается функция для подготовки к созданию пользователя (уникальная почта и тд)
    # по сути выносится из test_user_register в BaseCase
    def test_edit_just_created_user(self):
        register_data = self.prepare_registrations_data()
        response1 = MyRequests.post("/user/", data=register_data)
        # проверка на то, что пришел код 200 и id нового пользователя
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")
        # разложить данные пользователя по переменным
        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookies(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        new_name = 'Changed Name'

        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={'firstName': new_name}
        )
        # проверить, что редактирование успешное
        Assertions.assert_code_status(response3, 200)

        # GET - првоерить, что новые данные соответствуют введенным
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of the user after edit"
        )