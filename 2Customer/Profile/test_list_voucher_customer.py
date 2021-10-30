import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerListVoucher:

    def test_list_voucher_normal(self):
        show_profile = requests.get(settings.url_list_voucher_customer, headers=settings.header_with_token_customer)

        validate_status = show_profile.json().get('success')
        validate_message = show_profile.json().get('message')
        validate_voucher_surplus = show_profile.json().get('data')['voucher_surplus'][0]

        assert show_profile.status_code == 200
        assert validate_status == bool(True)
        assert 'Voucher berhasil ditemukan' in validate_message
        assert_that(validate_voucher_surplus).contains('id', 'title', 'description', 'code', 'percentage',
                                                       'fixed_discount', 'min_purchase', 'max_discount', 'max_usage', 'max_user')

    def test_list_voucher_wrong_token(self):
        show_profile = requests.get(settings.url_list_voucher_customer, headers=settings.header_wrong_token_customer)

        validate_status = show_profile.json().get('success')
        validate_message = show_profile.json().get('message')

        assert show_profile.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_list_voucher_token_empty_value(self):
        show_profile = requests.get(settings.url_list_voucher_customer, headers=settings.header_without_token_customer)

        validate_status = show_profile.json().get('success')
        validate_message = show_profile.json().get('message')

        assert show_profile.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message
