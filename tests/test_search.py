from unittest import TestCase

from CreApiUtils.ApiUtils import ApiUtils 

class TestUtils(TestCase):
    def test_simple_utils(self):
        au = ApiUtils()
        self.assertEqual('gut', 'gut')

