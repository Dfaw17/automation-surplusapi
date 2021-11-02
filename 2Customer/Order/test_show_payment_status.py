import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerOrdersShowPaymentStatus:

    def test_show_payement_status_normal(self):
        param3 = {
            'payment_method': 'OVO'
        }
        show_payment = requests.get(
            settings.url_show_payment_status_customer +
            settings.var_list_order_customer().json().get('data')[0][
                'registrasi_order_number'] + '/payment-status',
            params=param3, headers=settings.header_with_token_customer)

        validate_status = show_payment.json().get('success')
        validate_message = show_payment.json().get('message')

        assert show_payment.status_code == 200
        assert validate_status == bool(True)
        assert 'Status pembayaran berhasil ditemukan' in validate_message

    def test_show_payment_status_wrong_token(self):
        param3 = {
            'payment_method': 'OVO'
        }
        show_payment = requests.get(
            settings.url_show_payment_status_customer +
            settings.var_list_order_customer().json().get('data')[0][
                'registrasi_order_number'] + '/payment-status',
            params=param3, headers=settings.header_wrong_token_customer)

        validate_status = show_payment.json().get('success')
        validate_message = show_payment.json().get('message')

        assert show_payment.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_show_payment_status_token_empty_value(self):
        param3 = {
            'payment_method': 'OVO'
        }
        show_payment = requests.get(
            settings.url_show_payment_status_customer +
            settings.var_list_order_customer().json().get('data')[0][
                'registrasi_order_number'] + '/payment-status',
            params=param3, headers=settings.header_without_token_customer)

        validate_status = show_payment.json().get('success')
        validate_message = show_payment.json().get('message')

        assert show_payment.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_show_payment_status_id_trx_not_found(self):
        param3 = {
            'payment_method': 'OVO'
        }
        show_payment = requests.get(
            settings.url_show_payment_status_customer + 'S12345678987654321' + '/payment-status',
            params=param3, headers=settings.header_with_token_customer)

        validate_status = show_payment.json().get('success')
        validate_message = show_payment.json().get('message')
        validate_data = show_payment.json().get('data')

        assert show_payment.status_code == 200
        assert validate_status == bool(True)
        assert 'Status pembayaran berhasil ditemukan' in validate_message
        assert 'Payment not found' in validate_data

    def test_show_payment_status_id_trx_empty_value(self):
        param3 = {
            'payment_method': 'OVO'
        }
        show_payment = requests.get(
            settings.url_show_payment_status_customer + '' + 'payment-status',
            params=param3, headers=settings.header_with_token_customer)

        validate_status = show_payment.json().get('success')
        validate_message = show_payment.json().get('message')

        assert show_payment.status_code == 404
        assert validate_status == bool(False)
        assert 'Data pesanan tidak ditemukan' in validate_message

    def test_show_payment_status_id_trx_wrong_format(self):
        param3 = {
            'payment_method': 'OVO'
        }
        show_payment = requests.get(
            settings.url_show_payment_status_customer + '11:37' + '/payment-status',
            params=param3, headers=settings.header_with_token_customer)

        validate_status = show_payment.json().get('success')
        validate_message = show_payment.json().get('message')
        validate_data = show_payment.json().get('data')

        assert show_payment.status_code == 200
        assert validate_status == bool(True)
        assert 'Status pembayaran berhasil ditemukan' in validate_message
        assert 'Payment not found' in validate_data

    def test_show_payment_status_without_param_payment_methode(self):
        param3 = {
            # 'payment_method': 'OVO'
        }
        show_payment = requests.get(
            settings.url_show_payment_status_customer +
            settings.var_list_order_customer().json().get('data')[0][
                'registrasi_order_number'] + '/payment-status',
            params=param3, headers=settings.header_with_token_customer)

        validate_status = show_payment.json().get('success')
        validate_message = show_payment.json().get('message')['payment_method']

        assert show_payment.status_code == 422
        assert validate_status == bool(False)
        assert 'Metode Pembayaran tidak boleh kosong.' in validate_message

    def test_show_payment_status_payment_methode_empty(self):
        param3 = {
            'payment_method': ''
        }
        show_payment = requests.get(
            settings.url_show_payment_status_customer +
            settings.var_list_order_customer().json().get('data')[0][
                'registrasi_order_number'] + '/payment-status',
            params=param3, headers=settings.header_with_token_customer)

        validate_status = show_payment.json().get('success')
        validate_message = show_payment.json().get('message')['payment_method']

        assert show_payment.status_code == 422
        assert validate_status == bool(False)
        assert 'Metode Pembayaran tidak boleh kosong.' in validate_message

    def test_show_payment_status_payment_methode_wrong_value(self):
        param3 = {
            'payment_method': 'OVVOO'
        }
        show_payment = requests.get(
            settings.url_show_payment_status_customer +
            settings.var_list_order_customer().json().get('data')[0][
                'registrasi_order_number'] + '/payment-status',
            params=param3, headers=settings.header_with_token_customer)

        validate_status = show_payment.json().get('success')
        validate_message = show_payment.json().get('message')['payment_method']

        assert show_payment.status_code == 422
        assert validate_status == bool(False)
        assert 'Metode Pembayaran yang dipilih tidak tersedia.' in validate_message
