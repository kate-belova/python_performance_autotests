import os

import grpc

# noinspection PyUnresolvedReferences
import grpc.experimental.gevent as grpc_gevent
from dotenv import load_dotenv
from grpc import Channel
from locust.env import Environment

from locust_settings.grpc_locust import LocustInterceptor

grpc_gevent.init_gevent()

load_dotenv()


def create_grpc_channel() -> Channel:
    return grpc.insecure_channel(str(os.getenv("HOST_PORT")))


def create_locust_grpc_channel(
    environment: Environment,
) -> Channel:
    interceptor = LocustInterceptor(environment)

    channel = create_grpc_channel()

    return grpc.intercept_channel(channel, interceptor)
