import logging

from clients.http.gateway.users.client import build_users_gateway_http_client
from clients.http.gateway.accounts.client import build_accounts_gateway_http_client
from clients.http.gateway.operations.client import build_operations_gateway_http_client


logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


def main() -> None:
    users_client = build_users_gateway_http_client()
    accounts_client = build_accounts_gateway_http_client()
    operations_client = build_operations_gateway_http_client()

    # 1) Create user
    create_user_response = users_client.create_user()
    logger.info("Create user response: %s", create_user_response)

    user_id = create_user_response["user"]["id"]

    # 2) Open debit card account
    open_debit_account_response = accounts_client.open_debit_card_account(user_id)
    logger.info("Open debit card account response: %s", open_debit_account_response)

    account_id = open_debit_account_response["account"]["id"]
    card_id = open_debit_account_response["account"]["cards"][0]["id"]  # берем первую карту

    # 3) Make top up operation
    make_top_up_response = operations_client.make_top_up_operation(card_id=card_id, account_id=account_id)
    logger.info("Make top up operation response: %s", make_top_up_response)


if __name__ == "__main__":
    main()
