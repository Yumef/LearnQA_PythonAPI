from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserEdit(BaseCase):

    def setup(self):
        # REGISTER
        register_data = self.prepare_registrations_data()
        response1 = MyRequests.post("/user/", data=register_data)
        # проверка на то, что пришел код 200 и id нового пользователя
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")
        # разложить данные пользователя по переменным
        self.email = register_data['email']
        self.first_name = register_data['firstName']
        self.password = register_data['password']
        self.user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': self.email,
            'password': self.password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        self.auth_sid = self.get_cookies(response2, "auth_sid")
        self.token = self.get_header(response2, "x-csrf-token")


    # позитивный тест - редактирование авторизованным пользователем самого себя
    def test_edit_just_created_user(self):
        # EDIT
        new_name = 'Changed Name'

        response3 = MyRequests.put(
            f"/user/{self.user_id}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid},
            data={'firstName': new_name}
        )
        # проверить, что редактирование успешное
        Assertions.assert_code_status(response3, 200)

        # GET - проверить, что новые данные соответствуют введенным
        response4 = MyRequests.get(
            f"/user/{self.user_id}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )
        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of the user after edit"
        )


    # негативный тест - редактирование неавторизованным пользователем
    def test_edit_not_auth(self):
        # EDIT
        new_name = 'Changed Name 2'
        response5 = MyRequests.put(f"/user/1", data={'firstName': new_name})
        # проверить, что редактирование неуспешное
        Assertions.assert_code_status(response5, 400)
        assert response5.content.decode("utf-8") == "Auth token not supplied"


    # негативный тест - редактирование другим пользователем
    def test_edit_other_user(self):
        # EDIT
        new_name = 'Changed Name 4'
        print(self.user_id)
        other_user_id = int(self.user_id) - 1
        print(other_user_id)

        response6 = MyRequests.put(
            f"/user/{other_user_id}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid},
            data={'firstName': new_name}
        )
        # проверить, что редактирование неуспешное
        Assertions.assert_code_status(response6, 400)
        assert response6.content.decode("utf-8") == "Error message"

        # проверить, что пользователь не отредактировался
        response6_2 = MyRequests.get(
            f"/user/{self.user_id}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
            )
        response6_3 = self.get_json_value(response6_2, 'firstName')
        print(response6_3)
        assert response6_3 != new_name, "First Name and New Name are the same"


    # негативный тест - редактирование авторизованным пользователем самого себя с невалидным email
    def test_edit_with_invalid_email(self):
        # EDIT
        new_email = 'ChangedEmailexample.com'
        response7 = MyRequests.put(
            f"/user/{self.user_id}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid},
            data={'email': new_email}
        )
        # проверить, что редактирование неуспешное
        Assertions.assert_code_status(response7, 400)
        assert response7.content.decode("utf-8") == "Invalid email format"

        # проверить, что пользователь не отредактировался
        response7_2 = MyRequests.get(
            f"/user/{self.user_id}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )
        response7_3 = self.get_json_value(response7_2, 'email')
        print(response7_3)
        assert response7_3 != new_email, "Email and New Email are the same"


    # негативный тест - редактирование авторизованным пользователем самого себя с невалидным firstName
    def test_edit_with_invalid_firstName(self):
        # EDIT
        new_firstName = 'N'
        response8 = MyRequests.put(
            f"/user/{self.user_id}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid},
            data={'firstName': new_firstName}
        )
        # проверить, что редактирование неуспешное
        Assertions.assert_code_status(response8, 400)
        assert response8.content.decode("utf-8") == "Too short value for field firstName"

        # проверить, что пользователь не отредактировался
        response8_2 = MyRequests.get(
            f"/user/{self.user_id}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )
        response8_3 = self.get_json_value(response8_2, 'firstName')
        print(response8_3)
        assert response8_3 != new_firstName, "First Name and New Name are the same"
