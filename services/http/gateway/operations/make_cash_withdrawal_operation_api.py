import allure
import httpx

from schemas.operations_schemas import MakeOperationRequestSchema
from services.http.gateway.operations.operations_api import OperationsGatewayAPI


class MakeCashWithdrawalOperationGatewayAPI(OperationsGatewayAPI):
    def __init__(self):
        super().__init__()
        self.MAKE_CASH_WITHDRAWAL_OPERATION_API = (
            f"{self.OPERATIONS_API}/make-cash-withdrawal-operation"
        )

    @allure.step("Send POST request to make cash withdrawal operation")
    def send_request(self, card_id: str, account_id: str):
        operation_data = MakeOperationRequestSchema(
            card_id=card_id, account_id=account_id
        )
        response = httpx.post(
            self.MAKE_CASH_WITHDRAWAL_OPERATION_API,
            json=operation_data.model_dump(by_alias=True),
        )
        self.get_operation_response_data(response)
