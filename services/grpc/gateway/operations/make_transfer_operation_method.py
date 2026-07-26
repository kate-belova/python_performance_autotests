import allure

from contracts.services.gateway.operations.rpc_make_transfer_operation_pb2 import (
    MakeTransferOperationRequest,
    MakeTransferOperationResponse,
)
from services.grpc.gateway.operations.operations_grpc_service import (
    OperationsGatewaygRPCService,
)


class MakeTransferOperationGatewayMethod(OperationsGatewaygRPCService):
    def __init__(self):
        super().__init__()
        self.REQUEST = MakeTransferOperationRequest
        self.RESPONSE = MakeTransferOperationResponse

    @allure.step("Send gRPC request to make transfer operation")
    def send_request(self, card_id: str, account_id: str):
        request = self.REQUEST(
            status=self.status,
            amount=self.amount,
            card_id=card_id,
            account_id=account_id,
        )
        self.RESPONSE_DATA = self.SERVICE.MakeTransferOperation(request)
        self.check_response_type(self.RESPONSE)
