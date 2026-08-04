from grpc import Channel
from locust import between, task, User

from services.grpc.client import create_locust_grpc_channel
from services.grpc.gateway.accounts.open_debit_card_account_method import (
    OpenDebitCardAccountGatewayMethod,
)
from services.grpc.gateway.users.create_user_method import CreateUserGatewayMethod


class OpenDebitCardAccountScenarioUser(User):
    host = "localhost"
    wait_time = between(1, 3)

    grpc_channel: Channel
    create_user_client: CreateUserGatewayMethod
    open_debit_card_account_client: OpenDebitCardAccountGatewayMethod
    user_id: str

    def on_start(self) -> None:
        self.grpc_channel = create_locust_grpc_channel(self.environment)
        self.create_user_client = CreateUserGatewayMethod(self.grpc_channel)
        self.open_debit_card_account_client = OpenDebitCardAccountGatewayMethod(
            self.grpc_channel
        )

        self.create_user_client.send_request()
        self.user_id = self.create_user_client.USER_ID

    @task
    def open_debit_card_account(self) -> None:
        self.open_debit_card_account_client.send_request(user_id=self.user_id)

    def on_stop(self) -> None:
        self.grpc_channel.close()
