import httpx
from locust import task, User, between

from locust_settings.http.http_gateway_tasksets import GatewayHTTPSequentialTaskSet
from locust_settings.user import LocustBaseUser


class GetDocumentsSequentialTaskSet(GatewayHTTPSequentialTaskSet):
    user_id: str | None = None
    account_id: str | None = None

    @task
    def create_user(self):
        try:
            self.create_user_client.send_request()
            self.user_id = self.create_user_client.USER_ID
        except httpx.RequestError:
            pass

    @task
    def open_savings_account(self):
        if self.user_id is None:
            return

        try:
            self.open_savings_account_client.send_request(user_id=self.user_id)
            self.account_id = self.open_savings_account_client.account_id
        except httpx.RequestError:
            pass

    @task
    def get_documents(self):
        if self.account_id is None:
            return

        try:
            self.get_tariff_document_client.send_request(account_id=self.account_id)
            self.get_contract_document_client.send_request(
                account_id=self.account_id
            )
        except httpx.RequestError:
            pass


class GetDocumentsUser(LocustBaseUser):
    tasks = [GetDocumentsSequentialTaskSet]
