import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestGetAllMerchantMenu:

    def test_get_all_merchant_menu_normal(self):
        response = requests.get(settings.url_get_all_merchant_menu_merchant,
                                headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get("success")
        validate_message = data.get("message")
        validate_data = data.get("data")[0]

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert "Data menu berhasil ditemukan." in validate_message
        assert_that(validate_data).contains('id', 'nama_menu_makanan', 'merchant_kategori_makanan_id',
                                                 'is_exclusive', 'deskripsi', 'harga_asli', 'harga_jual',
                                                 'is_non_halal', 'weight', 'weight_string', 'image_thumbnail',
                                                 'created_at', 'updated_at', 'stock_id', 'merchant_id',
                                                 'waktu_mulai_penjemputan', 'waktu_akhir_penjemputan', 'stock',
                                                 'in_catalog', 'is_active', 'is_missed', 'is_tomorrow', 'waktu_missed',
                                                 'total_terjual', 'max_active_date', 'expired_date', 'expired_time',
                                                 'max_storage_days', 'nama_kategori_makanan')

    def test_get_all_merchant_wrong_token(self):
        response = requests.get(settings.url_get_all_merchant_menu_merchant,
                                headers=settings.header_wrong_token_merchant)

        data = response.json()
        validate_message = data.get("message")

        assert response.status_code == 401
        assert "Unauthorized" in validate_message

    def test_get_all_merchant_empty_token(self):
        response = requests.get(settings.url_get_all_merchant_menu_merchant,
                                headers=settings.header_wrong_token_merchant)
        data = response.json()
        validate_message = data.get("message")

        assert response.status_code == 401
        assert "Unauthorized" in validate_message

