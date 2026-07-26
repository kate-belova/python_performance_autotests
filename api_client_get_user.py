from services.http.gateway.users.create_user_api import CreateUserGatewayAPI
from services.http.gateway.users.get_user_api import GetUserGatewayAPI

create_user_gateway_client = CreateUserGatewayAPI()
get_user_gateway_client = GetUserGatewayAPI()

create_user_gateway_client.send_request()
print(
    "Create user data:",
    create_user_gateway_client.RESPONSE_DATA.model_dump_json(indent=2),
)

get_user_gateway_client.send_request(user_id=create_user_gateway_client.USER_ID)
print(
    "Get user data:",
    get_user_gateway_client.RESPONSE_DATA.model_dump_json(indent=2),
)
