import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerDiscoverMenu:

    def test_discovers_menu_normal(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long
        }
        discover = requests.get(settings.url_discover_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')
        validate_menu_kategori = len(discover.json().get('data')['menu_categories'])
        validate_data = discover.json().get('data')

        assert discover.status_code == 200
        assert validate_status == bool(True)
        assert 'Data discover berhasil ditemukan.' in validate_message
        assert validate_menu_kategori == 10
        assert_that(validate_data).contains('available_voucher', 'menu_categories', 'order_without_review',
                                            'nearby_menu', 'missed_menu', 'newest_menu', 'bestseller_menu',
                                            'nearby_merchant')

    def test_discovers_latitude_empty_value(self):
        param2 = {
            'latitude': '',
            'longitude': settings.long
        }
        discover = requests.get(settings.url_discover_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['latitude']

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'latitude tidak boleh kosong.' in validate_message

    def test_discovers_without_param_latitude(self):
        param2 = {
            # 'latitude': '',
            'longitude': settings.long
        }
        discover = requests.get(settings.url_discover_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['latitude']

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'latitude tidak boleh kosong.' in validate_message

    def test_discovers_longitude_empty_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': ''
        }
        discover = requests.get(settings.url_discover_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['longitude']

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'longitude tidak boleh kosong.' in validate_message

    def test_discovers_without_param_longitude(self):
        param2 = {
            'latitude': settings.lat,
            # 'longitude': ''
        }
        discover = requests.get(settings.url_discover_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['longitude']

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'longitude tidak boleh kosong.' in validate_message

    def test_discover_wrong_token(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long
        }
        discover = requests.get(settings.url_discover_customer, params=param2,
                                headers=settings.header_wrong_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')

        assert discover.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_discover_empty_token(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long
        }
        discover = requests.get(settings.url_discover_customer, params=param2,
                                headers=settings.header_without_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')

        assert discover.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message
