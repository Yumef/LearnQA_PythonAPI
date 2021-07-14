import requests

r = requests.get('https://playground.learnqa.ru/api/get_text')
print(r.text)