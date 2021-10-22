import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')

class TestCustomerLikeMerchant:

    def test_like_merchant_normal(self):
        like_merchants = requests.patch(settings.url_like_merchant_customer + str(
            settings.var_list_menu_discover().json().get('data')['nearby_merchant'][0]['merchant_id']) + '/like',
                                        headers=settings.header_with_token_customer)

        validate_status = like_merchants.json().get('success')
        validate_message = like_merchants.json().get('message')

        assert like_merchants.status_code == 200
        assert validate_status == bool(True)
        assert 'disukai' in validate_message

    def test_unlike_merchant_normal(self):
        like_merchants = requests.patch(settings.url_like_merchant_customer + str(
            settings.var_list_menu_discover().json().get('data')['nearby_merchant'][0]['merchant_id']) + '/like',
                                        headers=settings.header_with_token_customer)

        validate_status = like_merchants.json().get('success')
        validate_message = like_merchants.json().get('message')

        assert like_merchants.status_code == 200
        assert validate_status == bool(True)
        assert 'disukai' in validate_message

    def test_like_merchant_without_token(self):
        like_merchants = requests.patch(settings.url_like_merchant_customer + str(
            settings.var_list_menu_discover().json().get('data')['nearby_merchant'][0]['merchant_id']) + '/like',
                                        headers=settings.header_without_token_customer)

        validate_status = like_merchants.json().get('success')
        validate_message = like_merchants.json().get('message')

        assert like_merchants.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_like_merchant_wrong_token(self):
        like_merchants = requests.patch(settings.url_like_merchant_customer + str(
            settings.var_list_menu_discover().json().get('data')['nearby_merchant'][0]['merchant_id']) + '/like',
                                        headers=settings.header_wrong_token_customer)

        validate_status = like_merchants.json().get('success')
        validate_message = like_merchants.json().get('message')

        assert like_merchants.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_like_merchant_id_not_found(self):
        like_merchants = requests.patch(settings.url_like_merchant_customer + '9999' + '/like',
                                        headers=settings.header_with_token_customer)

        validate_status = like_merchants.json().get('success')
        validate_message = like_merchants.json().get('message')

        assert like_merchants.status_code == 200
        assert validate_status == bool(True)
        assert 'disukai' in validate_message

    def test_like_merchant_id_empty_value(self):
        like_merchants = requests.patch(settings.url_like_merchant_customer + '/like',
                                        headers=settings.header_with_token_customer)

        validate_status = like_merchants.json().get('success')
        validate_message = like_merchants.json().get('message')

        assert like_merchants.status_code == 404
        assert validate_status == bool(False)

    def test_like_merchant_id_minus_value(self):
        like_merchants = requests.patch(settings.url_like_merchant_customer+ '-999' + '/like',
                                        headers=settings.header_with_token_customer)

        validate_status = like_merchants.json().get('success')
        validate_message = like_merchants.json().get('message')

        assert like_merchants.status_code == 500
        assert validate_status == bool(False)
        assert 'Aduh!' in validate_message

    def test_like_merchant_id_text_value(self):
        like_merchants = requests.patch(settings.url_like_merchant_customer+ 'aaa' + '/like',
                                        headers=settings.header_with_token_customer)

        validate_status = like_merchants.json().get('success')
        validate_message = like_merchants.json().get('message')

        assert like_merchants.status_code == 500
        assert validate_status == bool(False)
        assert 'Aduh!' in validate_message
