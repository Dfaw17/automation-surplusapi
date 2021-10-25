import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')

class TestCustomerBanner:

    def test_banner_normal(self):

        banner = requests.get(settings.url_banner_customer, headers=settings.header_with_token_customer)
        validate_status = banner.json().get('success')
        validate_message = banner.json().get('message')

        assert banner.status_code == 200
        assert validate_status == bool(True)
        assert 'Data banner berhasil ditemukan.' in validate_message