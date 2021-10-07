import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestOrderIndex:

    def test_order_index_normal(self):
        response = requests.get(settings.url_index_order_merchant + '?type=finish',
                                headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")
        validate_data = data.get("data")
        validate_order_items = data.get("data")[0]['order_item']

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert "Data pesanan ditemukan." in validate_message
        assert_that(validate_data).is_type_of(list)
        assert_that(validate_data[0]).contains('id', 'user_id', 'registrasi_order_number', 'created_at',
                                               'shipment_detail_id', 'isDelivery', 'preorder', 'subtotal',
                                               'grand_total',
                                               'komisi_surplus', 'komisi_merchant', 'customer_name', 'order_date',
                                               'cancel_status', 'is_tempat_makanan', 'total_jumlah_order',
                                               'order_item')
        assert_that(validate_order_items[0]).contains('merchant_menu_id', 'stock_id', 'jumlah_order', 'note',
                                                      'nama_menu_makanan', 'deskripsi', 'waktu_mulai_penjemputan',
                                                      'waktu_akhir_penjemputan', 'harga_asli', 'harga_jual',
                                                      'is_non_halal', 'is_tomorrow', 'created_at', 'updated_at')

    def test_order_index_token_empty_value(self):
        response = requests.get(settings.url_index_order_merchant + '?type=finish',
                                headers=settings.header_without_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message

    def test_order_index_token_wrong_value(self):
        response = requests.get(settings.url_index_order_merchant + '?type=finish',
                                headers=settings.header_wrong_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message

    def test_order_index_type_number_value(self):
        response = requests.get(settings.url_index_order_merchant + '?type=123',
                                headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")['type']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "type yang dipilih tidak tersedia." in validate_message

    def test_order_index_type_empty_value(self):
        response = requests.get(settings.url_index_order_merchant + '?type=',
                                headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")['type']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "type tidak boleh kosong." in validate_message

    def test_order_index_type_wrong_value(self):
        response = requests.get(settings.url_index_order_merchant + '?type=done',
                                headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")['type']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "type yang dipilih tidak tersedia." in validate_message
