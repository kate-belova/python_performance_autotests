from datetime import datetime
from enum import StrEnum

from faker import Faker
from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel

from schemas.documents_schemas import DocumentGatewaySchema

faker = Faker()

# fmt: off
CATEGORIES = [
    "alcohol", "air_tickets", "beauty", "books", "cafes", "cinema", "clothing",
    "education", "electricity", "electronics", "fast_food", "flowers", "gaming", 
    "gas_stations", "government_services", "groceries", "healthcare", "home_goods", 
    "hotels", "internet", "insurance", "marketplace", "mobile", "parking", "pets", 
    "pharmacies", "public_transport", "restaurants", "subscriptions", "sports", 
    "supermarket", "taxi", "tolls", "travel", "utilities", "water"
]
# fmt: on


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class OperationGatewaySchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str
    category: str
    created_at: datetime
    account_id: str


class OperationsResponseSchema(BaseModel):
    operations: list[OperationGatewaySchema]


class OperationsSummaryGatewaySchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    spent_amount: float
    received_amount: float
    cashback_amount: float


class OperationsSummaryResponseSchema(BaseModel):
    summary: list[OperationsSummaryGatewaySchema]


class OperationReceiptResponseSchema(BaseModel):
    receipt: DocumentGatewaySchema


class OperationResponseSchema(BaseModel):
    operation: OperationGatewaySchema


class MakeOperationRequestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_name=True,
        validate_by_alias=True,
    )

    status: OperationStatus = Field(
        default_factory=lambda: faker.random_element(list(OperationStatus))
    )
    amount: float = Field(
        default_factory=lambda: faker.pyfloat(
            positive=True,
            min_value=1,
            max_value=50000,
            right_digits=2,
        )
    )
    card_id: str
    account_id: str


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    category: str = Field(default_factory=lambda: faker.random_element(CATEGORIES))
