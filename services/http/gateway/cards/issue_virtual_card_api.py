import allure
import httpx

from schemas.cards_schemas import IssueCardRequestSchema
from services.http.gateway.cards.cards_api import CardsGatewayAPI


class IssueVirtualCardGatewayAPI(CardsGatewayAPI):
    def __init__(self):
        super().__init__()
        self.ISSUE_VIRTUAL_CARDS_API = f"{self.CARDS_API}/issue-virtual-cards"

    @allure.step("Send POST request to issue virtual card")
    def send_request(self, user_id: str, account_id: str):
        owner_data = IssueCardRequestSchema(
            user_id=user_id, account_id=account_id
        ).model_dump(by_alias=True)
        response = httpx.post(self.ISSUE_VIRTUAL_CARDS_API, json=owner_data)
        self.get_card_response_data(response)
