from __future__ import annotations

from typing import TypedDict

from httpx import QueryParams, Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


# ====== Response structures ======

class OperationDict(TypedDict):
    """
    Описание структуры операции.
    """
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str


class OperationReceiptDict(TypedDict):
    """
    Описание структуры чека по операции.
    """
    url: str
    document: str


class OperationsSummaryDict(TypedDict):
    """
    Описание структуры статистики по операциям.
    """
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


# ====== Query/Request structures ======

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


# ====== Response wrappers (как в уроке account: AccountDict и т.п.) ======

class GetOperationResponseDict(TypedDict):
    operation: OperationDict


class GetOperationReceiptResponseDict(TypedDict):
    receipt: OperationReceiptDict


class GetOperationsResponseDict(TypedDict):
    operations: list[OperationDict]


class GetOperationsSummaryResponseDict(TypedDict):
    summary: OperationsSummaryDict


class MakeFeeOperationResponseDict(TypedDict):
    operation: OperationDict


class MakeTopUpOperationResponseDict(TypedDict):
    operation: OperationDict


class MakeCashbackOperationResponseDict(TypedDict):
    operation: OperationDict


class MakeTransferOperationResponseDict(TypedDict):
    operation: OperationDict


class MakePurchaseOperationResponseDict(TypedDict):
    operation: OperationDict


class MakeBillPaymentOperationResponseDict(TypedDict):
    operation: OperationDict


class MakeCashWithdrawalOperationResponseDict(TypedDict):
    operation: OperationDict


class OperationsGatewayHTTPClient(HTTPClient):
    """HTTP API клиент для эндпоинтов /api/v1/operations сервиса http-gateway."""

    # ====== Low-level API methods (у тебя уже есть) ======

    def get_operation_api(self, operation_id: str) -> Response:
        """
        GET /api/v1/operations/{operation_id}
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        GET /api/v1/operations/operation-receipt/{operation_id}
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        GET /api/v1/operations
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        GET /api/v1/operations/operations-summary
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        POST /api/v1/operations/make-fee-operation
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        POST /api/v1/operations/make-top-up-operation
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        POST /api/v1/operations/make-cashback-operation
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        POST /api/v1/operations/make-transfer-operation
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        POST /api/v1/operations/make-purchase-operation
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        POST /api/v1/operations/make-bill-payment-operation
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        POST /api/v1/operations/make-cash-withdrawal-operation
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)

    # ====== High-level methods (ТЗ) ======

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        """
        Высокоуровневый метод получения операции.
        """
        response = self.get_operation_api(operation_id)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        """
        Высокоуровневый метод получения чека операции.
        """
        response = self.get_operation_receipt_api(operation_id)
        return response.json()

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        """
        Высокоуровневый метод получения списка операций по счету.
        """
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        """
        Высокоуровневый метод получения статистики по операциям по счету.
        """
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        """
        Высокоуровневый метод создания операции комиссии.
        """
        request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        """
        Высокоуровневый метод создания операции пополнения.
        """
        request = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=1500.11,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseDict:
        """
        Высокоуровневый метод создания операции кэшбэка.
        """
        request = MakeCashbackOperationRequestDict(
            status="COMPLETED",
            amount=10.01,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseDict:
        """
        Высокоуровневый метод создания операции перевода.
        """
        request = MakeTransferOperationRequestDict(
            status="COMPLETED",
            amount=100.00,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseDict:
        """
        Высокоуровневый метод создания операции покупки.
        """
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=25.50,
            cardId=card_id,
            accountId=account_id,
            category="food",
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseDict:
        """
        Высокоуровневый метод создания операции оплаты по счету.
        """
        request = MakeBillPaymentOperationRequestDict(
            status="COMPLETED",
            amount=500.00,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseDict:
        """
        Высокоуровневый метод создания операции снятия наличных.
        """
        request = MakeCashWithdrawalOperationRequestDict(
            status="COMPLETED",
            amount=200.00,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
