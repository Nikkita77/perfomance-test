import logging

from clients.http.gateway.users.client import build_users_gateway_http_client

users_gateway_client = build_users_gateway_http_client()

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

create_user_response = users_gateway_client.create_user()
logger.info('Create user data:', create_user_response)

# Используем атрибуты вместо ключей
get_user_response = users_gateway_client.get_user(create_user_response.user.id)
logger.info('Get user data:', get_user_response)