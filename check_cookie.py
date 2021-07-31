import requests

response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
cookie_in_the_response = dict(response.cookies)
print(cookie_in_the_response)
for key, value in cookie_in_the_response.items():
    cookie_name = key
    cookie_value = value

class TestCheckCookie:
    def test_check_cookie_name(self):
        assert cookie_name == 'HomeWork', f"Cookie name is not 'HomeWork', but '{cookie_name}'"

    def test_check_cookie_value(self):
        assert cookie_value == 'hw_value', f"Cookie value is not 'hw_value', but '{cookie_value}'"
