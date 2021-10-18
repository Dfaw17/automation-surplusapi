import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerRegisterProgress:

    def test_register_progress_normal(self):
        param = {
            'email': settings.email_has_registered
        }
        headers = {
            "Accept": "application/json"
        }

        response = requests.get(settings.url_register_progress_customer, params=param, headers=headers)
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')
        validate_email = data.get('data')['customer']
        validate_status_akun = data.get('data')['status']

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert_that(validate_message).is_not_empty()
        validate_email == settings.email_has_registered
        assert_that(validate_status_akun).is_not_empty()

    def test_register_progress_without_param_email(self):
        param = {
            # 'email': settings.email_has_registered
        }
        headers = {
            "Accept": "application/json"
        }

        response = requests.get(settings.url_register_progress_customer, params=param, headers=headers)
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')['email']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'email tidak boleh kosong.' in validate_message

    def test_register_progress_email_value_empty(self):
        param = {
            'email': ''
        }
        headers = {
            "Accept": "application/json"
        }

        response = requests.get(settings.url_register_progress_customer, params=param, headers=headers)
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')['email']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'email tidak boleh kosong.' in validate_message

    def test_register_progress_email_without_at(self):
        param = {
            'email': "kopiruangvirtualgmail.com"
        }
        headers = {
            "Accept": "application/json"
        }

        response = requests.get(settings.url_register_progress_customer, params=param, headers=headers)
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')['email']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'email harus merupakan alamat email yang valid.' in validate_message
