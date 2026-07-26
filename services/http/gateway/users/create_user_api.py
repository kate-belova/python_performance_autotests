import allure
import httpx

from schemas.users_schemas import UserRequestSchema
from services.http.gateway.users.users_api import UsersGatewayAPI


class CreateUserGatewayAPI(UsersGatewayAPI):
    def __init__(self):
        super().__init__()
        self.CREATE_USER_API = f"{self.BASE_API}/users"
        self.USER_ID = None

    @allure.step("Send POST request to create user")
    def send_request(self):
        user_data = UserRequestSchema().model_dump(by_alias=True)
        response = httpx.post(self.CREATE_USER_API, json=user_data)
        self.get_user_response_data(response)
        self.USER_ID = self.RESPONSE_DATA.user.id
