import allure

from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import (
    MakeTopUpOperationRequest,
    MakeTopUpOperationResponse,
)
from services.grpc.gateway.operations.operations_grpc_service import (
    OperationsGatewaygRPCService,
)


class MakeTopUpOperationGatewayMethod(OperationsGatewaygRPCService):
    def __init__(self):
        super().__init__()
        self.REQUEST = MakeTopUpOperationRequest
        self.RESPONSE = MakeTopUpOperationResponse

    @allure.step("Send gRPC request to make top up operation")
    def send_request(self, card_id: str, account_id: str):
        request = self.REQUEST(
            status=self.status,
            amount=self.amount,
            card_id=card_id,
            account_id=account_id,
        )
        self.RESPONSE_DATA = self.SERVICE.MakeTopUpOperation(request)
        self.check_response_type(self.RESPONSE)
