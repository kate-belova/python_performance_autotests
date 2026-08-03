import logging
import os

import httpx
from dotenv import load_dotenv

from locust_settings.http_locust import (
    locust_request_event_hook,
    locust_response_event_hook,
)

load_dotenv()


def create_http_client(
    event_hooks: dict | None = None,
) -> httpx.Client:
    base_url = os.getenv("BASE_URL")

    if base_url is None:
        raise ValueError("BASE_URL is not set")

    return httpx.Client(
        base_url=base_url,
        timeout=10,
        event_hooks=event_hooks,
    )


def create_locust_http_client(environment) -> httpx.Client:
    logging.getLogger("httpx").setLevel(logging.WARNING)

    return create_http_client(
        event_hooks={
            "request": [locust_request_event_hook],
            "response": [locust_response_event_hook(environment)],
        }
    )
