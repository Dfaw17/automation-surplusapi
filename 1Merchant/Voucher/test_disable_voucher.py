import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestDisableVoucher:

    def test_disable_normal(self):
        response = requests.put(settings.url_voucher_merchant + '/162/disable',
                                headers=settings.header_with_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')
        validate_voucher_id = data.get('data')['id']
        validate_disable= data.get('data')['is_disabled']

        assert response.status_code == 200
        assert_that(validate_status).is_equal_to(bool(True))
        assert_that(validate_message).is_equal_to('Data voucher berhasil diubah.')
        assert_that(validate_voucher_id).is_equal_to(162)
        assert_that(validate_disable).is_equal_to(bool(True))

    def test_disable_token_empty(self):
        response = requests.put(settings.url_voucher_merchant + '/181/disable',
                                headers=settings.header_without_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 401
        assert_that(validate_status).is_equal_to(bool(False))
        assert_that(validate_message).is_equal_to('Unauthorized')

    def test_disable_token_wrong(self):
        response = requests.put(settings.url_voucher_merchant + '/181/disable',
                                headers=settings.header_wrong_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 401
        assert_that(validate_status).is_equal_to(bool(False))
        assert_that(validate_message).is_equal_to('Unauthorized')

    def test_disable_wrong_id(self):
        response = requests.put(settings.url_voucher_merchant + '/99999/disable' ,headers=settings.header_with_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        # assert response.status_code == 200
        assert_that(validate_status).is_equal_to(bool(False))
        assert_that(validate_message).is_equal_to('Data voucher tidak ditemukan.')
