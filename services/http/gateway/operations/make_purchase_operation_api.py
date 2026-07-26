import allure
import httpx

from schemas.operations_schemas import (
    MakePurchaseOperationRequestSchema,
)
from services.http.gateway.operations.operations_api import OperationsGatewayAPI


class MakePurchaseOperationGatewayAPI(OperationsGatewayAPI):
    def __init__(self):
        super().__init__()
        self.MAKE_PURCHASE_OPERATION_API = (
            f"{self.OPERATIONS_API}/make-purchase-operation"
        )

    @allure.step("Send POST request to make purchase operation")
    def send_request(self, card_id: str, account_id: str):
        operation_data = MakePurchaseOperationRequestSchema(
            card_id=card_id, account_id=account_id
        )
        response = httpx.post(
            self.MAKE_PURCHASE_OPERATION_API,
            json=operation_data.model_dump(by_alias=True),
        )
        self.get_operation_response_data(response)
