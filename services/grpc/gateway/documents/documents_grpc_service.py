from contracts.services.gateway.documents.documents_gateway_service_pb2_grpc import \
    DocumentsGatewayServiceStub
from services.grpc.base_service import BaseService


class DocumentsGatewaygRPCService(BaseService):
    def __init__(self):
        super().__init__()
        self.SERVICE = DocumentsGatewayServiceStub(self.CHANNEL)