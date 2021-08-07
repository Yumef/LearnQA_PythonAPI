from requests import Response
import json

class Assertions:
    # сделать метод статическим, т.к. Assertions не является прямым наследником для тестов
    @staticmethod
    # создать функцию, в которой убедиться, что значение внутри json доступно по определенному имени и равно ожидаемому
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}"
        # если парсинг успешный:
        assert name in response_as_dict, f"Resonse JSON doesn`t have key '{name}"
        assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}"
        # если парсинг успешный:
        assert name in response_as_dict, f"Resonse JSON doesn`t have key '{name}"

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}"
        # если парсинг успешный:
        for name in names:
            assert name in response_as_dict, f"Resonse JSON doesn`t have key '{name}"

    @staticmethod
    def assert_json_has_not_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}. But it`s present"
        # если парсинг успешный:
        assert name not in response_as_dict, f"Resonse JSON shoudn`t have key '{name}"

    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f"Unexpected status code! Expected: {expected_status_code}. Actual: {response.status_code}"




