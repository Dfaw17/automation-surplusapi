import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestGetVoucher:

    def test_get_voucher_active(self):
        param = {
            "status": "1",
        }
        response = requests.get(settings.url_voucher_merchant, params=param,
                                headers=settings.header_with_token_merchant)

        data = response.json()
        validate_status = data.get('success')

        assert response.status_code == 200
        assert_that(validate_status).is_equal_to(bool(True))

    def test_get_voucher_pending(self):
        param = {
            "status": "2",
        }
        response = requests.get(settings.url_voucher_merchant, params=param,
                                headers=settings.header_with_token_merchant)

        data = response.json()
        validate_status = data.get('success')

        assert response.status_code == 200
        assert_that(validate_status).is_equal_to(bool(True))

    def test_get_voucher_history(self):
        param = {
            "status": "3",
        }
        response = requests.get(settings.url_voucher_merchant, params=param,
                                headers=settings.header_with_token_merchant)

        data = response.json()
        validate_status = data.get('success')

        assert response.status_code == 200
        assert_that(validate_status).is_equal_to(bool(True))

    def test_get_voucher_token_empty(self):
        param = {
            "status": "3",
        }
        response = requests.get(settings.url_voucher_merchant, params=param,
                                headers=settings.header_without_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 401
        assert_that(validate_status).is_equal_to(bool(False))
        assert_that(validate_message).is_equal_to('Unauthorized')

    def test_get_voucher_wrong_token(self):
        param = {
            "status": "3",
        }
        response = requests.get(settings.url_voucher_merchant, params=param,
                                headers=settings.header_wrong_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 401
        assert_that(validate_status).is_equal_to(bool(False))
        assert_that(validate_message).is_equal_to('Unauthorized')

    def test_get_voucher_status_empty(self):
        param = {
            "status": "",
        }
        response = requests.get(settings.url_voucher_merchant, params=param,
                                headers=settings.header_with_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['status']

        assert response.status_code == 422
        assert_that(validate_status).is_equal_to(bool(False))
        assert 'status tidak boleh kosong.' in validate_message
