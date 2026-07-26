import allure
import httpx

from schemas.accounts_schemas import AccountsResponseSchema
from services.http.gateway.accounts.accounts_api import AccountsGatewayAPI


class GetAccountsGatewayAPI(AccountsGatewayAPI):
    def __init__(self):
        super().__init__()
        self.GET_ACCOUNTS_API = self.ACCOUNTS_API

    @allure.step("Forming request parameters")
    def create_params(self, user_id: str):
        return {"userId": user_id}

    @allure.step("Send GET request to get user accounts by user id")
    def send_request(self, user_id: str):
        params = self.create_params(user_id=user_id)
        response = httpx.get(self.GET_ACCOUNTS_API, params=params)

        content_type = response.headers.get("content-type", "")
        if "application/json" in content_type:
            self.RESPONSE_DATA = AccountsResponseSchema(**response.json())
