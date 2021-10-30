import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerOrdersShowVoucher:

    def test_show_voucher_normal(self):
        show_voucher = requests.get(
            settings.url_show_voucher_customer + str(settings.var_list_voucher_customer().json().get('data')[0]['id']),
            headers=settings.header_with_token_customer)

        validate_status = show_voucher.json().get('success')
        validate_message = show_voucher.json().get('message')
        validate_data = show_voucher.json().get('data')

        assert show_voucher.status_code == 200
        assert validate_status == bool(True)
        assert "Voucher berhasil ditemukan" in validate_message
        assert_that(validate_data).contains('id', 'title', 'description', 'code', 'percentage',
                                            'fixed_discount',
                                            'min_purchase', 'max_discount', 'max_usage', 'max_user',
                                            'total_usage',
                                            'total_user', 'is_specific_user', 'start_at', 'end_at', 'duration',
                                            'custom_time', 'tos', 'guide', 'type_id', 'target_id', 'image',
                                            'created_at', 'updated_at', 'deleted_at', 'expired_at')

    def test_show_voucher_wrong_token(self):
        show_voucher = requests.get(
            settings.url_show_voucher_customer + str(settings.var_list_voucher_customer().json().get('data')[0]['id']),
            headers=settings.header_wrong_token_customer)

        validate_status = show_voucher.json().get('success')
        validate_message = show_voucher.json().get('message')

        assert show_voucher.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message

    def test_show_voucher_token_empty_value(self):
        show_voucher = requests.get(
            settings.url_show_voucher_customer + str(settings.var_list_voucher_customer().json().get('data')[0]['id']),
            headers=settings.header_without_token_customer)

        validate_status = show_voucher.json().get('success')
        validate_message = show_voucher.json().get('message')

        assert show_voucher.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message

    def test_show_voucher_id_not_found(self):
        show_voucher = requests.get(
            settings.url_show_voucher_customer + '999999', headers=settings.header_with_token_customer)

        validate_status = show_voucher.json().get('success')
        validate_message = show_voucher.json().get('message')

        assert show_voucher.status_code == 404
        assert validate_status == bool(False)
        assert "Voucher tidak ditemukan" in validate_message

    def test_show_vouchet_id_text_value(self):
        show_voucher = requests.get(
            settings.url_show_voucher_customer + 'aaa', headers=settings.header_with_token_customer)

        validate_status = show_voucher.json().get('success')
        validate_message = show_voucher.json().get('message')

        assert show_voucher.status_code == 404
        assert validate_status == bool(False)
        assert "Voucher tidak ditemukan" in validate_message

    def test_show_voucher_id_empty_value(self):
        show_voucher = requests.get(
            settings.url_show_voucher_customer + '', headers=settings.header_with_token_customer)

        validate_status = show_voucher.json().get('success')
        validate_message = show_voucher.json().get('message')

        assert show_voucher.status_code == 200
        assert validate_status == bool(True)
        assert "Voucher berhasil ditemukan" in validate_message
