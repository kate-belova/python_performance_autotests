import allure
import httpx

from services.http.gateway.operations.operations_api import OperationsGatewayAPI


class GetOperationGatewayAPI(OperationsGatewayAPI):
    def __init__(self):
        super().__init__()

    @allure.step("Send GET request to get operation details by operation id")
    def send_request(self, operation_id: str):
        response = httpx.get(f"{self.OPERATIONS_API}/{operation_id}")
        self.get_operation_response_data(response)
