import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

count_url = 0
while response.history[count_url].url != "https://learnqa.ru/":
    count_url += 1

print(count_url)
print(response.url)