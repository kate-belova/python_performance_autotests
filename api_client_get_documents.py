from services.http.gateway.accounts.open_credit_card_account_api import (
    OpenCreditCardAccountGatewayAPI,
)
from services.http.gateway.documents.get_contract_document_api import (
    GetContractDocumentGatewayAPI,
)
from services.http.gateway.documents.get_tariff_document_api import (
    GetTariffDocumentGatewayAPI,
)
from services.http.gateway.users.create_user_api import CreateUserGatewayAPI

create_user_client = CreateUserGatewayAPI()
open_credit_card_account_client = OpenCreditCardAccountGatewayAPI()
get_tariff_document_client = GetTariffDocumentGatewayAPI()
get_contract_document_client = GetContractDocumentGatewayAPI()

create_user_client.send_request()
user_data = create_user_client.RESPONSE_DATA.model_dump_json(indent=2)
print("Create user response:", user_data)

user_id = create_user_client.USER_ID
open_credit_card_account_client.send_request(user_id=user_id)
credit_card_data = open_credit_card_account_client.RESPONSE_DATA.model_dump_json(
    indent=2
)
print("Open credit card account response:", credit_card_data)

account_id = open_credit_card_account_client.account_id
get_tariff_document_client.send_request(account_id=account_id)
tariff_document_data = get_tariff_document_client.RESPONSE_DATA.model_dump_json(
    indent=2
)
print("Get tariff document response:", tariff_document_data)

get_contract_document_client.send_request(account_id=account_id)
contract_document_data = get_contract_document_client.RESPONSE_DATA.model_dump_json(
    indent=2
)
print("Get contract document response:", contract_document_data)
