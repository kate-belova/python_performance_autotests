import allure

from contracts.services.gateway.operations.rpc_make_cash_withdrawal_operation_pb2 import (
    MakeCashWithdrawalOperationRequest,
    MakeCashWithdrawalOperationResponse,
)
from services.grpc.gateway.operations.operations_grpc_service import (
    OperationsGatewaygRPCService,
)


class MakeCashWithdrawalOperationGatewayMethod(OperationsGatewaygRPCService):
    def __init__(self):
        super().__init__()
        self.REQUEST = MakeCashWithdrawalOperationRequest
        self.RESPONSE = MakeCashWithdrawalOperationResponse

    @allure.step("Send gRPC request to make cash withdrawal operation")
    def send_request(self, card_id: str, account_id: str):
        request = self.REQUEST(
            status=self.status,
            amount=self.amount,
            card_id=card_id,
            account_id=account_id,
        )
        self.RESPONSE_DATA = self.SERVICE.MakeCashWithdrawalOperation(request)
        self.check_response_type(self.RESPONSE)
