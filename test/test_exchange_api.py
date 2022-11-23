# coding: utf-8

"""
    Kalshi Trade API

    This documentation describes Kalshi's trading API (known as Trade API v2). By using this API, you agree to Kalshi's Developer Agreement (https://kalshi.com/developer-agreement).  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: support@kalshi.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import kalshi_python
from kalshi_python.api.exchange_api import ExchangeApi  # noqa: E501
from kalshi_python.rest import ApiException


class TestExchangeApi(unittest.TestCase):
    """ExchangeApi unit test stubs"""

    def setUp(self):
        self.api = ExchangeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_exchange_status(self):
        """Test case for get_exchange_status

        Endpoint for getting the exchange status.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()