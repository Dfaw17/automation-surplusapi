import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerShowAddress:

    def test_show_address_normal(self):
        show = requests.get(
            settings.url_show_address_customer + str(settings.var_list_voucher_customer().json().get('data')[0]['id']),
            headers=settings.header_with_token_customer)

        verify_status = show.json().get('success')
        verify_message = show.json().get('message')
        verify_data = show.json().get('data')
        verify_data_id = show.json().get('data')['id']

        assert show.status_code == 200
        assert verify_status == bool(True)
        assert 'Data alamat berhasil ditemukan.' in verify_message
        assert_that(verify_data).contains_only('id', 'user_id', 'receiver', 'phone', 'address', 'kategori', 'title',
                                               'note',
                                               'created_at', 'updated_at', 'latitude', 'longitude')
        assert verify_data_id == settings.var_list_voucher_customer().json().get('data')[0]['id']

    def test_show_address_wrong_token(self):
        show = requests.get(
            settings.url_show_address_customer + str(settings.var_list_voucher_customer().json().get('data')[0]['id']),
            headers=settings.header_wrong_token_customer)

        verify_status = show.json().get('success')
        verify_message = show.json().get('message')

        assert show.status_code == 401
        assert verify_status == bool(False)
        assert 'Unauthorized' in verify_message

    def test_show_address_token_empty_value(self):
        show = requests.get(
            settings.url_show_address_customer + str(settings.var_list_voucher_customer().json().get('data')[0]['id']),
            headers=settings.header_without_token_customer)

        verify_status = show.json().get('success')
        verify_message = show.json().get('message')

        assert show.status_code == 401
        assert verify_status == bool(False)
        assert 'Unauthorized' in verify_message

    def test_show_address_id_not_found(self):
        show = requests.get(
            settings.url_show_address_customer + '6666',
            headers=settings.header_with_token_customer)

        verify_status = show.json().get('success')
        verify_message = show.json().get('message')

        assert show.status_code == 404
        assert verify_status == bool(False)
        assert 'Alamat tidak ditemukan' in verify_message

    def test_show_address_id_empty_value(self):
        show = requests.get(
            settings.url_show_address_customer + '',
            headers=settings.header_with_token_customer)

        verify_status = show.json().get('success')
        verify_message = show.json().get('message')

        assert show.status_code == 200
        assert verify_status == bool(True)
        assert 'Data alamat berhasil ditemukan.' in verify_message

    def test_show_address_id_text_value(self):
        show = requests.get(
            settings.url_show_address_customer + 'aaa',
            headers=settings.header_with_token_customer)

        verify_status = show.json().get('success')
        verify_message = show.json().get('message')

        assert show.status_code == 404
        assert verify_status == bool(False)
        assert 'Alamat tidak ditemukan' in verify_message