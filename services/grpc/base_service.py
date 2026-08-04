import grpc

from services.grpc.client import create_grpc_channel


class BaseService:
    def __init__(self, channel: grpc.Channel | None = None):
        self.CHANNEL = channel or create_grpc_channel()
        self.RESPONSE_DATA = None

    def check_response_type(self, response_type):
        if self.RESPONSE_DATA is None:
            raise ValueError("RESPONSE_DATA is empty. Call send_request() first.")
        assert isinstance(self.RESPONSE_DATA, response_type), (
            f'Should be "{response_type.__name__}", '
            f'but got "{type(self.RESPONSE_DATA).__name__}"'
        )
