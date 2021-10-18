import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerForgetPassword:

    def test_forget_password_normal(self):
        param = {
            'email': settings.email_has_registered
        }
        headers = {
            "Accept": "application/json"
        }

        response = requests.post(settings.url_reset_password_customer, params=param, headers=headers)
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')
        #
        assert response.status_code == 200
        assert validate_status == bool(True)
        assert 'Kami mengirimkan link untuk reset password ke e-mail' in validate_message

    def test_forget_password_email_wrong_data(self):
        param = {
            'email': settings.email_belum_register
        }
        headers = {
            "Accept": "application/json"
        }

        response = requests.post(settings.url_reset_password_customer, params=param, headers=headers)
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')
        assert response.status_code == 404
        assert validate_status == bool(False)
        assert 'Kami tidak menemukan user dengan e-mail ' in validate_message

    def test_Forget_password_email_without_at(self):
        param = {
            'email': 'kopiruangvirtualgmail.com'
        }
        headers = {
            "Accept": "application/json"
        }

        response = requests.post(settings.url_reset_password_customer, params=param, headers=headers)
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')['email']
        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'email harus merupakan alamat email yang valid.' in validate_message

    def test_forget_password_email_with_space(self):
        param = {
            'email': 'kopiruangvirtual gmail.com'
        }
        headers = {
            "Accept": "application/json"
        }

        response = requests.post(settings.url_reset_password_customer, params=param, headers=headers)
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')['email']
        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'email harus merupakan alamat email yang valid.' in validate_message

    def test_forget_password_email_empty_value(self):
        param = {
            'email': ''
        }
        headers = {
            "Accept": "application/json"
        }

        response = requests.post(settings.url_reset_password_customer, params=param, headers=headers)
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')['email']
        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'email tidak boleh kosong.' in validate_message

    def test_forget_password_without_param_email(self):
        param = {
            # 'email': ''
        }
        headers = {
            "Accept": "application/json"
        }

        response = requests.post(settings.url_reset_password_customer, params=param, headers=headers)
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')['email']
        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'email tidak boleh kosong.' in validate_message
