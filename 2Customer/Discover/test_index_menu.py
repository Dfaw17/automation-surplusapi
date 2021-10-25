import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerIndexMenu:

    def test_index_menu_normal(self):
        param2 = {
            'type': 'nearby'
        }
        index_menu = requests.get(settings.url_index_menu_customer, params=param2,
                                  headers=settings.header_with_token_customer)

        validate_status = index_menu.json().get('success')
        validate_message = index_menu.json().get('message')
        validate_data = index_menu.json().get('data')[0]

        assert index_menu.status_code == 200
        assert validate_status == bool(True)
        assert 'Data menu terlewat berhasil ditemukan.' in validate_message
        assert_that(validate_data).contains('stock_id', 'merchant_id', 'menu_id', 'nama_menu_makanan',
                                            'merchant_kategori_makanan_id', 'is_exclusive', 'deskripsi', 'harga_asli',
                                            'harga_jual', 'is_non_halal', 'weight', 'weight_string', 'image_thumbnail',
                                            'created_at', 'updated_at', 'waktu_mulai_penjemputan',
                                            'waktu_akhir_penjemputan', 'stock', 'is_active', 'is_missed', 'is_tomorrow',
                                            'is_hide', 'waktu_missed', 'total_terjual', 'max_active_date',
                                            'expired_date', 'expired_time', 'max_storage_days', 'nama_merchant',
                                            'alamat_merchant', 'merchant_logo', 'merchant_branch_status',
                                            'merchant_central_id', 'distance')

    def test_index_menu_wrong_token(self):
        param2 = {
            'type': 'nearby'
        }
        index_menu = requests.get(settings.url_index_menu_customer, params=param2,
                                  headers=settings.header_wrong_token_customer)

        validate_status = index_menu.json().get('success')
        validate_message = index_menu.json().get('message')

        assert index_menu.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_index_menu_token_empty_value(self):
        param2 = {
            'type': 'nearby'
        }
        index_menu = requests.get(settings.url_index_menu_customer, params=param2,
                                  headers=settings.header_without_token_customer)

        validate_status = index_menu.json().get('success')
        validate_message = index_menu.json().get('message')

        assert index_menu.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_index_menu_type_empty_value(self):
        param2 = {
            'type': ''
        }
        index_menu = requests.get(settings.url_index_menu_customer, params=param2,
                                  headers=settings.header_with_token_customer)

        validate_status = index_menu.json().get('success')
        validate_message = index_menu.json().get('message')['type']

        assert index_menu.status_code == 422
        assert validate_status == bool(False)
        assert 'type tidak boleh kosong.' in validate_message

    def test_index_menu_type_not_available_value(self):
        param2 = {
            'type': 'qaqaqa'
        }
        index_menu = requests.get(settings.url_index_menu_customer, params=param2,
                                  headers=settings.header_with_token_customer)

        validate_status = index_menu.json().get('success')
        validate_message = index_menu.json().get('message')['type']

        assert index_menu.status_code == 422
        assert validate_status == bool(False)
        assert 'type yang dipilih tidak tersedia.' in validate_message

    def test_index_menu_without_param_type(self):
        param2 = {
            # 'type': 'qaqaqa'
        }
        index_menu = requests.get(settings.url_index_menu_customer, params=param2,
                                  headers=settings.header_with_token_customer)

        validate_status = index_menu.json().get('success')
        validate_message = index_menu.json().get('message')['type']

        assert index_menu.status_code == 422
        assert validate_status == bool(False)
        assert 'type tidak boleh kosong.' in validate_message

