import allure

from contracts.services.gateway.documents.rpc_get_tariff_document_pb2 import (
    GetTariffDocumentRequest,
    GetTariffDocumentResponse,
)
from services.grpc.gateway.documents.documents_grpc_service import (
    DocumentsGatewaygRPCService,
)


class GetTariffDocumentGatewayMethod(DocumentsGatewaygRPCService):
    def __init__(self):
        super().__init__()
        self.REQUEST = GetTariffDocumentRequest
        self.RESPONSE = GetTariffDocumentResponse

    @allure.step("Send gRPC request to get tariff document by account id")
    def send_request(self, account_id: str):
        request = self.REQUEST(account_id=account_id)
        self.RESPONSE_DATA = self.SERVICE.GetTariffDocument(request)
        self.check_response_type(self.RESPONSE)
