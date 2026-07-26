from services.grpc.gateway.accounts.open_debit_card_account_method import \
    OpenDebitCardAccountGatewayMethod
from services.grpc.gateway.cards.issue_physical_card_method import \
    IssuePhysicalCardGatewayMethod
from services.grpc.gateway.users.create_user_method import CreateUserGatewayMethod

create_user_gateway_client = CreateUserGatewayMethod()
open_debit_card_account_gateway_client = OpenDebitCardAccountGatewayMethod()
issue_physical_card_gateway_client = IssuePhysicalCardGatewayMethod()

create_user_gateway_client.send_request()
user_data = create_user_gateway_client.RESPONSE_DATA
print("Create user data:", user_data)

user_id = create_user_gateway_client.USER_ID
open_debit_card_account_gateway_client.send_request(user_id=user_id)
account_data = open_debit_card_account_gateway_client.RESPONSE_DATA
print("Open debit card account data:", account_data)

account_id = open_debit_card_account_gateway_client.account_id
issue_physical_card_gateway_client.send_request(user_id=user_id, account_id=account_id)
card_data = issue_physical_card_gateway_client.RESPONSE_DATA
print("Issue physical card data:", card_data)
