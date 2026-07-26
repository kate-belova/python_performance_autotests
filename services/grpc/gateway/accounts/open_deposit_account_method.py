import allure

from contracts.services.gateway.accounts.rpc_open_deposit_account_pb2 import (
    OpenDepositAccountRequest,
    OpenDepositAccountResponse,
)
from services.grpc.gateway.accounts.accounts_grpc_service import (
    AccountsGatewaygRPCService,
)


class OpenDepositAccountGatewayMethod(AccountsGatewaygRPCService):
    def __init__(self):
        super().__init__()
        self.REQUEST = OpenDepositAccountRequest
        self.RESPONSE = OpenDepositAccountResponse

    @allure.step("Send gRPC request to open deposit account")
    def send_request(self, user_id: str):
        request = self.REQUEST(user_id=user_id)
        self.RESPONSE_DATA = self.SERVICE.OpenDepositAccount(request)
        self.check_response_type(self.RESPONSE)
