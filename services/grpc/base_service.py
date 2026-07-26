import os

import grpc

# noinspection PyUnresolvedReferences
import grpc.experimental.gevent as grpc_gevent
from dotenv import load_dotenv

grpc_gevent.init_gevent()

load_dotenv()


class BaseService:
    def __init__(self):
        self.CHANNEL = grpc.insecure_channel(str(os.getenv("HOST_PORT")))
        self.RESPONSE_DATA = None

    def check_response_type(self, response_type):
        if self.RESPONSE_DATA is None:
            raise ValueError("RESPONSE_DATA is empty. Call send_request() first.")
        assert isinstance(self.RESPONSE_DATA, response_type), (
            f'Should be "{response_type.__name__}", '
            f'but got "{type(self.RESPONSE_DATA).__name__}"'
        )
