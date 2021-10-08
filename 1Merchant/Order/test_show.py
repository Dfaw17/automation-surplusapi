import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestOrderShow:

    def test_order_show_normal(self):
        response = requests.get(settings.url_show_order_merchant + str(
            settings.var_list_order_merchant().json().get('data')[0]['registrasi_order_number']),
                                headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")
        validate_data = data.get("data")
        validate_data_items = data.get("data")['items']
        validate_data_progress_status = data.get("data")['progress_status']
        validate_data_merchant = data.get("data")['merchant']
        validate_data_transaksi = data.get("data")['transaksi']

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert "Data pesanan ditemukan." in validate_message
        assert_that(validate_data).contains('id', 'user_id', 'merchant_id', 'registrasi_order_number',
                                            'registrasi_order_number_secondary', 'alamat', 'status_order_id',
                                            'canceled_by', 'created_at', 'updated_at', 'keterangan', 'shipment_id',
                                            'shipment_detail_id', 'shipment_detail_id', 'order_time',
                                            'pickup_date',
                                            'pickup_time_start', 'pickup_time_end', 'pickup_method', 'preorder',
                                            'customer_name', 'metode_pembayaran', 'invoice_url', 'subtotal',
                                            'delivery_price', 'donation_price', 'voucher_discount', 'voucher_code',
                                            'lunchbox_discount', 'grand_total', 'hemat', 'can_finished', 'items',
                                            'progress_status', 'merchant', 'transaksi', 'order_date')

        assert_that(validate_data_items[0]).contains('menu_id', 'stock_id', 'nama_menu_makanan', 'jumlah_order',
                                                     'harga_jual', 'image', 'is_tomorrow', 'note')

        assert_that(validate_data_progress_status).contains('status', 'info')

        assert_that(validate_data_merchant).contains('id', 'name', 'email', 'no_ponsel', 'alamat', 'auth_origin',
                                                     'referal_code', 'created_at', 'onesignal_loc', 'latitude',
                                                     'longitude', 'distance', 'merchant_logo', 'merchant_category')

        assert_that(validate_data_transaksi).contains('id', 'metode_pembayaran_id', 'order_id', 'invoice_id',
                                                      'invoice_url', 'invoice_expired', 'phone_number', 'subtotal',
                                                      'grand_total', 'grand_total_harga_asli', 'potongan_surplus',
                                                      'potongan_voucher', 'potongan_kotak_makan', 'hemat',
                                                      'komisi_merchant', 'komisi_surplus', 'kode', 'jenis_kode',
                                                      'is_tempat_makanan', 'image_lunchbox', 'is_dikirim',
                                                      'status_transaksi_id', 'status_pickup_id', 'step_progress',
                                                      'pickup_by_system', 'created_at', 'updated_at', 'voucher_id',
                                                      'shipment_price', 'shipment_fee')

    def test_order_show_token_empty_value(self):
        response = requests.get(settings.url_show_order_merchant + str(
            settings.var_list_order_merchant().json().get('data')[0]['registrasi_order_number']),
                                headers=settings.header_without_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message

    def test_order_show_wrong_token(self):
        response = requests.get(settings.url_show_order_merchant + str(
            settings.var_list_order_merchant().json().get('data')[0]['registrasi_order_number']),
                                headers=settings.header_wrong_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message

    def test_order_show_id_trx_empty(self):
        response = requests.get(settings.url_show_order_merchant + "",headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')['type']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'type tidak boleh kosong.' in validate_message

    def test_order_show_id_trx_wrong(self):
        response = requests.get(settings.url_show_order_merchant + "aaabbb",headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 404
        assert validate_status == bool(False)
        assert 'Data pesanan tidak ditemukan' in validate_message
