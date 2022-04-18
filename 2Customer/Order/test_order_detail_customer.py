import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerOrdersDetailOrder:

    def test_order_detail_normal(self):
        detail_order = requests.get(
            settings.url_detail_order_customer + settings.var_list_order_customer().json().get('data')['data'][0][
                'registrasi_order_number'], headers=settings.header_with_token_customer)

        validate_status = detail_order.json().get('success')
        validate_message = detail_order.json().get('message')
        validate_data = detail_order.json().get('data')

        assert detail_order.status_code == 200
        assert validate_status == bool(True)
        assert 'berhasil ditemukan.' in validate_message
        assert_that(validate_data).is_not_none()
        assert validate_data['registrasi_order_number'] == settings.var_list_order_customer().json().get('data')['data'][0][
            'registrasi_order_number']

    def test_order_detail_token_empty_value(self):
        detail_order = requests.get(
            settings.url_detail_order_customer + settings.var_list_order_customer().json().get('data')['data'][0][
                'registrasi_order_number'], headers=settings.header_without_token_customer)

        validate_status = detail_order.json().get('success')
        validate_message = detail_order.json().get('message')

        assert detail_order.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_order_detail_token_wrong_value(self):
        detail_order = requests.get(
            settings.url_detail_order_customer + settings.var_list_order_customer().json().get('data')['data'][0][
                'registrasi_order_number'], headers=settings.header_wrong_token_customer)

        validate_status = detail_order.json().get('success')
        validate_message = detail_order.json().get('message')

        assert detail_order.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_order_detail_id_transaksi_wrong_format_value(self):
        detail_order = requests.get(
            settings.url_detail_order_customer + '09:30', headers=settings.header_with_token_customer)

        validate_status = detail_order.json().get('success')
        validate_message = detail_order.json().get('message')

        assert detail_order.status_code == 404
        assert validate_status == bool(False)
        assert 'Data pesanan tidak ditemukan' in validate_message

    def test_order_detail_id_transaksi_not_found(self):
        detail_order = requests.get(
            settings.url_detail_order_customer + '999888777', headers=settings.header_with_token_customer)

        validate_status = detail_order.json().get('success')
        validate_message = detail_order.json().get('message')

        assert detail_order.status_code == 404
        assert validate_status == bool(False)
        assert 'Data pesanan tidak ditemukan' in validate_message

    def test_order_detail_id_transaksi_empty_value(self):
        detail_order = requests.get(
            settings.url_detail_order_customer + '', headers=settings.header_with_token_customer)

        validate_status = detail_order.json().get('success')
        validate_message = detail_order.json().get('message')['status_order']

        assert detail_order.status_code == 422
        assert validate_status == bool(False)
        assert 'Status pesanan tidak boleh kosong.' in validate_message
