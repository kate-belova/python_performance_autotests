import os

from dotenv import load_dotenv

load_dotenv()


class BaseAPI:
    def __init__(self):
        self.BASE_API = os.getenv("BASE_URL")
        self.RESPONSE_DATA = None
