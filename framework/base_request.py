from protei_testing_api_nominatim.framework.models import ResponseModel
from protei_testing_api_nominatim.framework.constants import Configuration
from protei_testing_api_nominatim.framework.requests import ShellRequestAPI


class BaseRequest:
    URL = Configuration.URL

    def __init__(self):
        self.url = self.URL
        self.request_api = ShellRequestAPI()

    @staticmethod
    def get_response_model(response):
        return ResponseModel(status=response.status_code, response=response.json(), url=response.url)
