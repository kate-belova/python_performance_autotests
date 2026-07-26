import allure

from contracts.services.gateway.accounts.rpc_get_accounts_pb2 import (
    GetAccountsRequest,
    GetAccountsResponse,
)
from services.grpc.gateway.accounts.accounts_grpc_service import (
    AccountsGatewaygRPCService,
)


class GetAccountsGetwayMethod(AccountsGatewaygRPCService):
    def __init__(self):
        super().__init__()
        self.REQUEST = GetAccountsRequest
        self.RESPONSE = GetAccountsResponse

    @allure.step("Send gRPC request to get user accounts by user id")
    def send_request(self, user_id: str):
        request = self.REQUEST(user_id=user_id)
        self.RESPONSE_DATA = self.SERVICE.GetAccounts(request)
        self.check_response_type(self.RESPONSE)
