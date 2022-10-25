# coding=utf-8
from ..framework.logger import Logger

from .schemas.schema_search import ResponseSearch
from .schemas.schema_reverse import ResponseReverse
import pytest
from ..framework.constants import StatusCode
from ..configurations.data_for_tests import DataSearch, DataReverse
from .api.search import Search
from .api.reverse import Reverse

from pydantic import ValidationError


class TestTask3:

    @pytest.mark.skip
    @pytest.mark.parametrize("data", DataSearch.DATA)
    def test_request_to_get_list_of_search_and_check_on_model(self, data):
        response = Search().get_response_search(data)
        assert response.status == StatusCode.STATUS_200, \
            f"Server response is {response.status}, expected result is {StatusCode.STATUS_200}"
        Logger.info(f"url = {response.url}")
        Logger.info(f"{type(response.response)}")
        Logger.info(f"JSON = {response.response}")

        try:
            q = ResponseSearch(response_model=response.response)
            Logger.info(f"Model = {q.json()}")
        except ValidationError as e:
            print(e)
            # print(e.json())

    @pytest.mark.need_review
    @pytest.mark.parametrize("data", DataReverse.DATA)
    def test_request_to_get_reverse(self, data):
        response = Reverse().get_response_reverse(data)
        assert response.status == StatusCode.STATUS_200, \
            f"Server response is {response.status}, expected result is {StatusCode.STATUS_200}"
        Logger.info(f"url = {response.url}")
        Logger.info(f"{type(response.response)}")
        Logger.info(f"JSON = {response.response}")

        try:
            q = ResponseReverse(**response.response)
            Logger.info(f"Model = {q.json()}")
        except ValidationError as e:
            print(e)
            # print(e.json())
