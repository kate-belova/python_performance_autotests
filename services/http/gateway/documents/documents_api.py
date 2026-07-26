from services.http.base_api import BaseAPI


class DocumentsGatewayAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.DOCUMENTS_API = f"{self.BASE_API}/documents"
