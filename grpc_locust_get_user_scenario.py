from grpc import Channel
from locust import User, between, task

from services.grpc.client import create_locust_grpc_channel
from services.grpc.gateway.users.create_user_method import CreateUserGatewayMethod
from services.grpc.gateway.users.get_user_method import GetUserGatewayMethod


class GetUserScenarioUser(User):
    host = "localhost"
    wait_time = between(1, 3)

    grpc_channel: Channel
    create_user_client: CreateUserGatewayMethod
    get_user_client: GetUserGatewayMethod
    user_id: str

    def on_start(self) -> None:
        self.grpc_channel = create_locust_grpc_channel(self.environment)
        self.create_user_client = CreateUserGatewayMethod(self.grpc_channel)
        self.get_user_client = GetUserGatewayMethod(self.grpc_channel)

        self.create_user_client.send_request()
        self.user_id = self.create_user_client.USER_ID

    @task
    def get_user(self) -> None:
        self.get_user_client.send_request(user_id=self.user_id)

    def on_stop(self) -> None:
        self.grpc_channel.close()
