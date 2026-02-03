from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class OperationType(StrEnum):
    """
    Тип операции.
    """
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    PURCHASE = "PURCHASE"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    """
    Статус операции.
    """
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    PENDING = "PENDING"


class OperationSchema(BaseModel):
    """
    Описание структуры операции.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: Optional[str] = None
    created_at: datetime = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")


class OperationReceiptSchema(BaseModel):
    """
    Описание структуры чека по операции.
    """
    url: str
    document: str


class OperationsSummarySchema(BaseModel):
    """
    Описание структуры статистики по операциям.
    """
    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")


# ====== Requests ======

class GetOperationsQuerySchema(BaseModel):
    """
    Query-параметры для получения списка операций по счету.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class GetOperationsSummaryQuerySchema(BaseModel):
    """
    Query-параметры для получения статистики по операциям по счету.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class MakeOperationRequestSchema(BaseModel):
    """
    Базовая структура запроса на создание операции.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    """
    Запрос на создание операции комиссии.
    """


class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    """
    Запрос на создание операции пополнения.
    """


class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    """
    Запрос на создание операции кэшбэка.
    """


class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    """
    Запрос на создание операции перевода.
    """


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """
    Запрос на создание операции покупки.
    """
    category: str


class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    """
    Запрос на создание операции оплаты по счету.
    """


class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    """
    Запрос на создание операции снятия наличных.
    """


# ====== Responses ======

class GetOperationResponseSchema(BaseModel):
    """
    Ответ получения операции по operation_id.
    """
    operation: OperationSchema


class GetOperationReceiptResponseSchema(BaseModel):
    """
    Ответ получения чека по операции.
    """
    receipt: OperationReceiptSchema


class GetOperationsResponseSchema(BaseModel):
    """
    Ответ получения списка операций.
    """
    operations: list[OperationSchema]


class GetOperationsSummaryResponseSchema(BaseModel):
    """
    Ответ получения статистики по операциям.
    """
    summary: OperationsSummarySchema


class MakeFeeOperationResponseSchema(BaseModel):
    """
    Ответ создания операции комиссии.
    """
    operation: OperationSchema


class MakeTopUpOperationResponseSchema(BaseModel):
    """
    Ответ создания операции пополнения.
    """
    operation: OperationSchema


class MakeCashbackOperationResponseSchema(BaseModel):
    """
    Ответ создания операции кэшбэка.
    """
    operation: OperationSchema


class MakeTransferOperationResponseSchema(BaseModel):
    """
    Ответ создания операции перевода.
    """
    operation: OperationSchema


class MakePurchaseOperationResponseSchema(BaseModel):
    """
    Ответ создания операции покупки.
    """
    operation: OperationSchema


class MakeBillPaymentOperationResponseSchema(BaseModel):
    """
    Ответ создания операции оплаты по счету.
    """
    operation: OperationSchema


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """
    Ответ создания операции снятия наличных.
    """
    operation: OperationSchema
