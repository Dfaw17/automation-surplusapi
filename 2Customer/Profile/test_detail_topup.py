import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerDetailTopup:

    def test_get_detail_topup(self):
        detail_topup = requests.get(settings.url_detail_topup, headers=settings.header_with_token_customer)

        validate_status = detail_topup.json().get('success')

        assert detail_topup.status_code == 200
        assert validate_status == bool(True)

    def test_get_detail_topup_wrong_token(self):
        detail_topup = requests.get(settings.url_detail_topup, headers=settings.header_wrong_token_customer)

        validate_status = detail_topup.json().get('success')
        validate_message = detail_topup.json().get('message')

        assert detail_topup.status_code == 401
        assert validate_status == bool(False)
        assert_that(validate_message).is_equal_to("Unauthorized")

    def test_get_detail_topup_without_token(self):
        detail_topup = requests.get(settings.url_detail_topup, headers=settings.header_without_token_customer)

        validate_status = detail_topup.json().get('success')
        validate_message = detail_topup.json().get('message')

        assert detail_topup.status_code == 401
        assert validate_status == bool(False)
        assert_that(validate_message).is_equal_to("Unauthorized")
