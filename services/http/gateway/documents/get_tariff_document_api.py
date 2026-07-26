import allure
import httpx

from schemas.documents_schemas import TariffDocumentResponseSchema
from services.http.gateway.documents.documents_api import DocumentsGatewayAPI


class GetTariffDocumentGatewayAPI(DocumentsGatewayAPI):
    def __init__(self):
        super().__init__()

    @allure.step("Send GET request to get account tariff document by account id")
    def send_request(self, account_id: str):
        response = httpx.get(f"{self.DOCUMENTS_API}/tariff-document/{account_id}")
        content_type = response.headers.get("content-type", "")
        if "application/json" in content_type:
            self.RESPONSE_DATA = TariffDocumentResponseSchema(**response.json())
