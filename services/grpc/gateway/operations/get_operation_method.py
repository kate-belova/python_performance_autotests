import allure

from contracts.services.gateway.operations.rpc_get_operation_pb2 import (
    GetOperationRequest,
    GetOperationResponse,
)
from services.grpc.gateway.operations.operations_grpc_service import (
    OperationsGatewaygRPCService,
)


class GetOperationGatewayMethod(OperationsGatewaygRPCService):
    def __init__(self):
        super().__init__()
        self.REQUEST = GetOperationRequest
        self.RESPONSE = GetOperationResponse

    @allure.step("Send gRPC request to get operation details by operation id")
    def send_request(self, operation_id: str):
        request = self.REQUEST(id=operation_id)
        self.RESPONSE_DATA = self.SERVICE.GetOperation(request)
        self.check_response_type(self.RESPONSE)
