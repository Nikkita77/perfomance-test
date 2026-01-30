
from clients.http.gateway.accounts.client import build_accounts_gateway_http_client
from clients.http.gateway.documents.client import build_documents_gateway_http_client
from clients.http.gateway.users.client import build_users_gateway_http_client


users_client = build_users_gateway_http_client()
accounts_client = build_accounts_gateway_http_client()
documents_client = build_documents_gateway_http_client()

    # 1) Create user
create_user_response = users_client.create_user()
print("Create user response: %s", create_user_response)

user_id = create_user_response["user"]["id"]

    # 2) Open credit card account
open_credit_card_account_response = accounts_client.open_credit_card_account(user_id)
print("Open credit card account response: %s", open_credit_card_account_response)

account_id = open_credit_card_account_response["account"]["id"]

    # 3) Get tariff document
tariff_doc_response = documents_client.get_tariff_document(account_id)
print("Get tariff document response: %s", tariff_doc_response)

    # 4) Get contract document
contract_doc_response = documents_client.get_contract_document(account_id)
print("Get contract document response: %s", contract_doc_response)