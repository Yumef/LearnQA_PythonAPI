import json.decoder
from requests import Response
from datetime import datetime

class BaseCase:
    # функция, которая определяет, есть ли куки в ответе и возвращает их:
    def get_cookies(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Cannot find cookies with name {cookie_name} in the last response"
        return response.cookies[cookie_name]

    # функция, которая определяет, есть ли хэдер в ответе и возвращает его:
    def get_header(self, response: Response, header_name):
        assert header_name in response.headers, f"Cannot find header with name {header_name} in the last response"
        return response.headers[header_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}"
        # если парсинг успешный:
        assert name in response_as_dict, f"resonse JSON doesn`t have key '{name}"
        return response_as_dict[name]

    def prepare_registrations_data(self, email=None):
        if email is None:    # если email передать (не None), то генерироваться (логика ниже) он не будет
            base_part = "learnqa"
            domain = "example.com"
            random_part = datetime.now().strftime(
                "%m%d%Y%H%M%S")  # на основе сегодняшней даты, чтобы тесты, запущенные в разное время не создали повторяющиеся данные
            email = f"{base_part}{random_part}@{domain}"
        return {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }
