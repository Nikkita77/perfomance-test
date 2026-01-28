from typing import TypedDict

import httpx

from clients.http.client import HTTPClient


class IssueVirtualCardRequestDict(TypedDict):
    """Тело запроса для выпуска виртуальной карты."""
    userId: str
    accountId: str


class IssuePhysicalCardRequestDict(TypedDict):
    """Тело запроса для выпуска физической карты."""
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HTTPClient):
    """
    HTTP-клиент для работы с эндпоинтами /api/v1/cards сервиса http-gateway.

    Содержит методы для выпуска виртуальных и физических карт.
    """

    def issue_virtual_card_api(self, request: IssueVirtualCardRequestDict) -> httpx.Response:
        """
        Выпускает виртуальную карту.

        Отправляет POST-запрос на эндпоинт:
        /api/v1/cards/issue-virtual-card

        Args:
            request: Данные для выпуска виртуальной карты.
                Формат:
                {
                    "userId": "<str>",
                    "accountId": "<str>"
                }

        Returns:
            httpx.Response: HTTP-ответ сервиса http-gateway.
        """
        return self.post("/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: IssuePhysicalCardRequestDict) -> httpx.Response:
        """
        Выпускает физическую карту.

        Отправляет POST-запрос на эндпоинт:
        /api/v1/cards/issue-physical-card

        Args:
            request: Данные для выпуска физической карты.
                Формат:
                {
                    "userId": "<str>",
                    "accountId": "<str>"
                }

        Returns:
            httpx.Response: HTTP-ответ сервиса http-gateway.
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)