import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')

class TestCustomerLoginEmail:
    def test_login_normal(self):
        param = {
            'email': settings.email_has_registered,
            'password': settings.kata_sandi
        }
        headers = {
            "Accept": "application/json"
        }

        response = requests.post(settings.url_login_email_customer, data=param, headers=headers)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')
        validate_token = data.get('token')

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert 'Login customer berhasil.' in validate_message
        assert_that(validate_token).is_not_empty()

    def test_login_email_empty_value(self):
        param = {
            'email': '',
            'password': settings.kata_sandi
        }
        headers = {
            "Accept": "application/json"
        }

        response = requests.post(settings.url_login_email_customer, data=param, headers=headers)
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')['email']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'email tidak boleh kosong.' in validate_message

    def test_login_without_param_email(self):
        param = {
            # 'email': '',
            'password': settings.kata_sandi
        }
        headers = {
            "Accept": "application/json"
        }

        response = requests.post(settings.url_login_email_customer, data=param, headers=headers)
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')['email']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'email tidak boleh kosong.' in validate_message

    def test_login_password_empty_value(self):
        param = {
            'email': settings.email_has_registered,
            'password': ''
        }
        headers = {
            "Accept": "application/json"
        }

        response = requests.post(settings.url_login_email_customer, data=param, headers=headers)
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')['password']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'Kata sandi tidak boleh kosong.' in validate_message

    def test_login_without_param_password(self):
        param = {
            'email': settings.email_has_registered,
            # 'password': ''
        }
        headers = {
            "Accept": "application/json"
        }

        response = requests.post(settings.url_login_email_customer, data=param, headers=headers)
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')['password']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'Kata sandi tidak boleh kosong.' in validate_message

    def test_login_wrong_password(self):
        param = {
            'email': settings.email_has_registered,
            'password': 'aq123wsderf'
        }
        headers = {
            "Accept": "application/json"
        }

        response = requests.post(settings.url_login_email_customer, data=param, headers=headers)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 404
        assert validate_status == bool(False)
        assert 'Email atau password salah.' in validate_message

    def test_login_email_with_space(self):
        param = {
            'email': 'kopiruangvirtual @gmail.com',
            'password': settings.kata_sandi
        }
        headers = {
            "Accept": "application/json"
        }

        response = requests.post(settings.url_login_email_customer, data=param, headers=headers)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 404
        assert validate_status == bool(False)
        assert 'Email atau password salah.' in validate_message

    def test_login_email_without_at(self):
        param = {
            'email': 'kopiruangvirtualgmail.com',
            'password': settings.kata_sandi
        }
        headers = {
            "Accept": "application/json"
        }

        response = requests.post(settings.url_login_email_customer, data=param, headers=headers)
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')['email']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'email harus merupakan alamat email yang valid.' in validate_message