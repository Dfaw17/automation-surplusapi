import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerListMerchant:

    def test_list_merchant_normal(self):
        param2 = {
            'latitude': '-6.3823317',
            'longitude': '107.1162607'
        }
        list_merchant = requests.get(settings.url_list_merchant_customer, params=param2,
                                     headers=settings.header_with_token_customer)

        validate_status = list_merchant.json().get('success')
        validate_message = list_merchant.json().get('message')
        validate_data = list_merchant.json().get('data')[0]
        validate_merchant_id = list_merchant.json().get('data')[0]['merchant_id']
        validate_nama_merchant = list_merchant.json().get('data')[0]['nama_merchant']

        assert list_merchant.status_code == 200
        assert validate_status == bool(True)
        assert 'Data merchant berhasil ditemukan.' in validate_message
        assert_that(validate_data).contains('merchant_id', 'nama_merchant', 'merchant_logo',
                                            'merchant_branch_status', 'merchant_central_id', 'distance',
                                            'merchant_verified')
        assert_that(validate_merchant_id).is_not_none()
        assert_that(validate_nama_merchant).is_not_none()

    def test_list_merchant_wrong_token(self):
        param2 = {
            'latitude': '-6.3823317',
            'longitude': '107.1162607'
        }
        list_merchant = requests.get(settings.url_list_merchant_customer, params=param2,
                                     headers=settings.header_wrong_token_customer)

        validate_status = list_merchant.json().get('success')
        validate_message = list_merchant.json().get('message')

        assert list_merchant.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_list_merchant_token_empty_value(self):
        param2 = {
            'latitude': '-6.3823317',
            'longitude': '107.1162607'
        }
        list_merchant = requests.get(settings.url_list_merchant_customer, params=param2,
                                     headers=settings.header_without_token_customer)

        validate_status = list_merchant.json().get('success')
        validate_message = list_merchant.json().get('message')

        assert list_merchant.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_list_merchant_latitude_empty_value(self):
        param2 = {
            'latitude': '',
            'longitude': '107.1162607'
        }
        list_merchant = requests.get(settings.url_list_merchant_customer, params=param2,
                                     headers=settings.header_with_token_customer)

        validate_status = list_merchant.json().get('success')
        validate_message = list_merchant.json().get('message')['latitude']

        assert list_merchant.status_code == 422
        assert validate_status == bool(False)
        assert 'latitude tidak boleh kosong.' in validate_message

    def test_list_merchant_without_param_latitude(self):
        param2 = {
            # 'latitude': '',
            'longitude': '107.1162607'
        }
        list_merchant = requests.get(settings.url_list_merchant_customer, params=param2,
                                     headers=settings.header_with_token_customer)

        validate_status = list_merchant.json().get('success')
        validate_message = list_merchant.json().get('message')['latitude']

        assert list_merchant.status_code == 422
        assert validate_status == bool(False)
        assert 'latitude tidak boleh kosong.' in validate_message

    def test_list_merchant_latitude_text_value(self):
        param2 = {
            'latitude': 'aaa',
            'longitude': '107.1162607'
        }
        list_merchant = requests.get(settings.url_list_merchant_customer, params=param2,
                                     headers=settings.header_with_token_customer)

        validate_status = list_merchant.json().get('success')
        validate_message = list_merchant.json().get('message')

        assert list_merchant.status_code == 500
        assert validate_status == bool(False)
        assert 'Aduh!' in validate_message

    def test_list_merchant_longitude_empty_value(self):
        param2 = {
            'latitude': '-6.3823317',
            'longitude': ''
        }
        list_merchant = requests.get(settings.url_list_merchant_customer, params=param2,
                                     headers=settings.header_with_token_customer)

        validate_status = list_merchant.json().get('success')
        validate_message = list_merchant.json().get('message')['longitude']

        assert list_merchant.status_code == 422
        assert validate_status == bool(False)
        assert 'longitude tidak boleh kosong.' in validate_message

    def test_list_merchant_without_param_longitude(self):
        param2 = {
            'latitude': '-6.3823317',
            'longitude': ''
        }
        list_merchant = requests.get(settings.url_list_merchant_customer, params=param2,
                                     headers=settings.header_with_token_customer)

        validate_status = list_merchant.json().get('success')
        validate_message = list_merchant.json().get('message')['longitude']

        assert list_merchant.status_code == 422
        assert validate_status == bool(False)
        assert 'longitude tidak boleh kosong.' in validate_message

    def test_list_merchant_longitude_text_value(self):
        param2 = {
            'latitude': '-6.3823317',
            'longitude': 'aaa'
        }
        list_merchant = requests.get(settings.url_list_merchant_customer, params=param2,
                                     headers=settings.header_with_token_customer)

        validate_status = list_merchant.json().get('success')
        validate_message = list_merchant.json().get('message')

        assert list_merchant.status_code == 500
        assert validate_status == bool(False)
        assert 'Aduh!' in validate_message