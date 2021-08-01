import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

history = response.history
len_history = len(history)
for i in history:
    print(i.url)

print(len_history)