from faker import Faker

from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import (
    OperationsGatewayServiceStub,
)
from contracts.services.operations.operation_pb2 import OperationStatus
from services.grpc.base_service import BaseService

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


class OperationsGatewaygRPCService(BaseService):
    def __init__(self):
        super().__init__()
        self.SERVICE = OperationsGatewayServiceStub(self.CHANNEL)

    @property
    def status(self):
        return faker.random_element(OperationStatus.values())

    @property
    def amount(self):
        return faker.pyfloat(
            positive=True, min_value=1, max_value=50000, right_digits=2
        )

    @property
    def category(self):
        return faker.random_element(CATEGORIES)
