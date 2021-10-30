import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')

class TestCustomerUpdatePassword:

    def test_update_password_normal(self):

        param2 = {
            'old_password': '12345678',
            'new_password': '12345678',
            're_new_password': '12345678'
        }
        update_passwrod = requests.patch(settings.url_update_password_customer, params=param2, headers=settings.header_with_token_customer)

        validate_status = update_passwrod.json().get('success')
        validate_message = update_passwrod.json().get('message')

        assert update_passwrod.status_code == 200
        assert validate_status == bool(True)
        assert 'Password berhasil diperbaharui' in validate_message

    def test_update_password_wrong_token(self):

        param2 = {
            'old_password': '12345678',
            'new_password': '12345678',
            're_new_password': '12345678'
        }
        update_passwrod = requests.patch(settings.url_update_password_customer, params=param2, headers=settings.header_wrong_token_customer)

        validate_status = update_passwrod.json().get('success')
        validate_message = update_passwrod.json().get('message')

        assert update_passwrod.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_update_password_token_empty_value(self):

        param2 = {
            'old_password': '12345678',
            'new_password': '12345678',
            're_new_password': '12345678'
        }
        update_passwrod = requests.patch(settings.url_update_password_customer, params=param2, headers=settings.header_without_token_customer)

        validate_status = update_passwrod.json().get('success')
        validate_message = update_passwrod.json().get('message')

        assert update_passwrod.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_update_password_old_empty_value(self):

        param2 = {
            'old_password': '',
            'new_password': '12345678',
            're_new_password': '12345678'
        }
        update_passwrod = requests.patch(settings.url_update_password_customer, params=param2, headers=settings.header_with_token_customer)

        validate_status = update_passwrod.json().get('success')
        validate_message = update_passwrod.json().get('message')['old_password']

        assert update_passwrod.status_code == 422
        assert validate_status == bool(False)
        assert 'Kata sandi lama tidak boleh kosong.' in validate_message

    def test_update_password_without_param_old(self):

        param2 = {
            # 'old_password': '',
            'new_password': '12345678',
            're_new_password': '12345678'
        }
        update_passwrod = requests.patch(settings.url_update_password_customer, params=param2, headers=settings.header_with_token_customer)

        validate_status = update_passwrod.json().get('success')
        validate_message = update_passwrod.json().get('message')['old_password']

        assert update_passwrod.status_code == 422
        assert validate_status == bool(False)
        assert 'Kata sandi lama tidak boleh kosong.' in validate_message

    def test_update_password_old_wrong(self):

        param2 = {
            'old_password': 'zzzzzzzzzzz',
            'new_password': '12345678',
            're_new_password': '12345678'
        }
        update_passwrod = requests.patch(settings.url_update_password_customer, params=param2, headers=settings.header_with_token_customer)

        validate_status = update_passwrod.json().get('success')
        validate_message = update_passwrod.json().get('message')['old_password']

        assert update_passwrod.status_code == 422
        assert validate_status == bool(False)
        assert 'Kata sandi lama tidak sesuai atau salah' in validate_message

    def test_update_password_new_empty_value(self):

        param2 = {
            'old_password': '12345678',
            'new_password': '',
            're_new_password': '12345678'
        }
        update_passwrod = requests.patch(settings.url_update_password_customer, params=param2, headers=settings.header_with_token_customer)

        validate_status = update_passwrod.json().get('success')
        validate_message = update_passwrod.json().get('message')['new_password']

        assert update_passwrod.status_code == 422
        assert validate_status == bool(False)
        assert 'Kata sandi baru tidak boleh kosong.' in validate_message

    def test_update_password_without_param_new(self):

        param2 = {
            'old_password': '12345678',
            # 'new_password': '',
            're_new_password': '12345678'
        }
        update_passwrod = requests.patch(settings.url_update_password_customer, params=param2, headers=settings.header_with_token_customer)

        validate_status = update_passwrod.json().get('success')
        validate_message = update_passwrod.json().get('message')['new_password']

        assert update_passwrod.status_code == 422
        assert validate_status == bool(False)
        assert 'Kata sandi baru tidak boleh kosong.' in validate_message

    def test_update_password_new_value_kurang6(self):

        param2 = {
            'old_password': '12345678',
            'new_password': '123',
            're_new_password': '12345678'
        }
        update_passwrod = requests.patch(settings.url_update_password_customer, params=param2, headers=settings.header_with_token_customer)

        validate_status = update_passwrod.json().get('success')
        validate_message = update_passwrod.json().get('message')['new_password']

        assert update_passwrod.status_code == 422
        assert validate_status == bool(False)
        assert 'Kata sandi baru harus diantara 6 dan 20 karakter.' in validate_message

    def test_update_password_new_doesnt_match(self):

        param2 = {
            'old_password': '12345678',
            'new_password': '123456789',
            're_new_password': '12345678'
        }
        update_passwrod = requests.patch(settings.url_update_password_customer, params=param2, headers=settings.header_with_token_customer)

        validate_status = update_passwrod.json().get('success')
        validate_message = update_passwrod.json().get('message')['re_new_password']

        assert update_passwrod.status_code == 422
        assert validate_status == bool(False)
        assert 'Ulang kata sandi baru dan Kata sandi baru harus sama.' in validate_message

    def test_update_password_re_new_empty_value(self):

        param2 = {
            'old_password': '12345678',
            'new_password': '123456789',
            're_new_password': ''
        }
        update_passwrod = requests.patch(settings.url_update_password_customer, params=param2, headers=settings.header_with_token_customer)

        validate_status = update_passwrod.json().get('success')
        validate_message = update_passwrod.json().get('message')['re_new_password']

        assert update_passwrod.status_code == 422
        assert validate_status == bool(False)
        assert 'Ulang kata sandi baru tidak boleh kosong.' in validate_message

    def test_update_password_without_param_re_new(self):

        param2 = {
            'old_password': '12345678',
            'new_password': '123456789',
            # 're_new_password': ''
        }
        update_passwrod = requests.patch(settings.url_update_password_customer, params=param2, headers=settings.header_with_token_customer)

        validate_status = update_passwrod.json().get('success')
        validate_message = update_passwrod.json().get('message')['re_new_password']

        assert update_passwrod.status_code == 422
        assert validate_status == bool(False)
        assert 'Ulang kata sandi baru tidak boleh kosong.' in validate_message

