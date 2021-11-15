import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerSelfPickup:

    def test_sp_normal(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')
        validate_data = self_pickup.json().get('data')
        validate_data_transaksi = self_pickup.json().get('data')['transaksi']

        assert self_pickup.status_code == 201
        assert validate_status == bool(True)
        assert 'Order Self Pickup berhasil dibuat' in validate_message
        assert_that(validate_data).is_not_none()
        assert_that(validate_data_transaksi).is_not_none()

    def test_sp_wrong_token(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_wrong_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')

        assert self_pickup.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_sp_token_empty_value(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_without_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')

        assert self_pickup.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_sp_payment_methode_empty_value(self):
        param = {
            'payment_method_id': '',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')['payment_method_id']

        assert self_pickup.status_code == 422
        assert validate_status == bool(False)
        assert 'Metode Pembayaran tidak boleh kosong.' in validate_message

    def test_sp_without_param_payment_methode(self):
        param = {
            # 'payment_method_id': '',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')['payment_method_id']

        assert self_pickup.status_code == 422
        assert validate_status == bool(False)
        assert 'Metode Pembayaran tidak boleh kosong.' in validate_message

    def test_sp_payment_methode_wrong_value(self):
        param = {
            'payment_method_id': '66',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')['payment_method_id']

        assert self_pickup.status_code == 422
        assert validate_status == bool(False)
        assert 'Metode Pembayaran yang dipilih tidak tersedia.' in validate_message

    def test_sp_payment_methode_text_value(self):
        param = {
            'payment_method_id': 'aaa',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')['payment_method_id']

        assert self_pickup.status_code == 422
        assert validate_status == bool(False)
        assert 'Metode Pembayaran yang dipilih tidak tersedia.' in validate_message

    def test_sp_phone_empty_value(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')['phone_number']

        assert self_pickup.status_code == 422
        assert validate_status == bool(False)
        assert 'No. HP tidak boleh kosong ketika Metode Pembayaran adalah 1.' in validate_message

    def test_sp_without_param_phone(self):
        param = {
            'payment_method_id': '1',
            # 'phone_number': '',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')['phone_number']

        assert self_pickup.status_code == 422
        assert validate_status == bool(False)
        assert 'No. HP tidak boleh kosong ketika Metode Pembayaran adalah 1.' in validate_message

    def test_sp_phone_text_value(self):
        param = {
            'payment_method_id': '1',
            'phone_number': 'aaa',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')

        assert self_pickup.status_code == 500
        assert validate_status == bool(False)
        assert 'Aduh!' in validate_message

    def test_sp_phone_wrong_format_value(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '09:00',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')

        assert self_pickup.status_code == 500
        assert validate_status == bool(False)
        assert 'Aduh!' in validate_message

    def test_sp_lunchbox_empty_value(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': '',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')['is_lunchbox']

        assert self_pickup.status_code == 422
        assert validate_status == bool(False)
        assert 'Kotak makan tidak boleh kosong.' in validate_message

    def test_sp_without_param_lunchbox(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            # 'is_lunchbox': '',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')['is_lunchbox']

        assert self_pickup.status_code == 422
        assert validate_status == bool(False)
        assert 'Kotak makan tidak boleh kosong.' in validate_message

    def test_sp_lunchbox_text_value(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': 'a',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')['is_lunchbox']

        assert self_pickup.status_code == 422
        assert validate_status == bool(False)
        assert 'Kotak makan harus bernilai true atau false.' in validate_message

    def test_sp_lunchbox_not_bool_value(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': '10',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')['is_lunchbox']

        assert self_pickup.status_code == 422
        assert validate_status == bool(False)
        assert 'Kotak makan harus bernilai true atau false.' in validate_message

    def test_sp_donation_empty_value(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            'donation_price': '',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')['donation_price']

        assert self_pickup.status_code == 422
        assert validate_status == bool(False)
        assert 'Jumlah donasi harus berupa angka.' in validate_message

    def test_sp_without_param_donation(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            # 'donation_price': '',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')
        validate_data = self_pickup.json().get('data')
        validate_data_transaksi = self_pickup.json().get('data')['transaksi']

        assert self_pickup.status_code == 201
        assert validate_status == bool(True)
        assert 'Order Self Pickup berhasil dibuat' in validate_message
        assert_that(validate_data).is_not_none()
        assert_that(validate_data_transaksi).is_not_none()

    def test_sp_donation_text_value(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            'donation_price': 'aa',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')['donation_price']
        assert self_pickup.status_code == 422
        assert validate_status == bool(False)
        assert 'Jumlah donasi harus berupa angka.' in validate_message

    def test_sp_donation_value_kurang_2500(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            'donation_price': '1000',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')['donation_price']
        assert self_pickup.status_code == 422
        assert validate_status == bool(False)
        assert 'Jumlah donasi harus diantara 2500 dan 30000' in validate_message

    def test_sp_voucher_empty_value(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'voucher_id': '',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')['voucher_id']

        assert self_pickup.status_code == 422
        assert validate_status == bool(False)
        assert 'Voucher harus berupa angka.' in validate_message

    def test_sp_without_param_voucher(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            'donation_price': '2500',
            # 'voucher_id': '',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        assert self_pickup.status_code == 201
        assert validate_status == bool(True)

    def test_sp_voucher_not_found(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'voucher_id': '9999999',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')

        assert self_pickup.status_code == 404
        assert validate_status == bool(False)
        assert 'Voucher tidak ditemukan' in validate_message

    def test_sp_voucher_text_value(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'voucher_id': 'aaa',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')['voucher_id']

        assert self_pickup.status_code == 422
        assert validate_status == bool(False)
        assert 'Voucher harus berupa angka.' in validate_message

    def test_sp_stock_id_empty_value(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'voucher_id': '557',
            'order_items[0][stock_id]': '',
            'order_items[0][qty]': '1',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')['order_items.0.stock_id']

        assert self_pickup.status_code == 422
        assert validate_status == bool(False)
        assert 'order_items.0.stock_id tidak boleh kosong.' in validate_message

    def test_sp_without_param_stock_id(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'voucher_id': '557',
            # 'order_items[0][stock_id]': '',
            'order_items[0][qty]': '1',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')['order_items.0.stock_id']

        assert self_pickup.status_code == 422
        assert validate_status == bool(False)
        assert 'order_items.0.stock_id tidak boleh kosong.' in validate_message

    def test_sp_stock_id_text_value(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'voucher_id': '557',
            'order_items[0][stock_id]': 'aaa',
            'order_items[0][qty]': '1',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')['order_items.0.stock_id']

        assert self_pickup.status_code == 422
        assert validate_status == bool(False)
        assert 'order_items.0.stock_id harus berupa angka.' in validate_message

    def test_sp_stock_id_not_found(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'voucher_id': '557',
            'order_items[0][stock_id]': '9999999',
            'order_items[0][qty]': '1',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')[0]['message']

        assert self_pickup.status_code == 422
        assert validate_status == bool(False)
        assert 'Menu tidak ditemukan' in validate_message

    def test_sp_qty_empty_value(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'voucher_id': '557',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')['order_items.0.qty']

        assert self_pickup.status_code == 422
        assert validate_status == bool(False)
        assert 'order_items.0.qty tidak boleh kosong.' in validate_message

    def test_sp_without_param_qty(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'voucher_id': '557',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')['order_items.0.qty']

        assert self_pickup.status_code == 422
        assert validate_status == bool(False)
        assert 'order_items.0.qty tidak boleh kosong.' in validate_message

    def test_sp_qty_value_text(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'voucher_id': '557',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': 'aaa',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')['order_items.0.qty']

        assert self_pickup.status_code == 422
        assert validate_status == bool(False)
        assert 'order_items.0.qty harus berupa angka.' in validate_message

    def test_sp_qty_minus_value(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'voucher_id': '557',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '-1',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')['order_items.0.qty']

        assert self_pickup.status_code == 422
        assert validate_status == bool(False)
        assert 'order_items.0.qty harus diantara 1 dan 999' in validate_message

    def test_sp_qty_melebihi_stock(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'voucher_id': '557',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '999',
            'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')[0]['message']

        assert self_pickup.status_code == 422
        assert validate_status == bool(False)
        assert 'tidak tersedia' in validate_message

    def test_sp_without_param_note(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'voucher_id': '557',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
            # 'order_items[0][note]': 'Note Menu',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)

        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')

        assert self_pickup.status_code == 201
        assert validate_status == bool(True)
        assert 'Order Self Pickup berhasil dibuat' in validate_message

    def test_sp_note_empty_value(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'voucher_id': '557',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
            'order_items[0][note]': '',
            'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)
        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')

        assert self_pickup.status_code == 201
        assert validate_status == bool(True)
        assert 'Order Self Pickup berhasil dibuat' in validate_message

    def test_sp_without_param_address(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'voucher_id': '557',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
            'order_items[0][note]': '',
            # 'address': 'Megaregency',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)
        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')['address']

        assert self_pickup.status_code == 422
        assert validate_status == bool(False)
        assert 'Alamat tidak boleh kosong.' in validate_message

    def test_sp_address_empty_value(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'voucher_id': '557',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
            'order_items[0][note]': '',
            'address': '',
            'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)
        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')['address']

        assert self_pickup.status_code == 422
        assert validate_status == bool(False)
        assert 'Alamat tidak boleh kosong.' in validate_message

    def test_sp_without_param_note_u(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'voucher_id': '557',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
            'order_items[0][note]': '',
            'address': 'Megaregency',
            # 'note': 'Note QA'
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)
        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')

        assert self_pickup.status_code == 500
        assert validate_status == bool(False)
        assert 'Aduh!' in validate_message

    def test_sp_note_empty_value_u(self):
        param = {
            'payment_method_id': '1',
            'phone_number': '081386356616',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'voucher_id': '557',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
            'order_items[0][note]': '',
            'address': 'Megaregency',
            'note': ''
        }
        self_pickup = requests.post(settings.url_self_pickup_customer, data=param,
                                    headers=settings.header_with_token_customer)
        validate_status = self_pickup.json().get('success')
        validate_message = self_pickup.json().get('message')

        assert self_pickup.status_code == 201
        assert validate_status == bool(True)
        assert 'Order Self Pickup berhasil dibuat' in validate_message
