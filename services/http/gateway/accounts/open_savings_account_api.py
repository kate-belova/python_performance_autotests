import allure
import httpx

from schemas.accounts_schemas import OpenAccountRequestSchema
from services.http.gateway.accounts.accounts_api import AccountsGatewayAPI


class OpenSavingsAccountGatewayAPI(AccountsGatewayAPI):
    def __init__(self):
        super().__init__()
        self.OPEN_SAVINGS_ACCOUNT_API = f"{self.ACCOUNTS_API}/open-savings-account"

    @allure.step("Send POST request to open savings account")
    def send_request(self, user_id: str):
        user_data = OpenAccountRequestSchema(user_id=user_id).model_dump(by_alias=True)
        response = httpx.post(self.OPEN_SAVINGS_ACCOUNT_API, json=user_data)
        self.get_account_response_data(response)
