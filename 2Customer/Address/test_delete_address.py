import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')

class TestCustomerDeleteAddress:

    def test_delete_address_normal(self):
        delete = requests.delete(settings.url_delete_address_customer + str(
            settings.var_list_address_customer().json().get('data')[0]['id']),
                                 headers=settings.header_with_token_customer)

        validate_status = delete.json().get('success')
        validate_message = delete.json().get('message')

        assert delete.status_code == 200
        assert validate_status == bool(True)
        assert 'Data alamat berhasil dihapus' in validate_message

    def test_delete_wrong_token(self):
        delete = requests.delete(settings.url_delete_address_customer + str(
            settings.var_list_address_customer().json().get('data')[0]['id']),
                                 headers=settings.header_wrong_token_customer)

        validate_status = delete.json().get('success')
        validate_message = delete.json().get('message')

        assert delete.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_delete_address_token_empty_value(self):
        delete = requests.delete(settings.url_delete_address_customer + str(
            settings.var_list_address_customer().json().get('data')[0]['id']),
                                 headers=settings.header_without_token_customer)

        validate_status = delete.json().get('success')
        validate_message = delete.json().get('message')

        assert delete.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_delete_address_id_empty_value(self):
        delete = requests.delete(settings.url_delete_address_customer + '',
                                 headers=settings.header_with_token_customer)

        validate_status = delete.json().get('success')
        validate_message = delete.json().get('message')

        assert delete.status_code == 405
        assert validate_status == bool(False)
        assert 'Method Not Allowed' in validate_message

    def test_delete_address_id_text_value(self):
        delete = requests.delete(settings.url_delete_address_customer + 'aaaa',
                                 headers=settings.header_with_token_customer)

        validate_status = delete.json().get('success')
        validate_message = delete.json().get('message')

        assert delete.status_code == 404
        assert validate_status == bool(False)
        assert 'Alamat tidak ditemukan' in validate_message

    def test_delete_address_id_not_found(self):
        delete = requests.delete(settings.url_delete_address_customer + '999999',
                                 headers=settings.header_with_token_customer)

        validate_status = delete.json().get('success')
        validate_message = delete.json().get('message')

        assert delete.status_code == 404
        assert validate_status == bool(False)
        assert 'Alamat tidak ditemukan' in validate_message
