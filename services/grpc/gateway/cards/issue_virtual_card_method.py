import allure

from contracts.services.gateway.cards.rpc_issue_virtual_card_pb2 import (
    IssueVirtualCardRequest,
    IssueVirtualCardResponse,
)
from services.grpc.gateway.cards.cards_grpc_service import CardsGatewaygRPCService


class IssueVirtualCardGatewayMethod(CardsGatewaygRPCService):
    def __init__(self):
        super().__init__()
        self.REQUEST = IssueVirtualCardRequest
        self.RESPONSE = IssueVirtualCardResponse

    @allure.step("Send gRPC request to issue virtual card")
    def send_request(self, user_id: str, account_id: str):
        request = self.REQUEST(user_id=user_id, account_id=account_id)
        self.RESPONSE_DATA = self.SERVICE.IssueVirtualCard(request)
        self.check_response_type(self.RESPONSE)
