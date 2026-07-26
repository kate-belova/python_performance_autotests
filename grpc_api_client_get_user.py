from services.grpc.gateway.users.create_user_method import CreateUserGatewayMethod
from services.grpc.gateway.users.get_user_method import GetUserGatewayMethod

create_user_gateway_client = CreateUserGatewayMethod()
get_user_gateway_client = GetUserGatewayMethod()

create_user_gateway_client.send_request()
print("Create user data:", create_user_gateway_client.RESPONSE_DATA)

get_user_gateway_client.send_request(user_id=create_user_gateway_client.USER_ID)
print("Get user data:", get_user_gateway_client.RESPONSE_DATA)
