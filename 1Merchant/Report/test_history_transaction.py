import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestOrderHistoryTransaction:

    def test_history_transaction_normal(self):
        response = requests.get(settings.url_history_trx_merchant, headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")
        validate_data = data.get("data")
        validate_data_orders = data.get("data")['orders']
        validate_data_total_order = data.get("data")['total_order']
        validate_data_order_item = data.get("data")['orders'][0]['order_item']

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert "Data riwayat transaksi berhasil ditemukan" in validate_message
        assert_that(validate_data).contains_only('orders', 'total_order')
        assert_that(len(validate_data_orders)).is_equal_to(validate_data_total_order)
        assert_that(validate_data_orders[0]).contains('id', 'user_id', 'registrasi_order_number', 'created_at',
                                                      'shipment_detail_id', 'isDelivery', 'preorder', 'subtotal',
                                                      'grand_total', 'komisi_surplus', 'komisi_merchant',
                                                      'customer_name',
                                                      'order_date', 'cancel_status', 'is_tempat_makanan',
                                                      'total_jumlah_order', 'order_item')

        assert_that(validate_data_order_item[0]).contains('merchant_menu_id', 'stock_id', 'jumlah_order', 'note',
                                                          'nama_menu_makanan', 'deskripsi',
                                                          'waktu_mulai_penjemputan',
                                                          'waktu_akhir_penjemputan', 'harga_asli', 'harga_jual',
                                                          'is_non_halal', 'is_tomorrow', 'created_at',
                                                          'updated_at')

    def test_history_transaction_wrong_token(self):
        response = requests.get(settings.url_history_trx_merchant, headers=settings.header_wrong_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")

        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message
        assert response.status_code == 401

    def test_history_transaction_token_empty(self):
        response = requests.get(settings.url_history_trx_merchant, headers=settings.header_without_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")

        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message
        assert response.status_code == 401
