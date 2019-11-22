# coding: utf-8

"""
    enable:Banking SDK

    Currently enable:Banking SDK consists of [authorization](#auth-api), [account information](#aisp-api) and [payment initiation](#pisp-api) APIs. The same calls and data structures are used for interacting with different banks. In order to use each of the APIs corresponding API instance needs to be created with bank specific settings.  enable:Banking SDK API is based on [STET PSD2 specification](https://www.stet.eu/en/psd2/).  This API intends to provide an interface for Third Party Providers (TPP) for accessing Account Servicing Payment Service Providers (ASPSP, i.e. banks).  TPP may act as Account Information Service Provider (AISP), Payment Initiation Service Providers (PISP) or both.  The Payment Service User (PSU) is the owner of the accounts held by the ASPSP and gives accreditations to the TPP in order to access his accounts information or initiates payment from these accounts.   # noqa: E501

    API version: 0.3.0
    Contact: hello@enablebanking.com
    Generated by enable:Banking SDK generator using Swagger Codegen project
"""


from __future__ import absolute_import

import unittest

import enablebanking
from enablebanking.api.meta_api import MetaApi  # noqa: E501
from enablebanking.rest import ApiException


class TestMetaApi(unittest.TestCase):
    """MetaApi unit test stubs"""

    def setUp(self):
        self.api = enablebanking.api.meta_api.MetaApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_connectors(self):
        """Test case for get_connectors

        Retrieval of the available connectors  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
