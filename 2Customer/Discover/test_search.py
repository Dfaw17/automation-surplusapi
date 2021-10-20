import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerSearchMenu:

    def test_search_normal(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')
        validate_data = discover.json().get('data')

        assert discover.status_code == 200
        assert validate_status == bool(True)
        assert 'Data pencarian berhasil ditemukan.' in validate_message
        assert_that(validate_data).contains_only('menus', 'merchants')

    def test_search_token_empty_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_without_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')

        assert discover.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_search_wrong_token(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_wrong_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')

        assert discover.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_search_latitude_empty_value(self):
        param2 = {
            'latitude': '',
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['latitude']

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'latitude tidak boleh kosong.' in validate_message

    def test_search_without_param_latitude(self):
        param2 = {
            # 'latitude': '',
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['latitude']

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'latitude tidak boleh kosong.' in validate_message

    def test_search_latitude_text_value(self):
        param2 = {
            'latitude': 'aaa',
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')

        assert discover.status_code == 500
        assert validate_status == bool(False)
        assert 'Aduh!' in validate_message

    def test_search_longitude_empty_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': '',
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['longitude']

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'longitude tidak boleh kosong.' in validate_message

    def test_search_longitude_text_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': 'aaa',
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')

        assert discover.status_code == 500
        assert validate_status == bool(False)
        assert 'Aduh! ' in validate_message

    def test_search_without_param_longitude(self):
        param2 = {
            'latitude': settings.lat,
            # 'longitude': 'aaa',
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['longitude']

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'longitude tidak boleh kosong.' in validate_message

    def test_search_missed_empty_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['missed']

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'Menu terlewat harus bernilai true atau false.' in validate_message

    def test_search_missed_text_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': 'aaa',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['missed']

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'Menu terlewat harus bernilai true atau false.' in validate_message

    def test_search_missed_not_bool_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '5',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['missed']

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'Menu terlewat harus bernilai true atau false.' in validate_message

    def test_search_without_param_missed(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            # 'missed': '5',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')
        validate_data = discover.json().get('data')

        assert discover.status_code == 200
        assert validate_status == bool(True)
        assert 'Data pencarian berhasil ditemukan.' in validate_message
        assert_that(validate_data).contains_only('menus', 'merchants')

    def test_search_menu_categories_empty_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['menu_categories.0']

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'menu_categories.0 harus berupa angka.' in validate_message

    def test_search_menu_categories_text_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': 'aaa',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['menu_categories.0']

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'menu_categories.0 harus berupa angka.' in validate_message

    def test_search_menu_categories_not_found_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '500',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')
        validate_data = discover.json().get('data')

        assert discover.status_code == 200
        assert validate_status == bool(True)
        assert 'Data pencarian berhasil ditemukan.' in validate_message
        assert_that(validate_data).contains_only('menus', 'merchants')

    def test_search_menu_categories_without_index(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories': '500',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['menu_categories']

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'Format Kategori Menu tidak benar.' in validate_message

    def test_search_without_param_menu_categories(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            # 'menu_categories[0]': '500',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')
        validate_data = discover.json().get('data')

        assert discover.status_code == 200
        assert validate_status == bool(True)
        assert 'Data pencarian berhasil ditemukan.' in validate_message
        assert_that(validate_data).contains_only('menus', 'merchants')

    def test_search_without_param_max_price(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            # 'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')
        validate_data = discover.json().get('data')

        assert discover.status_code == 200
        assert validate_status == bool(True)
        assert 'Data pencarian berhasil ditemukan' in validate_message
        assert_that(validate_data).contains_only('menus', 'merchants')

    def test_search_max_price_minus_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '-50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')
        validate_data = discover.json().get('data')

        assert discover.status_code == 200
        assert validate_status == bool(True)
        assert 'Data pencarian berhasil ditemukan' in validate_message
        assert_that(validate_data).contains_only('menus', 'merchants')

    def test_search_max_price_text_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': 'aaa',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['max_price']

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'Harga Maksimal harus berupa angka.' in validate_message

    def test_searh_max_price_empty(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')
        validate_data = discover.json().get('data')

        assert discover.status_code == 200
        assert validate_status == bool(True)
        assert 'Data pencarian berhasil ditemukan.' in validate_message
        assert_that(validate_data).contains_only('menus', 'merchants')

    def test_search_without_param_distance(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            # 'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')
        validate_data = discover.json().get('data')

        assert discover.status_code == 200
        assert validate_status == bool(True)
        assert 'Data pencarian berhasil ditemukan.' in validate_message
        assert_that(validate_data).contains_only('menus', 'merchants')

    def test_search_distance_minus_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '-10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['distance']

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'Jarak setidaknya harus 100.' in validate_message

    def test_search_distance_text_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': 'aaa',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['distance']

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'Jarak harus berupa angka.' in validate_message

    def test_search_distance_empty(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')
        validate_data = discover.json().get('data')

        assert discover.status_code == 200
        assert validate_status == bool(True)
        assert 'Data pencarian berhasil ditemukan.' in validate_message
        assert_that(validate_data).contains_only('menus', 'merchants')

    def test_search_without_param_preorder(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            # 'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')
        validate_data = discover.json().get('data')

        assert discover.status_code == 200
        assert validate_status == bool(True)
        assert 'Data pencarian berhasil ditemukan.' in validate_message
        assert_that(validate_data).contains_only('menus', 'merchants')

    def test_search_preorder_empty_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['preorder']
        validate_data = discover.json().get('data')

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'Menu Pre-order harus bernilai true atau false.' in validate_message

    def test_search_preorder_text_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': 'aaa',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['preorder']
        validate_data = discover.json().get('data')

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'Menu Pre-order harus bernilai true atau false.' in validate_message

    def test_search_preorder_not_bool_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '55',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['preorder']
        validate_data = discover.json().get('data')

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'Menu Pre-order harus bernilai true atau false.' in validate_message

    def test_search_without_param_pickup_time_start(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            # 'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')
        validate_data = discover.json().get('data')

        assert discover.status_code == 200
        assert validate_status == bool(True)
        assert 'Data pencarian berhasil ditemukan.' in validate_message
        assert_that(validate_data).contains_only('menus', 'merchants')

    def test_search_param_pickup_time_start_empty_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['pickup_time_start']

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'Waktu awal penjemputan tidak cocok dengan format H:i.' in validate_message

    def test_search_param_pickup_time_start_text_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': 'aaa',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['pickup_time_start']

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'Waktu awal penjemputan tidak cocok dengan format H:i.' in validate_message

    def test_search_param_pickup_time_start_not_time_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '12345',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['pickup_time_start']

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'Waktu awal penjemputan tidak cocok dengan format H:i.' in validate_message

    def test_search_param_pickup_time_start_am_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '7 AM',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['pickup_time_start']

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'Waktu awal penjemputan tidak cocok dengan format H:i.' in validate_message

    def test_search_without_param_pickup_time_end(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            # 'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')
        validate_data = discover.json().get('data')

        assert discover.status_code == 200
        assert validate_status == bool(True)
        assert 'Data pencarian berhasil ditemukan.' in validate_message
        assert_that(validate_data).contains_only('menus', 'merchants')

    def test_search_param_pickup_time_end_empty_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['pickup_time_end']

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'Waktu akhir penjemputan tidak cocok dengan format H:i.' in validate_message

    def test_search_param_pickup_time_end_text_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': 'aaa',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['pickup_time_end']

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'Waktu akhir penjemputan tidak cocok dengan format H:i.' in validate_message

    def test_search_param_pickup_time_end_not_time_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '123',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['pickup_time_end']

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'Waktu akhir penjemputan tidak cocok dengan format H:i.' in validate_message

    def test_search_param_pickup_time_end_am_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '9 PM',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['pickup_time_end']

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'Waktu akhir penjemputan tidak cocok dengan format H:i.' in validate_message

    def test_search_without_param_keyword(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            # 'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')
        validate_data = discover.json().get('data')

        assert discover.status_code == 200
        assert validate_status == bool(True)
        assert 'Data pencarian berhasil ditemukan.' in validate_message
        assert_that(validate_data).contains_only('menus', 'merchants')

    def test_search_keyword_empty_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')
        validate_data = discover.json().get('data')

        assert discover.status_code == 200
        assert validate_status == bool(True)
        assert 'Data pencarian berhasil ditemukan.' in validate_message
        assert_that(validate_data).contains_only('menus', 'merchants')

    def test_search_without_param_order_by(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            # 'order_by': 'nearby',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')
        validate_data = discover.json().get('data')

        assert discover.status_code == 200
        assert validate_status == bool(True)
        assert 'Data pencarian berhasil ditemukan.' in validate_message
        assert_that(validate_data).contains_only('menus', 'merchants')

    def test_search_order_by_empty_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': '',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['order_by']

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'Urutan yang dipilih tidak tersedia.' in validate_message

    def test_search_order_by_not_available_value(self):
        param2 = {
            'latitude': settings.lat,
            'longitude': settings.long,
            'missed': '0',
            'ready_stock': '1',
            'menu_categories[0]': '1',
            'max_price': '50000',
            'distance': '10000',
            'preorder': '0',
            'pickup_time_start': '01:00',
            'pickup_time_end': '23:00',
            'keyword': '',
            'order_by': 'nearbyy',
            'is_active': '1'
        }
        discover = requests.get(settings.url_search_customer, params=param2,
                                headers=settings.header_with_token_customer)

        validate_status = discover.json().get('success')
        validate_message = discover.json().get('message')['order_by']

        assert discover.status_code == 422
        assert validate_status == bool(False)
        assert 'Urutan yang dipilih tidak tersedia.' in validate_message
