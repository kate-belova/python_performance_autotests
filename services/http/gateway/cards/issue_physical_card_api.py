import allure
import httpx

from schemas.cards_schemas import IssueCardRequestSchema, IssueCardResponseSchema
from services.http.gateway.cards.cards_api import CardsGatewayAPI


class IssuePhysicalCardGatewayAPI(CardsGatewayAPI):
    def __init__(self):
        super().__init__()
        self.ISSUE_PHYSICAL_CARD_API = f"{self.CARDS_API}/issue-physical-card"

    @allure.step("Send POST request to issue physical card")
    def send_request(self, user_id: str, account_id: str):
        owner_data = IssueCardRequestSchema(
            user_id=user_id, account_id=account_id
        ).model_dump(by_alias=True)
        response = httpx.post(self.ISSUE_PHYSICAL_CARD_API, json=owner_data)
        self.get_card_response_data(response)
