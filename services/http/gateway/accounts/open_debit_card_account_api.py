import allure
import httpx

from schemas.accounts_schemas import OpenAccountRequestSchema
from services.http.gateway.accounts.accounts_api import AccountsGatewayAPI


class OpenDebitCardAccountGatewayAPI(AccountsGatewayAPI):
    def __init__(self):
        super().__init__()
        self.OPEN_DEBIT_CARD_ACCOUNT_API = (
            f"{self.ACCOUNTS_API}/open-debit-card-account"
        )

    @allure.step("Send POST request to open debit card account")
    def send_request(self, user_id: str):
        user_data = OpenAccountRequestSchema(user_id=user_id).model_dump(by_alias=True)
        response = httpx.post(self.OPEN_DEBIT_CARD_ACCOUNT_API, json=user_data)
        self.get_account_response_data(response)
