import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

first_response = response.history[0]
count_url = 0
for i in response:
    count_url += 1

print(count_url)
print(response.url)