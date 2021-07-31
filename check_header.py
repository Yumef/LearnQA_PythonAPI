import requests

response = requests.get("https://playground.learnqa.ru/api/homework_header")
header_in_the_response = dict(response.headers)
print(header_in_the_response)
header_name = 'x-secret-homework-header'

class TestCheckHeader:
    def test_check_header_name(self):
        assert header_name in header_in_the_response, f"Header name '{header_name}' is not in Response'"

    def test_check_header_value(self):
        assert header_in_the_response.get(header_name) == 'Some secret value', f"Header value is not 'Some secret value' but '{header_in_the_response.get(header_name)}'"
