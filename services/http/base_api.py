import httpx

from services.http.client import create_http_client


class BaseAPI:
    def __init__(self, client: httpx.Client | None = None):
        self.CLIENT = client or create_http_client()
        self.RESPONSE_DATA = None
