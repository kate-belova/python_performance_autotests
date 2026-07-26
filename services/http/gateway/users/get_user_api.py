import allure
import httpx

from services.http.gateway.users.users_api import UsersGatewayAPI


class GetUserGatewayAPI(UsersGatewayAPI):
    def __init__(self):
        super().__init__()

    @allure.step("Send GET request to get user by user id")
    def send_request(self, user_id: str):
        response = httpx.get(f"{self.USERS_API}/{user_id}")
        self.get_user_response_data(response)
