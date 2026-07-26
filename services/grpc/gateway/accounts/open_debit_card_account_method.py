import allure

from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import (
    OpenDebitCardAccountRequest,
    OpenDebitCardAccountResponse,
)
from services.grpc.gateway.accounts.accounts_grpc_service import (
    AccountsGatewaygRPCService,
)


class OpenDebitCardAccountGatewayMethod(AccountsGatewaygRPCService):
    def __init__(self):
        super().__init__()
        self.REQUEST = OpenDebitCardAccountRequest
        self.RESPONSE = OpenDebitCardAccountResponse

    @allure.step("Send gRPC request to open debit card account")
    def send_request(self, user_id: str):
        request = self.REQUEST(user_id=user_id)
        self.RESPONSE_DATA = self.SERVICE.OpenDebitCardAccount(request)
        self.check_response_type(self.RESPONSE)
