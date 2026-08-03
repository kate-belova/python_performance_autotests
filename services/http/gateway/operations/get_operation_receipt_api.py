import httpx

from schemas.operations_schemas import OperationReceiptResponseSchema
from services.http.gateway.operations.operations_api import OperationsGatewayAPI


class GetOperationReceiptGatewayAPI(OperationsGatewayAPI):
    def __init__(self, client: httpx.Client | None = None):
        super().__init__(client)
        self.PATH = "/operation-receipt"
        self.GET_OPERATION_RECEIPT_PATH_NAME = (
            self.OPERATIONS_PATH_NAME + self.PATH + "/{operation_id}"
        )

    def send_request(self, operation_id: str):
        extensions = {"path_name": self.GET_OPERATION_RECEIPT_PATH_NAME}
        response = self.CLIENT.get(
            f"{self.OPERATIONS_API}{self.PATH}/{operation_id}",
            extensions=extensions,
        )

        content_type = response.headers.get("content-type", "")
        if "application/json" in content_type:
            self.RESPONSE_DATA = OperationReceiptResponseSchema(**response.json())
