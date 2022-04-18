import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerOrdersListOrder:
    def test_order_list_normal(self):
        param2 = {
            'status_order': 'done'
        }
        list_order = requests.get(settings.url_list_order_customer, params=param2,
                                  headers=settings.header_with_token_customer)

        validate_status = list_order.json().get('success')
        validate_message = list_order.json().get('message')

        assert list_order.status_code == 200
        assert validate_status == bool(True)
        assert 'Data order berhasil ditemukan.' in validate_message

    def test_order_list_wrong_token(self):
        param2 = {
            'status_order': 'done'
        }
        list_order = requests.get(settings.url_list_order_customer, params=param2,
                                  headers=settings.header_wrong_token_customer)

        validate_status = list_order.json().get('success')
        validate_message = list_order.json().get('message')

        assert list_order.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_order_list_token_empty_value(self):
        param2 = {
            'status_order': 'done'
        }
        list_order = requests.get(settings.url_list_order_customer, params=param2,
                                  headers=settings.header_without_token_customer)

        validate_status = list_order.json().get('success')
        validate_message = list_order.json().get('message')

        assert list_order.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_order_list_status_order_wrong_value(self):
        param2 = {
            'status_order': 'dones'
        }
        list_order = requests.get(settings.url_list_order_customer, params=param2,
                                  headers=settings.header_with_token_customer)

        validate_status = list_order.json().get('success')
        validate_message = list_order.json().get('message')['status_order']

        assert list_order.status_code == 422
        assert validate_status == bool(False)
        assert 'Status pesanan yang dipilih tidak tersedia.' in validate_message

    def test_order_list_status_order_empty_value(self):
        param2 = {
            'status_order': ''
        }
        list_order = requests.get(settings.url_list_order_customer, params=param2,
                                  headers=settings.header_with_token_customer)

        validate_status = list_order.json().get('success')
        validate_message = list_order.json().get('message')['status_order']

        assert list_order.status_code == 422
        assert validate_status == bool(False)
        assert 'Status pesanan tidak boleh kosong.' in validate_message

    def test_order_list_without_param_status_order(self):
        param2 = {
            # 'status_order': ''
        }
        list_order = requests.get(settings.url_list_order_customer, params=param2,
                                  headers=settings.header_with_token_customer)

        validate_status = list_order.json().get('success')
        validate_message = list_order.json().get('message')['status_order']

        assert list_order.status_code == 422
        assert validate_status == bool(False)
        assert 'Status pesanan tidak boleh kosong.' in validate_message
