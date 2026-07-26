import allure
import httpx

from schemas.operations_schemas import OperationReceiptResponseSchema
from services.http.gateway.operations.operations_api import OperationsGatewayAPI


class GetOperationReceiptGatewayAPI(OperationsGatewayAPI):
    def __init__(self):
        super().__init__()

    @allure.step("Send GET request to get operation receipt by operation id")
    def send_request(self, operation_id: str):
        response = httpx.get(f"{self.OPERATIONS_API}/operation-receipt/{operation_id}")
        content_type = response.headers.get("content-type", "")
        if "application/json" in content_type:
            self.RESPONSE_DATA = OperationReceiptResponseSchema(**response.json())
