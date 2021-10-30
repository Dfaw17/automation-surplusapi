import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerOrdersIndexVoucher:

    def test_index_voucher_normal(self):
        voucher = requests.get(settings.url_index_voucher_customer, headers=settings.header_with_token_customer)

        validate_status = voucher.json().get('success')
        validate_message = voucher.json().get('message')
        validate_data = voucher.json().get('data')

        assert voucher.status_code == 200
        assert validate_status == bool(True)
        assert "Voucher berhasil ditemukan" in validate_message
        assert_that(validate_data['voucher_surplus'][0]).contains('id', 'title', 'description', 'code', 'percentage',
                                                                  'fixed_discount',
                                                                  'min_purchase', 'max_discount', 'max_usage',
                                                                  'max_user',
                                                                  'total_usage',
                                                                  'total_user', 'is_specific_user', 'start_at',
                                                                  'end_at', 'duration',
                                                                  'custom_time', 'tos', 'guide', 'type_id', 'target_id',
                                                                  'image',
                                                                  'created_at', 'updated_at', 'deleted_at')

    def test_index_voucher_wrong_token(self):
        voucher = requests.get(settings.url_index_voucher_customer, headers=settings.header_wrong_token_customer)

        validate_status = voucher.json().get('success')
        validate_message = voucher.json().get('message')

        assert voucher.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message

    def test_index_voucher_token_empty_value(self):
        voucher = requests.get(settings.url_index_voucher_customer, headers=settings.header_without_token_customer)

        validate_status = voucher.json().get('success')
        validate_message = voucher.json().get('message')

        assert voucher.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message
