from contracts.services.gateway.users.users_gateway_service_pb2_grpc import \
    UsersGatewayServiceStub
from services.grpc.base_service import BaseService


class UsersGatewaygRPCService(BaseService):
    def __init__(self):
        super().__init__()
        self.SERVICE = UsersGatewayServiceStub(self.CHANNEL)