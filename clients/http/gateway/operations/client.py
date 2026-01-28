from __future__ import annotations

from typing import TypedDict

from httpx import QueryParams, Response

from clients.http.client import HTTPClient


class GetOperationsQueryDict(TypedDict):
    """Query-параметры для получения списка операций по счету."""
    accountId: str


class GetOperationsSummaryQueryDict(TypedDict):
    """Query-параметры для получения статистики по операциям по счету."""
    accountId: str


class MakeOperationRequestDict(TypedDict):
    """Базовая структура для создания операции."""
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeFeeOperationRequestDict(MakeOperationRequestDict):
    """Тело запроса для создания операции комиссии."""


class MakeTopUpOperationRequestDict(MakeOperationRequestDict):
    """Тело запроса для создания операции пополнения."""


class MakeCashbackOperationRequestDict(MakeOperationRequestDict):
    """Тело запроса для создания операции кэшбэка."""


class MakeTransferOperationRequestDict(MakeOperationRequestDict):
    """Тело запроса для создания операции перевода."""


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """Тело запроса для создания операции покупки."""
    category: str


class MakeBillPaymentOperationRequestDict(MakeOperationRequestDict):
    """Тело запроса для создания операции оплаты по счету."""


class MakeCashWithdrawalOperationRequestDict(MakeOperationRequestDict):
    """Тело запроса для создания операции снятия наличных."""


class OperationsGatewayHTTPClient(HTTPClient):
    """HTTP API клиент для эндпоинтов /api/v1/operations сервиса http-gateway."""

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получение информации об операции по operation_id.

        Args:
            operation_id: Идентификатор операции.

        Returns:
            httpx.Response: Ответ сервиса с данными операции.
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получение чека по операции по operation_id.

        Args:
            operation_id: Идентификатор операции.

        Returns:
            httpx.Response: Ответ сервиса с чеком по операции.
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Получение списка операций для определенного счета.

        Args:
            query: Query-параметры запроса. Должны содержать accountId.

        Returns:
            httpx.Response: Ответ сервиса со списком операций.
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Получение статистики по операциям для определенного счета.

        Args:
            query: Query-параметры запроса. Должны содержать accountId.

        Returns:
            httpx.Response: Ответ сервиса со статистикой по операциям.
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Создание операции комиссии.

        Args:
            request: Тело запроса на создание операции комиссии.

        Returns:
            httpx.Response: Ответ сервиса с созданной операцией.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Создание операции пополнения.

        Args:
            request: Тело запроса на создание операции пополнения.

        Returns:
            httpx.Response: Ответ сервиса с созданной операцией.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Создание операции кэшбэка.

        Args:
            request: Тело запроса на создание операции кэшбэка.

        Returns:
            httpx.Response: Ответ сервиса с созданной операцией.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Создание операции перевода.

        Args:
            request: Тело запроса на создание операции перевода.

        Returns:
            httpx.Response: Ответ сервиса с созданной операцией.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Создание операции покупки.

        Args:
            request: Тело запроса на создание операции покупки.

        Returns:
            httpx.Response: Ответ сервиса с созданной операцией.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Создание операции оплаты по счету.

        Args:
            request: Тело запроса на создание операции оплаты по счету.

        Returns:
            httpx.Response: Ответ сервиса с созданной операцией.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Создание операции снятия наличных денег.

        Args:
            request: Тело запроса на создание операции снятия наличных денег.

        Returns:
            httpx.Response: Ответ сервиса с созданной операцией.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)