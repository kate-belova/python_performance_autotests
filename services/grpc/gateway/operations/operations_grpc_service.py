from grpc import Channel

from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import (
    OperationsGatewayServiceStub,
)
from services.grpc.base_service import BaseService


class OperationsGatewaygRPCService(BaseService):
    def __init__(self, channel: Channel | None = None):
        super().__init__(channel)
        self.SERVICE = OperationsGatewayServiceStub(self.CHANNEL)
