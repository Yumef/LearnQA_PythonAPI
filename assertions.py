from requests import Response
import json

class Assertions:
    # сделать метод статическим, т.к. Assertions не является прямым наследником для тестов
    # то есть эти методы сами должны принять на вход значения и проверить их
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

