import time
import httpx

# Шаг 1: создаём пользователя
create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

print("Create user response:", create_user_response_data)
print("Status code:", create_user_response.status_code)

# Шаг 2: Создаем кредитный счёт для пользователя

open_credit_card_account_payload = {
"userId": create_user_response_data["user"]["id"]
}
open_credit_card_account_payload_response = httpx.post('http://localhost:8003/api/v1/accounts/open-credit-card-account', json=open_credit_card_account_payload)
open_credit_card_account_payload_data = open_credit_card_account_payload_response.json()
account_id_data = open_credit_card_account_payload_data["account"]["id"]
card_id_data = open_credit_card_account_payload_data["account"]["cards"][0]["id"]
print(account_id_data)
print(card_id_data)
print(open_credit_card_account_payload_response.status_code)
print(open_credit_card_account_payload_data)

# Шаг 3: Совершаем операцию покупки (purchase)
make_purchase_operation_payload = {
  "status": "IN_PROGRESS",
  "amount": 77.99,
  "cardId": card_id_data,
  "accountId": account_id_data,
  "category": "taxi"
}

make_purchase_operation_response = httpx.post("http://localhost:8003/api/v1/operations/make-purchase-operation", json=make_purchase_operation_payload)
make_purchase_operation_data = make_purchase_operation_response.json()
operation_id_data = make_purchase_operation_data["operation"]["id"]

print(make_purchase_operation_response.status_code)
print(make_purchase_operation_data)
print(operation_id_data)

# Шаг 4 Получаем чек по операции
get_operation_receipt_response = httpx.get(f"http://localhost:8003/api/v1/operations/operation-receipt/{operation_id_data}")
get_operation_receipt_data = get_operation_receipt_response.json()
print(get_operation_receipt_data)
print(get_operation_receipt_response.status_code)