import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')

class TestCustomerListFavMerchant:

    def test_merchant_favorite_normal(self):

        show_profile = requests.get(settings.url_fav_merchant_customer, headers=settings.header_with_token_customer)

        validate_status = show_profile.json().get('success')
        validate_message = show_profile.json().get('message')

        assert show_profile.status_code == 200
        assert validate_status == bool(True)
        assert 'Data merchant favorite berhasil ditemukan.' in validate_message

    def test_merchant_favorite_wrong_token(self):

        show_profile = requests.get(settings.url_fav_merchant_customer, headers=settings.header_wrong_token_customer)

        validate_status = show_profile.json().get('success')
        validate_message = show_profile.json().get('message')

        assert show_profile.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_merchant_favorite_token_empty_value(self):

        show_profile = requests.get(settings.url_fav_merchant_customer, headers=settings.header_wrong_token_customer)

        validate_status = show_profile.json().get('success')
        validate_message = show_profile.json().get('message')

        assert show_profile.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message
