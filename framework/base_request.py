from .models import ResponseModel
from .constants import Configuration
from .requests import ShellRequestAPI


class BaseRequest:
    URL = Configuration.URL

    def __init__(self):
        self.url = self.URL
        self.request_api = ShellRequestAPI()

    @staticmethod
    def get_response_model(response):
        return ResponseModel(status=response.status_code, response=response.json(), url=response.url)
