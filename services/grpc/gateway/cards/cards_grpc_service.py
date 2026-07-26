from contracts.services.gateway.cards.cards_gateway_service_pb2_grpc import (
    CardsGatewayServiceStub,
)
from services.grpc.base_service import BaseService


class CardsGatewaygRPCService(BaseService):
    def __init__(self):
        super().__init__()
        self.SERVICE = CardsGatewayServiceStub(self.CHANNEL)
