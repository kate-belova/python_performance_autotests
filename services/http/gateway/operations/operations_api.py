import allure

from schemas.operations_schemas import OperationResponseSchema
from services.http.base_api import BaseAPI


class OperationsGatewayAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.OPERATIONS_API = f"{self.BASE_API}/operations"

    @allure.step("Forming request parameters")
    def create_params(self, account_id: str):
        return {"accountId": account_id}

    def get_operation_response_data(self, response):
        content_type = response.headers.get("content-type", "")
        if "application/json" in content_type:
            self.RESPONSE_DATA = OperationResponseSchema(**response.json())
