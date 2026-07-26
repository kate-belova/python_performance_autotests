import allure

from contracts.services.gateway.operations.rpc_get_operations_pb2 import (
    GetOperationsRequest,
    GetOperationsResponse,
)
from services.grpc.gateway.operations.operations_grpc_service import (
    OperationsGatewaygRPCService,
)


class GetOperationsGatewayMethod(OperationsGatewaygRPCService):
    def __init__(self):
        super().__init__()
        self.REQUEST = GetOperationsRequest
        self.RESPONSE = GetOperationsResponse

    @allure.step("Send gRPC request to get account operations by account id")
    def send_request(self, account_id: str):
        request = self.REQUEST(account_id=account_id)
        self.RESPONSE_DATA = self.SERVICE.GetOperationsResponse(request)
        self.check_response_type(self.RESPONSE)
