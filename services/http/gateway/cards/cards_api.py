import httpx

from schemas.cards_schemas import IssueCardResponseSchema
from services.http.base_api import BaseAPI


class CardsGatewayAPI(BaseAPI):
    def __init__(self, client: httpx.Client | None = None):
        super().__init__(client)
        self.CARDS_PATH_NAME = self.CARDS_API = "/cards"

    def get_card_response_data(self, response):
        content_type = response.headers.get("content-type", "")
        if "application/json" in content_type:
            self.RESPONSE_DATA = IssueCardResponseSchema(**response.json())
