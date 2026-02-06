from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from tools.fakers import fake


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    PURCHASE = "PURCHASE"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    PENDING = "PENDING"


class OperationSchema(BaseModel):
    """
    Описание структуры операции (ответ API).
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
    url: str
    document: str


class OperationsSummarySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")


# ====== Requests ======

class GetOperationsQuerySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class GetOperationsSummaryQuerySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class MakeOperationRequestSchema(BaseModel):
    """
    Базовая структура запроса на создание операции.
    Должна создаваться без передачи status/amount (они генерируются автоматически).
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)  #  callable, без ()
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    """Запрос на создание операции комиссии."""


class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    """Запрос на создание операции пополнения."""


class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    """Запрос на создание операции кэшбэка."""


class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    """Запрос на создание операции перевода."""


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """
    Запрос на создание операции покупки.
    category тоже должна генерироваться автоматически.
    """
    category: str = Field(default_factory=fake.category)  #  callable, без ()


class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    """Запрос на создание операции оплаты по счету."""


class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    """Запрос на создание операции снятия наличных."""


# ====== Responses ======

class GetOperationResponseSchema(BaseModel):
    operation: OperationSchema


class GetOperationReceiptResponseSchema(BaseModel):
    receipt: OperationReceiptSchema


class GetOperationsResponseSchema(BaseModel):
    operations: list[OperationSchema]


class GetOperationsSummaryResponseSchema(BaseModel):
    summary: OperationsSummarySchema


class MakeFeeOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakeTopUpOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakeCashbackOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakeTransferOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakePurchaseOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakeBillPaymentOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    operation: OperationSchema
