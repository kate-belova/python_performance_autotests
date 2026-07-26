from services.grpc.gateway.accounts.open_debit_card_account_method import (
    OpenDebitCardAccountGatewayMethod,
)
from services.grpc.gateway.operations.make_top_up_operation_method import (
    MakeTopUpOperationGatewayMethod,
)
from services.grpc.gateway.users.create_user_method import CreateUserGatewayMethod

create_user_client = CreateUserGatewayMethod()
open_debit_card_account_client = OpenDebitCardAccountGatewayMethod()
make_top_up_operation_client = MakeTopUpOperationGatewayMethod()

create_user_client.send_request()
user_data = create_user_client.RESPONSE_DATA
print("Create user response:", user_data)

user_id = create_user_client.USER_ID
open_debit_card_account_client.send_request(user_id=user_id)
account_data = open_debit_card_account_client.RESPONSE_DATA
print("Open debit card account response:", account_data)

account_id = open_debit_card_account_client.account_id
card_id = open_debit_card_account_client.card_id
make_top_up_operation_client.send_request(account_id=account_id, card_id=card_id)
operation_data = make_top_up_operation_client.RESPONSE_DATA
print("Make top up operation response:", operation_data)
