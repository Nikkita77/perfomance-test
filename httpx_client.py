import time
import httpx

# Инициализируем клиент
client = httpx.Client()

payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

# Выполняем POST-запрос, используя клиент
response = client.post("http://localhost:8003/api/v1/users", json=payload)

# Выводим ответ в консоль
print(response.text)

