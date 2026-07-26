import allure

from contracts.services.gateway.operations.rpc_make_bill_payment_operation_pb2 import (
    MakeBillPaymentOperationRequest,
    MakeBillPaymentOperationResponse,
)
from services.grpc.gateway.operations.operations_grpc_service import (
    OperationsGatewaygRPCService,
)


class MakeBillPaymentOperationGatewayMethod(OperationsGatewaygRPCService):
    def __init__(self):
        super().__init__()
        self.REQUEST = MakeBillPaymentOperationRequest
        self.RESPONSE = MakeBillPaymentOperationResponse

    @allure.step("Send gRPC request to make bill payment operation")
    def send_request(self, card_id: str, account_id: str):
        request = self.REQUEST(
            status=self.status,
            amount=self.amount,
            card_id=card_id,
            account_id=account_id,
        )
        self.RESPONSE_DATA = self.SERVICE.MakeBillPaymentOperation(request)
        self.check_response_type(self.RESPONSE)
