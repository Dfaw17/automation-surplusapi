import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerCancelOrder:

    def test_order_cancel_normal(self):
        param = {
            'payment_phone_number': '081386356616',
            'reason': 'faw reason'
        }
        cancel_order = requests.patch(
            settings.url_cancel_order_customer + settings.var_order_cancel().json().get('data')[
                'registrasi_order_number'] + '/cancel', data=param,
            headers=settings.header_with_token_customer)

        validation_status = cancel_order.json().get('success')
        validation_message = cancel_order.json().get('message')

        assert cancel_order.status_code == 200
        assert validation_status == bool(True)
        assert 'Order berhasil dibatalkan dan refund anda sedang diproses' in validation_message

    def test_order_cancel_wrong_token(self):
        param = {
            'payment_phone_number': '081386356616',
            'reason': 'faw reason'
        }
        cancel_order = requests.patch(
            settings.url_cancel_order_customer + settings.var_order_cancel().json().get('data')[
                'registrasi_order_number'] + '/cancel', data=param,
            headers=settings.header_wrong_token_customer)

        validation_status = cancel_order.json().get('success')
        validation_message = cancel_order.json().get('message')

        assert cancel_order.status_code == 401
        assert validation_status == bool(False)
        assert 'Unauthorized' in validation_message

    def test_order_cancel_token_empty_value(self):
        param = {
            'payment_phone_number': '081386356616',
            'reason': 'faw reason'
        }
        cancel_order = requests.patch(
            settings.url_cancel_order_customer + settings.var_order_cancel().json().get('data')[
                'registrasi_order_number'] + '/cancel', data=param,
            headers=settings.header_without_token_customer)

        validation_status = cancel_order.json().get('success')
        validation_message = cancel_order.json().get('message')

        assert cancel_order.status_code == 401
        assert validation_status == bool(False)
        assert 'Unauthorized' in validation_message

    def test_order_cancel_trx_id_not_found(self):
        param = {
            'payment_phone_number': '081386356616',
            'reason': 'faw reason'
        }
        cancel_order = requests.patch(
            settings.url_cancel_order_customer + 'S1234567252906' + '/cancel', data=param,
            headers=settings.header_with_token_customer)

        validation_status = cancel_order.json().get('success')
        validation_message = cancel_order.json().get('message')

        assert cancel_order.status_code == 404
        assert validation_status == bool(False)
        assert 'tidak ditemukan' in validation_message

    def test_order_cancel_trx_id_empty_value(self):
        param = {
            'payment_phone_number': '081386356616',
            'reason': 'faw reason'
        }
        cancel_order = requests.patch(
            settings.url_cancel_order_customer + '' + '/cancel', data=param,
            headers=settings.header_with_token_customer)

        validation_status = cancel_order.json().get('success')
        validation_message = cancel_order.json().get('message')

        assert cancel_order.status_code == 404
        assert validation_status == bool(False)

    def test_order_cancel_trx_id_wrong_format(self):
        param = {
            'payment_phone_number': '081386356616',
            'reason': 'faw reason'
        }
        cancel_order = requests.patch(
            settings.url_cancel_order_customer + 'K123456789765' + '/cancel', data=param,
            headers=settings.header_with_token_customer)

        validation_status = cancel_order.json().get('success')
        validation_message = cancel_order.json().get('message')

        assert cancel_order.status_code == 404
        assert validation_status == bool(False)
        assert 'tidak ditemukan' in validation_message

    def test_order_cancel_reason_empty_value(self):
        param = {
            'payment_phone_number': '081386356616',
            'reason': ''
        }
        cancel_order = requests.patch(
            settings.url_cancel_order_customer + settings.var_order_cancel().json().get('data')[
                'registrasi_order_number'] + '/cancel', data=param,
            headers=settings.header_with_token_customer)

        validation_status = cancel_order.json().get('success')
        validation_message = cancel_order.json().get('message')['reason']

        assert cancel_order.status_code == 422
        assert validation_status == bool(False)
        assert 'reason tidak boleh kosong.' in validation_message

    def test_order_cancel_without_param_reason(self):
        param = {
            'payment_phone_number': '081386356616',
            # 'reason': ''
        }
        cancel_order = requests.patch(
            settings.url_cancel_order_customer + settings.var_order_cancel().json().get('data')[
                'registrasi_order_number'] + '/cancel', data=param,
            headers=settings.header_with_token_customer)

        validation_status = cancel_order.json().get('success')
        validation_message = cancel_order.json().get('message')['reason']

        assert cancel_order.status_code == 422
        assert validation_status == bool(False)
        assert 'reason tidak boleh kosong.' in validation_message

    def test_order_cancel_payment_phone_empty_value(self):
        param = {
            'payment_phone_number': '',
            'reason': 'faw reason'
        }
        cancel_order = requests.patch(
            settings.url_cancel_order_customer + settings.var_order_cancel().json().get('data')[
                'registrasi_order_number'] + '/cancel', data=param,
            headers=settings.header_with_token_customer)

        validation_status = cancel_order.json().get('success')
        validation_message = cancel_order.json().get('message')['payment_phone_number']

        assert cancel_order.status_code == 422
        assert validation_status == bool(False)
        assert 'No. HP pembayaran tidak boleh kosong.' in validation_message

    def test_order_cancel_without_param_payment_phone(self):
        param = {
            # 'payment_phone_number': '',
            'reason': 'faw reason'
        }
        cancel_order = requests.patch(
            settings.url_cancel_order_customer + settings.var_order_cancel().json().get('data')[
                'registrasi_order_number'] + '/cancel', data=param,
            headers=settings.header_with_token_customer)

        validation_status = cancel_order.json().get('success')
        validation_message = cancel_order.json().get('message')['payment_phone_number']

        assert cancel_order.status_code == 422
        assert validation_status == bool(False)
        assert 'No. HP pembayaran tidak boleh kosong.' in validation_message

    def test_order_cancel_payment_phone_text_value(self):
        param = {
            'payment_phone_number': 'aabbcc',
            'reason': 'faw reason'
        }
        cancel_order = requests.patch(
            settings.url_cancel_order_customer + settings.var_order_cancel().json().get('data')[
                'registrasi_order_number'] + '/cancel', data=param,
            headers=settings.header_with_token_customer)

        validation_status = cancel_order.json().get('success')
        validation_message = cancel_order.json().get('message')

        assert cancel_order.status_code == 200
        assert validation_status == bool(True)
        assert 'Order berhasil dibatalkan dan refund anda sedang diproses' in validation_message




