import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestShowMerchantMenu:

    def test_show_merchant_menu_normal(self):
        response = requests.get(
            settings.url_get_all_merchant_menu_merchant + str(
                settings.var_list_menu_merchant().json().get('data')[0]['id']),
            headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")
        validate_data_id = str(data.get("data")["id"])
        validate_data = data.get("data")
        validate_merchant_id = str(data.get("data")["merchant_id"])
        validate_nama_makanan = data.get("data")["nama_menu_makanan"]

        assert validate_status == bool(True)
        assert response.status_code == 200
        assert validate_message == "Data menu ditemukan."
        assert validate_data_id == str(settings.var_list_menu_merchant().json().get('data')[0]['id'])
        assert_that(validate_merchant_id).is_not_none()
        assert_that(validate_nama_makanan).is_not_empty()
        assert str(settings.var_list_menu_merchant().json().get('data')[0]['merchant_id']) == validate_merchant_id
        assert_that(validate_data).contains_only('id', 'nama_menu_makanan', 'merchant_kategori_makanan_id',
                                                 'is_exclusive', 'deskripsi', 'harga_asli', 'harga_jual',
                                                 'is_non_halal', 'weight', 'weight_string', 'image_thumbnail',
                                                 'created_at', 'updated_at', 'stock_id', 'merchant_id',
                                                 'waktu_mulai_penjemputan', 'waktu_akhir_penjemputan', 'stock',
                                                 'in_catalog', 'is_active', 'is_missed', 'is_tomorrow', 'waktu_missed',
                                                 'total_terjual', 'max_active_date', 'expired_date', 'expired_time',
                                                 'max_storage_days', 'menu_images')

    def test_show_merchant_menu_empty_token(self):
        response = requests.get(settings.url_get_all_merchant_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']),
                                headers=settings.header_without_token_merchant)
        data = response.text

        assert response.status_code == 401
        assert "Unauthorized" in data

    def test_show_merchant_menu_wrong_token(self):
        response = requests.get(settings.url_get_all_merchant_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']),
                                headers=settings.header_wrong_token_merchant)
        data = response.text

        assert response.status_code == 401
        assert "Unauthorized" in data

    def test_show_merchant_menu_wrong_id(self):
        response = requests.get(settings.url_get_all_merchant_menu_merchant + '999999',
                                headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")

        assert validate_status == bool(False)
        assert response.status_code == 404
        assert validate_message == "Data tidak ditemukan"
