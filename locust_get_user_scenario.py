import httpx
from locust import User, between, task

from services.http.client import create_locust_http_client
from services.http.gateway.users.create_user_api import CreateUserGatewayAPI
from services.http.gateway.users.get_user_api import GetUserGatewayAPI


class GetUserScenarioUser(User):
    host = "localhost"
    wait_time = between(1, 3)

    http_client: httpx.Client
    create_user_client: CreateUserGatewayAPI
    get_user_client: GetUserGatewayAPI
    user_id: str

    def on_start(self) -> None:
        self.http_client = create_locust_http_client(self.environment)
        self.create_user_client = CreateUserGatewayAPI(self.http_client)
        self.get_user_client = GetUserGatewayAPI(self.http_client)

        self.create_user_client.send_request()
        self.user_id = self.create_user_client.USER_ID

    @task
    def get_user(self) -> None:
        try:
            self.get_user_client.send_request(user_id=self.user_id)
        except httpx.RequestError:
            pass

    def on_stop(self) -> None:
        self.http_client.close()
