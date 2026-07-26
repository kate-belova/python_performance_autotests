from services.http.gateway.accounts.open_debit_card_account_api import (
    OpenDebitCardAccountGatewayAPI,
)
from services.http.gateway.operations.make_top_up_operation_api import (
    MakeTopUpOperationGatewayAPI,
)
from services.http.gateway.users.create_user_api import CreateUserGatewayAPI

create_user_client = CreateUserGatewayAPI()
open_debit_card_account_client = OpenDebitCardAccountGatewayAPI()
make_top_up_operation_client = MakeTopUpOperationGatewayAPI()

create_user_client.send_request()
user_data = create_user_client.RESPONSE_DATA.model_dump_json(indent=2)
print("Create user response:", user_data)

user_id = create_user_client.USER_ID
open_debit_card_account_client.send_request(user_id=user_id)
account_data = open_debit_card_account_client.RESPONSE_DATA.model_dump_json(indent=2)
print("Open debit card account response:", account_data)

account_id = open_debit_card_account_client.account_id
card_id = open_debit_card_account_client.card_id
make_top_up_operation_client.send_request(account_id=account_id, card_id=card_id)
operation_data = make_top_up_operation_client.RESPONSE_DATA.model_dump_json(indent=2)
print("Make top up operation response:", operation_data)
