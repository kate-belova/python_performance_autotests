import allure

from contracts.services.gateway.operations.rpc_get_operations_summary_pb2 import (
    GetOperationsSummaryRequest,
    GetOperationsSummaryResponse,
)
from services.grpc.gateway.operations.operations_grpc_service import (
    OperationsGatewaygRPCService,
)


class GetOperationsSummaryGatewayMethod(OperationsGatewaygRPCService):
    def __init__(self):
        super().__init__()
        self.REQUEST = GetOperationsSummaryRequest
        self.RESPONSE = GetOperationsSummaryResponse

    @allure.step("Send gRPC request to get account operations summary by account id")
    def send_request(self, account_id: str):
        request = self.REQUEST(account_id=account_id)
        self.RESPONSE_DATA = self.SERVICE.GetOperationsSummary(request)
        self.check_response_type(self.RESPONSE)
