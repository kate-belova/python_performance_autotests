import allure
from faker import Faker

from contracts.services.gateway.users.rpc_create_user_pb2 import (
    CreateUserRequest,
    CreateUserResponse,
)
from services.grpc.gateway.users.users_grpc_service import UsersGatewaygRPCService

faker = Faker()


class CreateUserGatewayMethod(UsersGatewaygRPCService):
    def __init__(self):
        super().__init__()
        self.REQUEST = CreateUserRequest
        self.RESPONSE = CreateUserResponse
        self.USER_ID = None

    @allure.step("Send gRPC request to create user")
    def send_request(self):
        request = self.REQUEST(
            email=faker.email(),
            last_name=faker.last_name(),
            first_name=faker.first_name(),
            middle_name=faker.first_name(),
            phone_number=faker.phone_number(),
        )

        self.RESPONSE_DATA = self.SERVICE.CreateUser(request)
        self.check_response_type(self.RESPONSE)
        self.USER_ID = self.RESPONSE_DATA.user.id
