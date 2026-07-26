from schemas.accounts_schemas import AccountResponseSchema
from services.http.base_api import BaseAPI


class AccountsGatewayAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.ACCOUNTS_API = f"{self.BASE_API}/accounts"

    def get_account_response_data(self, response):
        content_type = response.headers.get("content-type", "")
        if "application/json" in content_type:
            self.RESPONSE_DATA = AccountResponseSchema(**response.json())

    @property
    def account_id(self):
        if self.RESPONSE_DATA is None:
            raise ValueError("RESPONSE_DATA is empty. Call send_request() first.")
        return self.RESPONSE_DATA.account.id

    @property
    def card_id(self):
        if self.RESPONSE_DATA is None:
            raise ValueError("RESPONSE_DATA is empty. Call send_request() first.")
        return self.RESPONSE_DATA.account.cards[0].id
