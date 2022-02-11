import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerUpdatePrivateData:

    def test_update_private_data_normal(self):
        param2 = {
            'name': 'maulana',
            'phone_number': '085710819443'
        }
        show_update_private_data = requests.patch(settings.url_update_private_data_customer, params=param2,
                                                  headers=settings.header_with_token_customer)

        validate_status = show_update_private_data.json().get('success')
        validate_message = show_update_private_data.json().get('message')
        validate_data = show_update_private_data.json().get('data')
        validate_data_name = show_update_private_data.json().get('data')['name']
        validate_data_no_ponsel = show_update_private_data.json().get('data')['no_ponsel']

        assert show_update_private_data.status_code == 200
        assert validate_status == bool(True)
        assert 'Data customer berhasil diperbarui.' in validate_message
        assert_that(validate_data).contains('id', 'name', 'email', 'no_ponsel', 'alamat', 'auth_origin',
                                                 'referal_code',
                                                 'onesignal_loc', 'latitude', 'longitude')
        assert validate_data_name == 'maulana'
        assert validate_data_no_ponsel == '085710819443'

    def test_update_private_data_wrong_token(self):
        param2 = {
            'name': 'maulana',
            'phone_number': '085710819443'
        }
        show_update_private_data = requests.patch(settings.url_update_private_data_customer, params=param2,
                                                  headers=settings.header_wrong_token_customer)

        validate_status = show_update_private_data.json().get('success')
        validate_message = show_update_private_data.json().get('message')

        assert show_update_private_data.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_update_private_data_empty_token(self):
        param2 = {
            'name': 'maulana',
            'phone_number': '085710819443'
        }
        show_update_private_data = requests.patch(settings.url_update_private_data_customer, params=param2,
                                                  headers=settings.header_without_token_customer)

        validate_status = show_update_private_data.json().get('success')
        validate_message = show_update_private_data.json().get('message')

        assert show_update_private_data.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_update_private_data_without_param_nama(self):
        param2 = {
            # 'name': 'maulana',
            'phone_number': '085710819443'
        }
        show_update_private_data = requests.patch(settings.url_update_private_data_customer, params=param2,
                                                  headers=settings.header_with_token_customer)

        validate_status = show_update_private_data.json().get('success')
        validate_message = show_update_private_data.json().get('message')['name']

        assert show_update_private_data.status_code == 422
        assert validate_status == bool(False)
        assert 'Nama tidak boleh kosong.' in validate_message

    def test_update_private_data_nama_empty_value(self):
        param2 = {
            'name': '',
            'phone_number': '085710819443'
        }
        show_update_private_data = requests.patch(settings.url_update_private_data_customer, params=param2,
                                                  headers=settings.header_with_token_customer)

        validate_status = show_update_private_data.json().get('success')
        validate_message = show_update_private_data.json().get('message')['name']

        assert show_update_private_data.status_code == 422
        assert validate_status == bool(False)
        assert 'Nama tidak boleh kosong.' in validate_message

    def test_update_private_data_nama_value_kurang6(self):
        param2 = {
            'name': 'aa',
            'phone_number': '085710819443'
        }
        show_update_private_data = requests.patch(settings.url_update_private_data_customer, params=param2,
                                                  headers=settings.header_with_token_customer)

        validate_status = show_update_private_data.json().get('success')
        validate_message = show_update_private_data.json().get('message')['name']

        assert show_update_private_data.status_code == 422
        assert validate_status == bool(False)
        assert 'Nama setidaknya harus 3 karakter.' in validate_message

    def test_update_private_data_without_param_phone(self):
        param2 = {
            'name': 'maulana',
            # 'phone_number': '085710819443'
        }
        show_update_private_data = requests.patch(settings.url_update_private_data_customer, params=param2,
                                                  headers=settings.header_with_token_customer)

        validate_status = show_update_private_data.json().get('success')
        validate_message = show_update_private_data.json().get('message')['phone_number']

        assert show_update_private_data.status_code == 422
        assert validate_status == bool(False)
        assert 'No. HP tidak boleh kosong.' in validate_message

    def test_update_private_data_phone_empty_value(self):
        param2 = {
            'name': 'maulana',
            'phone_number': ''
        }
        show_update_private_data = requests.patch(settings.url_update_private_data_customer, params=param2,
                                                  headers=settings.header_with_token_customer)

        validate_status = show_update_private_data.json().get('success')
        validate_message = show_update_private_data.json().get('message')['phone_number']

        assert show_update_private_data.status_code == 422
        assert validate_status == bool(False)
        assert 'No. HP tidak boleh kosong.' in validate_message

    def test_update_private_data_phone_text_value(self):
        param2 = {
            'name': 'maulana',
            'phone_number': 'aaa'
        }
        show_update_private_data = requests.patch(settings.url_update_private_data_customer, params=param2,
                                                  headers=settings.header_with_token_customer)

        validate_status = show_update_private_data.json().get('success')
        validate_message = show_update_private_data.json().get('message')

        assert show_update_private_data.status_code == 200
        assert validate_status == bool(True)
        assert 'Data customer berhasil diperbarui.' in validate_message
