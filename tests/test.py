# coding=utf-8

import pytest
from ..framework.constants import StatusCode
from ..configurations.data_for_tests import DataSearch, DataReverse
from .api.search import Search
from .api.reverse import Reverse
from .utils.validations import Validations

from .schemas.schema_search import ResponseSchemaSearch
from .schemas.schema_reverse import ResponseSchemaReverse


class TestNominatimAPI:

    @pytest.mark.need_review
    @pytest.mark.parametrize("data", DataSearch.DATA_SEARCH)
    def test_request_to_get_list_of_search_and_check_on_model(self, data):
        response = Search().get_response_search(data)
        assert response.status == StatusCode.STATUS_200, \
            f"Server response is {response.status}, expected result is {StatusCode.STATUS_200}"
        assert Validations.validate_response(schema=ResponseSchemaSearch, response=response.response), \
            f"Server response contains invalid data"

    @pytest.mark.need_review
    @pytest.mark.parametrize("data", DataReverse.DATA_REVERSE)
    def test_request_to_get_reverse(self, data):
        response = Reverse().get_response_reverse(data)
        assert response.status == StatusCode.STATUS_200, \
            f"Server response is {response.status}, expected result is {StatusCode.STATUS_200}"
        assert Validations.validate_response(schema=ResponseSchemaReverse, response=[response.response]), \
            f"Server response contains invalid data"
