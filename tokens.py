import requests
import time

# создавал задачу
task = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")

parsed_response_task = task.json()
seconds = parsed_response_task.get("seconds")

# делал один запрос с token ДО того, как задача готова
task2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=parsed_response_task)

# убеждался в правильности поля status
parsed_response_task2 = task2.json()
if parsed_response_task2.get("status") == "Job is NOT ready":
    print("status 'not ready'")

# ждал нужное количество секунд
time.sleep(seconds)

# делал бы один запрос c token ПОСЛЕ того, как задача готова
task3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=parsed_response_task)

# убеждался в правильности поля status и наличии поля result
parsed_response_task3 = task3.json()
if parsed_response_task3.get("status") == "Job is ready":
    print("status 'ready'")
if "result" in parsed_response_task3:
    print("result is in answer")