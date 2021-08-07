from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserDelete(BaseCase):
    # авторизация пользователя, который не будет удален
    def setup(self):
        # AUTH
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post("/user/login", data=data)

        self.auth_sid = self.get_cookies(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id = self.get_json_value(response1, "user_id")

    # негативный тест - удаление неудаляемого юзера
    def test_delete_base_user(self):
        response2 = MyRequests.delete(
            f"/user/{self.user_id}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )
        response3 = MyRequests.get(f"/user/{self.user_id}")
        # проверка на то, что нельзя удалить
        Assertions.assert_code_status(response2, 400)
        assert response2.content.decode("utf-8") == "Please, do not delete test users with ID 1, 2, 3, 4 or 5."
        # проверка на то, что пользователь есть
        Assertions.assert_code_status(response3, 200)

    # позитивный тест - удаление нового юзера
    def test_delete_new_user(self):
        # REGISTER
        email = 'email01010101@example.com'
        data = self.prepare_registrations_data(email=email)

        response4 = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response4, 200)
        user_id = self.get_json_value(response4, 'id')

        auth_data = {
            'email': email,
            'password': '123'
        }
        # LOGIN
        response5 = MyRequests.post("/user/login", data=auth_data)
        auth_sid = self.get_cookies(response5, "auth_sid")
        token = self.get_header(response5, "x-csrf-token")

        # DELETE
        response6 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        response7 = MyRequests.get(f"/user/{user_id}")
        # проверка на то, что можно удалить
        Assertions.assert_code_status(response6, 200)
        # проверка на то, что пользователя нет
        Assertions.assert_code_status(response7, 404)
        assert response7.content.decode("utf-8") == "User not found"

    # негативный тест - удаление юзера с другим id
    def test_delete_other_user(self):
        # REGISTER
        data = self.prepare_registrations_data()

        response8 = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response8, 200)
        user_id = self.get_json_value(response8, "id")
        print(user_id)

        # DELETE
        response9 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )
        response10 = MyRequests.get(f"/user/{user_id}")
        # проверка на то, что нельзя удалить
        Assertions.assert_code_status(response9, 400)
        assert response9.content.decode("utf-8") == "Видимо, здесь должна быть другая ошибка"
        # проверка на то, что пользователь есть
        Assertions.assert_code_status(response10, 200)