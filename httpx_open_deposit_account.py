import httpx
import time

# 1. Создание пользователя
create_user_payload = {
    "email": f"user{int(time.time())}@example.com",
    "lastName": "Ivanov",
    "firstName": "Ivan",
    "middleName": "Ivanovich",
    "phoneNumber": "79999999999"
}

create_user_response = httpx.post(
    "http://localhost:8003/api/v1/users",
    json=create_user_payload
)

print("Create user status:", create_user_response.status_code)
create_user_data = create_user_response.json()
print("Create user response:", create_user_data)

# Проверка наличия user.id
user_id = create_user_data["user"]["id"]

# 2. Открытие депозитного счёта
open_deposit_account_payload = {
    "userId": user_id
}

open_deposit_account_response = httpx.post(
    "http://localhost:8003/api/v1/accounts/open-deposit-account",
    json=open_deposit_account_payload
)

# 3. Вывод результата
print("Deposit account status:", open_deposit_account_response.status_code)
print("Deposit account response:", open_deposit_account_response.json())
