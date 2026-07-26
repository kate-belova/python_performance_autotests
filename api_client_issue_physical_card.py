from services.http.gateway.accounts.open_debit_card_account_api import (
    OpenDebitCardAccountGatewayAPI,
)
from services.http.gateway.cards.issue_physical_card_api import (
    IssuePhysicalCardGatewayAPI,
)
from services.http.gateway.users.create_user_api import CreateUserGatewayAPI

create_user_gateway_client = CreateUserGatewayAPI()
open_debit_card_account_gateway_client = OpenDebitCardAccountGatewayAPI()
issue_physical_card_gateway_client = IssuePhysicalCardGatewayAPI()

create_user_gateway_client.send_request()
user_data = create_user_gateway_client.RESPONSE_DATA.model_dump_json(indent=2)
print("Create user data:", user_data)

user_id = create_user_gateway_client.USER_ID
open_debit_card_account_gateway_client.send_request(user_id=user_id)
account_data = open_debit_card_account_gateway_client.RESPONSE_DATA.model_dump_json(
    indent=2
)
print("Open debit card account data:", account_data)

account_id = open_debit_card_account_gateway_client.account_id
issue_physical_card_gateway_client.send_request(user_id=user_id, account_id=account_id)
card_data = issue_physical_card_gateway_client.RESPONSE_DATA.model_dump_json(indent=2)
print("Issue physical card data:", card_data)
