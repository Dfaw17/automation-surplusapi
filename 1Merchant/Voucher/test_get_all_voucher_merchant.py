import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestGetAllVoucherMerchant:

    def test_get_all_voucehr_merchant(self):
        response = requests.get(settings.url_get_voucher_central_merchant, headers=settings.header_branch)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')
        validate_data = data.get('data')

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert_that(validate_message).is_equal_to('Data voucher central berhasil ditemukan.')
        assert_that(validate_data).is_not_none()

    def test_get_all_voucehr_merchant_token_empty(self):
        response = requests.get(settings.url_get_voucher_central_merchant, headers=settings.header_without_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 401
        assert validate_status == bool(False)
        assert_that(validate_message).is_equal_to('Unauthorized')

    def test_get_all_voucehr_merchant_token_wrong(self):
        response = requests.get(settings.url_get_voucher_central_merchant, headers=settings.header_wrong_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 401
        assert validate_status == bool(False)
        assert_that(validate_message).is_equal_to('Unauthorized')
