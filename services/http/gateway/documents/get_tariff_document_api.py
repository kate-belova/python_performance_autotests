import httpx

from schemas.documents_schemas import TariffDocumentResponseSchema
from services.http.gateway.documents.documents_api import DocumentsGatewayAPI


class GetTariffDocumentGatewayAPI(DocumentsGatewayAPI):
    def __init__(self, client: httpx.Client | None = None):
        super().__init__(client)
        self.PATH = "/tariff-document"
        self.GET_TARIFF_DOCUMENT_PATH_NAME = (
            self.DOCUMENTS_PATH_NAME + self.PATH + "/{account_id}"
        )

    def send_request(self, account_id: str):
        extensions = {"path_name": self.GET_TARIFF_DOCUMENT_PATH_NAME}
        response = self.CLIENT.get(
            f"{self.DOCUMENTS_API}{self.PATH}/{account_id}",
            extensions=extensions,
        )

        content_type = response.headers.get("content-type", "")
        if "application/json" in content_type:
            self.RESPONSE_DATA = TariffDocumentResponseSchema(**response.json())
