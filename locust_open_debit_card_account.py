import httpx
from locust import between, task, User

from services.http.client import create_locust_http_client
from services.http.gateway.accounts.open_debit_card_account_api import (
    OpenDebitCardAccountGatewayAPI,
)
from services.http.gateway.users.create_user_api import CreateUserGatewayAPI


class OpenDebitCardAccountScenarioUser(User):
    host = "localhost"
    wait_time = between(1, 3)

    http_client: httpx.Client
    create_user_client: CreateUserGatewayAPI
    open_debit_card_account_client: OpenDebitCardAccountGatewayAPI
    user_id: str

    def on_start(self) -> None:
        self.http_client = create_locust_http_client(self.environment)
        self.create_user_client = CreateUserGatewayAPI(self.http_client)
        self.open_debit_card_account_client = OpenDebitCardAccountGatewayAPI(
            self.http_client
        )

        self.create_user_client.send_request()
        self.user_id = self.create_user_client.USER_ID

    @task
    def open_debit_card_account(self) -> None:
        try:
            self.open_debit_card_account_client.send_request(user_id=self.user_id)
        except httpx.RequestError:
            pass

    def on_stop(self) -> None:
        self.http_client.close()
