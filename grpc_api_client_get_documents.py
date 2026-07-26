from services.grpc.gateway.accounts.open_credit_card_account_method import (
    OpenCreditCardAccountGatewayMethod,
)
from services.grpc.gateway.documents.get_contract_document_method import (
    GetContractDocumentGatewayMethod,
)
from services.grpc.gateway.documents.get_tariff_document_method import (
    GetTariffDocumentGatewayMethod,
)
from services.grpc.gateway.users.create_user_method import CreateUserGatewayMethod

create_user_client = CreateUserGatewayMethod()
open_credit_card_account_client = OpenCreditCardAccountGatewayMethod()
get_tariff_document_client = GetTariffDocumentGatewayMethod()
get_contract_document_client = GetContractDocumentGatewayMethod()

create_user_client.send_request()
user_data = create_user_client.RESPONSE_DATA
print("Create user response:", user_data)

user_id = create_user_client.USER_ID
open_credit_card_account_client.send_request(user_id=user_id)
credit_card_data = open_credit_card_account_client.RESPONSE_DATA
print("Open credit card account response:", credit_card_data)

account_id = open_credit_card_account_client.account_id
get_tariff_document_client.send_request(account_id=account_id)
tariff_document_data = get_tariff_document_client.RESPONSE_DATA
print("Get tariff document response:", tariff_document_data)

get_contract_document_client.send_request(account_id=account_id)
contract_document_data = get_contract_document_client.RESPONSE_DATA
print("Get contract document response:", contract_document_data)
