import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')

class TestCustomerShowMerchant:

    def test_show_merchant_normal(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long
        }
        show_merchants = requests.get(settings.url_show_merchants_customer + str(settings.var_list_menu_discover().json().get('data')['nearby_merchant'][0]['merchant_id']),
                                 params=param2, headers=settings.header_with_token_customer)
        validate_status = show_merchants.json().get('success')
        validate_message = show_merchants.json().get('message')
        validate_id_merchant = show_merchants.json().get('data')['merchant']['id']
        validate_data_merchant = show_merchants.json().get('data')['merchant']
        validate_data_menus = show_merchants.json().get('data')['menus']
        validate_data_merchant_name = show_merchants.json().get('data')['merchant']['name']
        validate_data_merchant_email = show_merchants.json().get('data')['merchant']['email']
        validate_data_merchant_phone = show_merchants.json().get('data')['merchant']['no_ponsel']
        validate_data_merchant_alamat = show_merchants.json().get('data')['merchant']['alamat']
        validate_data_merchant_merchant_latitude = show_merchants.json().get('data')['merchant']['merchant_latitude']
        validate_data_merchant_merchant_longitude = show_merchants.json().get('data')['merchant']['merchant_longitude']

        assert show_merchants.status_code == 200
        assert validate_status == bool(True)
        assert 'Data merchant berhasil ditemukan.' in validate_message
        assert validate_id_merchant == settings.var_list_menu_discover().json().get('data')['nearby_merchant'][0]['merchant_id']
        assert_that(validate_data_merchant).contains('id', 'name', 'email', 'no_ponsel', 'alamat', 'rating',
                                                          'total_like', "total_review",
                                                          'logo_url', 'merchant_latitude', 'merchant_longitude',
                                                          'distance', "merchant_branch_status", "merchant_central_id",
                                                          'isLike', "merchant_verified", "merchant_category")
        assert_that(validate_data_menus).contains_only('ready_stock', 'preorder')
        assert_that([validate_data_merchant_name, validate_data_merchant_email, validate_data_merchant_phone,
                     validate_data_merchant_alamat, validate_data_merchant_merchant_latitude,
                     validate_data_merchant_merchant_longitude]).is_not_empty()

    def test_show_merchant_token_empty_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long
        }
        show_merchants = requests.get(settings.url_show_merchants_customer + str(settings.var_list_menu_discover().json().get('data')['nearby_merchant'][0]['merchant_id']),
                                 params=param2, headers=settings.header_without_token_customer)

        validate_status = show_merchants.json().get('success')
        validate_message = show_merchants.json().get('message')

        assert show_merchants.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_show_merchant_wrong_token(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long
        }
        show_merchants = requests.get(settings.url_show_merchants_customer + str(settings.var_list_menu_discover().json().get('data')['nearby_merchant'][0]['merchant_id']),
                                 params=param2, headers=settings.header_wrong_token_customer)

        validate_status = show_merchants.json().get('success')
        validate_message = show_merchants.json().get('message')

        assert show_merchants.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_show_merchant_latitude_empty_value(self):
        param2 = {
            'latitude': '',
            'longitude': settings.long
        }
        show_merchants = requests.get(settings.url_show_merchants_customer + str(settings.var_list_menu_discover().json().get('data')['nearby_merchant'][0]['merchant_id']),
                                 params=param2, headers=settings.header_with_token_customer)

        validate_status = show_merchants.json().get('success')
        validate_message = show_merchants.json().get('message')['latitude']

        assert show_merchants.status_code == 422
        assert validate_status == bool(False)
        assert 'latitude tidak boleh kosong.' in validate_message

    def test_show_merchant_without_param_latitude(self):
        param2 = {
            # 'latitude': '',
            'longitude': settings.long
        }
        show_merchants = requests.get(settings.url_show_merchants_customer + str(settings.var_list_menu_discover().json().get('data')['nearby_merchant'][0]['merchant_id']),
                                 params=param2, headers=settings.header_with_token_customer)

        validate_status = show_merchants.json().get('success')
        validate_message = show_merchants.json().get('message')['latitude']

        assert show_merchants.status_code == 422
        assert validate_status == bool(False)
        assert 'latitude tidak boleh kosong.' in validate_message

    def test_show_merchant_latitude_text_value(self):
        param2 = {
            'latitude': 'aaa',
            'longitude': settings.long
        }
        show_merchants = requests.get(settings.url_show_merchants_customer + str(settings.var_list_menu_discover().json().get('data')['nearby_merchant'][0]['merchant_id']),
                                 params=param2, headers=settings.header_with_token_customer)

        validate_status = show_merchants.json().get('success')
        validate_message = show_merchants.json().get('message')

        assert show_merchants.status_code == 500
        assert validate_status == bool(False)
        assert 'Aduh!' in validate_message

    def test_show_merchant_without_param_longitude(self):
        param2 = {
            'latitude': settings.lat,
            # 'longitude': settings.long
        }
        show_merchants = requests.get(settings.url_show_merchants_customer + str(settings.var_list_menu_discover().json().get('data')['nearby_merchant'][0]['merchant_id']),
                                 params=param2, headers=settings.header_with_token_customer)

        validate_status = show_merchants.json().get('success')
        validate_message = show_merchants.json().get('message')['longitude']

        assert show_merchants.status_code == 422
        assert validate_status == bool(False)
        assert 'longitude tidak boleh kosong.' in validate_message

    def test_show_merchant_longitude_empty_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': ''
        }
        show_merchants = requests.get(settings.url_show_merchants_customer + str(settings.var_list_menu_discover().json().get('data')['nearby_merchant'][0]['merchant_id']),
                                 params=param2, headers=settings.header_with_token_customer)

        validate_status = show_merchants.json().get('success')
        validate_message = show_merchants.json().get('message')['longitude']

        assert show_merchants.status_code == 422
        assert validate_status == bool(False)
        assert 'longitude tidak boleh kosong.' in validate_message

    def test_show_merchant_longitude_text_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': 'aaa'
        }
        show_merchants = requests.get(settings.url_show_merchants_customer + str(settings.var_list_menu_discover().json().get('data')['nearby_merchant'][0]['merchant_id']),
                                 params=param2, headers=settings.header_with_token_customer)

        validate_status = show_merchants.json().get('success')
        validate_message = show_merchants.json().get('message')

        assert show_merchants.status_code == 500
        assert validate_status == bool(False)
        assert 'Aduh!' in validate_message

    def test_show_merchant_id_menu_not_found(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long
        }
        show_merchants = requests.get(settings.url_show_merchants_customer + '666',params=param2, headers=settings.header_with_token_customer)

        validate_status = show_merchants.json().get('success')
        validate_message = show_merchants.json().get('message')

        assert show_merchants.status_code == 404
        assert validate_status == bool(False)
        assert 'Merchant tidak ditemukan' in validate_message

    def test_show_merchant_without_id_menu(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long
        }
        show_merchants = requests.get(settings.url_show_merchants_customer,params=param2, headers=settings.header_with_token_customer)

        validate_status = show_merchants.json().get('success')
        validate_message = show_merchants.json().get('message')

        assert show_merchants.status_code == 200
        assert validate_status == bool(True)
        assert 'Data merchant berhasil ditemukan.' in validate_message

    def test_show_merchant_id_menu_text_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long
        }
        show_merchants = requests.get(settings.url_show_merchants_customer + 'aaa',params=param2, headers=settings.header_with_token_customer)

        validate_status = show_merchants.json().get('success')
        validate_message = show_merchants.json().get('message')

        assert show_merchants.status_code == 404
        assert validate_status == bool(False)
        assert 'Merchant tidak ditemukan' in validate_message