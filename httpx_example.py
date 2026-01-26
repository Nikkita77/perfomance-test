from pprint import pprint

import httpx

# response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
# print(response)
# print(response.json())
#
# data = {
#     "title": "Новая задача",
#     "completed": False,
#     "userId": 1
# }
# response = httpx.post("https://jsonplaceholder.typicode.com/todos")
#
# print(response.status_code)
# print(response.json())
#
# """Передача токена в хедерах"""
# headers = {"Authorization": "Bearer my_secret_token"}
# response = httpx.get("https://httpbin.org/get", headers=headers)
#
# print(response.status_code)
# print(response.request.headers)
# print(response.headers)
#
# """Передача query параметров в  урле"""
# params = {"userId": 1}
# response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
#
# print(response.status_code)
# pprint(response.json())

# """Передача файла с его преобразованием в текст"""
#
#
# files = {"file": ("example.txt", open("example.txt", "rb"))}
# response = httpx.post("https://httpbin.org/post", files=files)
#
# print(response.json())  # Ответ с данными о загруженном файле

client = httpx.Client(
    base_url="https://jsonplaceholder.typicode.com",
    headers={"Authorization": "Bearer my secret_token"}

)
response1 = client.get("/todos/1")
response2 = client.get("todos/2")

print(response1.status_code)
print(response1.json())  # Данные первой задачи
print(response2.status_code)
print(response2.json())  # Данные второй задачи