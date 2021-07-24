import requests

# 1. Делает http-запрос любого типа без параметра method.

response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print("1st")
print(response.text)
print()

# 2. Делает http-запрос не из списка. Например, HEAD.

method = {"method": "HEAD"}
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
print("2nd")
print(response.text)
print()

# 3. Делает запрос с правильным значением method.

method = {"method": "GET"}
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=method)
print("3rd")
print(response.text)

method = {"method": "POST"}
response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
print(response.text)

method = {"method": "PUT"}
response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
print(response.text)

method = {"method": "DELETE"}
response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
print(response.text)
print()

# 4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
method = {}
methods = ["GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS"]
print("4th")
for value in methods:
    method["method"] = value
    print(method)

    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=method)
    print('get ' + response.text)

    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
    print('post ' + response.text)

    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
    print('put ' + response.text)

    response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
    print('head ' + response.text)

    response = requests.patch("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
    print('patch ' + response.text)

    response = requests.options("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
    print('options ' + response.text)

    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
    print('delete ' + response.text)

    print()
    method = {}
