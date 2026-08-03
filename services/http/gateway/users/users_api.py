import httpx

from schemas.users_schemas import UserResponseSchema
from services.http.base_api import BaseAPI


class UsersGatewayAPI(BaseAPI):
    def __init__(self, client: httpx.Client | None = None):
        super().__init__(client)
        self.USERS_PATH_NAME = self.USERS_API = "/users"

    def get_user_response_data(self, response):
        content_type = response.headers.get("content-type", "")
        if "application/json" in content_type:
            self.RESPONSE_DATA = UserResponseSchema(**response.json())
