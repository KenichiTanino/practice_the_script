import os
from pathlib import Path
import sys

from vcr_unittest import VCRTestCase
import pytest

root_dir = Path(__file__).resolve().parent
sys.path.append( str(root_dir.parent) )

from lib.client import xmlrpc_client_hello, xmlrpc_client_time_result

class TestXMLRPC_Client(VCRTestCase):

    @pytest.mark.vcr()
    def test_client_hello(self):
        result = xmlrpc_client_hello()
        self.assertNotEqual(result, None)

    @pytest.mark.vcr()
    def test_client_time_result(self):
        result = xmlrpc_client_time_result()
        # self.assertNotEqual(result, None)
