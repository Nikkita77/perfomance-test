import time
from typing import Any, Dict

import httpx

BASE_URL = "http://localhost:8003/api/v1"
TIMEOUT = httpx.Timeout(10.0)


def build_create_user_payload() -> Dict[str, str]:
    timestamp = time.time()
    return {
        "email": f"user{timestamp}@example.com",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string",
        "phoneNumber": "string",
    }


def create_user(client: httpx.Client) -> Dict[str, Any]:
    response = client.post(f"{BASE_URL}/users", json=build_create_user_payload())
    response.raise_for_status()
    return response.json()


def get_user(client: httpx.Client, user_id: str) -> Dict[str, Any]:
    response = client.get(f"{BASE_URL}/users/{user_id}")
    response.raise_for_status()
    return response.json()


def main() -> None:
    with httpx.Client(timeout=TIMEOUT) as client:
        create_user_response = create_user(client)
        print("Create user response:", create_user_response)

        user_id = str(create_user_response["user"]["id"])
        get_user_response = get_user(client, user_id)
        print("Get user response:", get_user_response)


if __name__ == "__main__":
    main()
