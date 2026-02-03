import logging

from clients.http.gateway.users.client import build_users_gateway_http_client
from clients.http.gateway.accounts.client import build_accounts_gateway_http_client
from clients.http.gateway.operations.client import build_operations_gateway_http_client

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)



users_client = build_users_gateway_http_client()
accounts_client = build_accounts_gateway_http_client()
operations_client = build_operations_gateway_http_client()

create_user = users_client.create_user()
logger.info("Create user response: %s", create_user)

user_id = create_user.user.id  # ✅ Pydantic

open_debit = accounts_client.open_debit_card_account(user_id)  # возможно dict
logger.info("Open debit card account response: %s", open_debit)

account_id = open_debit["account"]["id"]
card_id = open_debit["account"]["cards"][0]["id"]

make_top_up = operations_client.make_top_up_operation(card_id=card_id, account_id=account_id)
logger.info("Make top up operation response: %s", make_top_up.model_dump(by_alias=True))


