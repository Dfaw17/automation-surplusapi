import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')

class TestCustomerShowMenu:

    def test_show_menu_normal(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long
        }
        show_menu = requests.get(settings.url_show_menu_customer + str(settings.var_list_menu_discover().json().get('data')['nearby_menu'][0]['stock_id']),
                                 params=param2, headers=settings.header_with_token_customer)

        validate_status = show_menu.json().get('success')
        validate_message = show_menu.json().get('message')
        validate_data_menu = show_menu.json().get('data')['stock_id']
        validate_merchant_id = show_menu.json().get('data')['merchant_id']
        validate_nama_menu_makanan = show_menu.json().get('data')['nama_menu_makanan']
        validate_merchant_kategori_makanan_id = show_menu.json().get('data')['merchant_kategori_makanan_id']

        assert validate_status == bool(True)
        assert 'Data menu berhasil ditemukan.' in validate_message
        assert show_menu.status_code == 200
        assert_that([validate_data_menu, validate_nama_menu_makanan, validate_merchant_kategori_makanan_id,
                     validate_merchant_id]).is_not_empty()

    def test_show_menu_without_token(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long
        }
        show_menu = requests.get(settings.url_show_menu_customer + str(settings.var_list_menu_discover().json().get('data')['nearby_menu'][0]['stock_id']),
                                 params=param2, headers=settings.header_without_token_customer)

        validate_status = show_menu.json().get('success')
        validate_message = show_menu.json().get('message')
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message
        assert show_menu.status_code == 401

    def test_show_menu_wrong_token(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long
        }
        show_menu = requests.get(settings.url_show_menu_customer + str(settings.var_list_menu_discover().json().get('data')['nearby_menu'][0]['stock_id']),
                                 params=param2, headers=settings.header_wrong_token_customer)

        validate_status = show_menu.json().get('success')
        validate_message = show_menu.json().get('message')
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message
        assert show_menu.status_code == 401

    def test_show_menu_latitude_empty_value(self):
        param2 = {
            'latitude': '',
            'longitude': settings.long
        }
        show_menu = requests.get(settings.url_show_menu_customer + str(settings.var_list_menu_discover().json().get('data')['nearby_menu'][0]['stock_id']),
                                 params=param2, headers=settings.header_with_token_customer)

        validate_status = show_menu.json().get('success')
        validate_message = show_menu.json().get('message')['latitude']
        assert validate_status == bool(False)
        assert 'latitude tidak boleh kosong.' in validate_message
        assert show_menu.status_code == 422

    def test_show_menu_latitude_text_value(self):
        param2 = {
            'latitude': 'aaa',
            'longitude': settings.long
        }
        show_menu = requests.get(settings.url_show_menu_customer + str(settings.var_list_menu_discover().json().get('data')['nearby_menu'][0]['stock_id']),
                                 params=param2, headers=settings.header_with_token_customer)

        validate_status = show_menu.json().get('success')
        validate_message = show_menu.json().get('message')
        assert validate_status == bool(False)
        assert 'Aduh!' in validate_message
        assert show_menu.status_code == 500

    def test_show_menu_without_param_latitude(self):
        param2 = {
            # 'latitude': 'aaa',
            'longitude': settings.long
        }
        show_menu = requests.get(settings.url_show_menu_customer + str(settings.var_list_menu_discover().json().get('data')['nearby_menu'][0]['stock_id']),
                                 params=param2, headers=settings.header_with_token_customer)

        validate_status = show_menu.json().get('success')
        validate_message = show_menu.json().get('message')['latitude']

        assert validate_status == bool(False)
        assert 'latitude tidak boleh kosong.' in validate_message
        assert show_menu.status_code == 422

    def test_show_menu_longitude_empty_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': ''
        }
        show_menu = requests.get(settings.url_show_menu_customer + str(settings.var_list_menu_discover().json().get('data')['nearby_menu'][0]['stock_id']),
                                 params=param2, headers=settings.header_with_token_customer)

        validate_status = show_menu.json().get('success')
        validate_message = show_menu.json().get('message')['longitude']
        assert validate_status == bool(False)
        assert 'longitude tidak boleh kosong.' in validate_message
        assert show_menu.status_code == 422

    def test_show_menu_longitude_text_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': 'aaa'
        }
        show_menu = requests.get(settings.url_show_menu_customer + str(settings.var_list_menu_discover().json().get('data')['nearby_menu'][0]['stock_id']),
                                 params=param2, headers=settings.header_with_token_customer)

        validate_status = show_menu.json().get('success')
        validate_message = show_menu.json().get('message')
        assert validate_status == bool(False)
        assert 'Aduh!' in validate_message
        assert show_menu.status_code == 500

    def test_show_menu_without_param_longitude(self):
        param2 = {
            'latitude': settings.lat,
            # 'longitude': 'aaa'
        }
        show_menu = requests.get(settings.url_show_menu_customer + str(settings.var_list_menu_discover().json().get('data')['nearby_menu'][0]['stock_id']),
                                 params=param2, headers=settings.header_with_token_customer)

        validate_status = show_menu.json().get('success')
        validate_message = show_menu.json().get('message')['longitude']

        assert validate_status == bool(False)
        assert 'longitude tidak boleh kosong.' in validate_message
        assert show_menu.status_code == 422

    def test_show_menu_id_menu_not_found(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long
        }
        show_menu = requests.get(settings.url_show_menu_customer + '99999',
                                 params=param2, headers=settings.header_with_token_customer)

        validate_status = show_menu.json().get('success')
        validate_message = show_menu.json().get('message')

        assert show_menu.status_code == 404
        assert validate_status == bool(False)
        assert 'Data menu tidak ditemukan' in validate_message

    def test_show_menu_without_id_menu(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long
        }
        show_menu = requests.get(settings.url_show_menu_customer ,params=param2, headers=settings.header_with_token_customer)

        validate_status = show_menu.json().get('success')
        validate_message = show_menu.json().get('message')['type']

        assert show_menu.status_code == 422
        assert validate_status == bool(False)
        assert 'type tidak boleh kosong.' in validate_message

    def test_show_menu_id_menu_text_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long
        }
        show_menu = requests.get(settings.url_show_menu_customer + 'aaa',
                                 params=param2, headers=settings.header_with_token_customer)

        validate_status = show_menu.json().get('success')
        validate_message = show_menu.json().get('message')

        assert show_menu.status_code == 404
        assert validate_status == bool(False)
        assert 'Data menu tidak ditemukan' in validate_message