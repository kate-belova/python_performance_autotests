import allure
import httpx

from schemas.operations_schemas import OperationsSummaryResponseSchema
from services.http.gateway.operations.operations_api import OperationsGatewayAPI


class GetOperationsSummaryGatewayAPI(OperationsGatewayAPI):
    def __init__(self):
        super().__init__()
        self.GET_OPERATIONS_SUMMARY_API = f"{self.OPERATIONS_API}/operations-summary"

    @allure.step("Send GET request to get account operations summary by account id")
    def send_request(self, account_id: str):
        params = self.create_params(account_id=account_id)
        response = httpx.get(self.GET_OPERATIONS_SUMMARY_API, params=params)

        content_type = response.headers.get("content-type", "")
        if "application/json" in content_type:
            self.RESPONSE_DATA = OperationsSummaryResponseSchema(**response.json())
