import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestPasswordReset:

    def test_reset_password_normal(self):
        param = {
            "email": settings.email_merchant
        }

        response = requests.post(settings.url_reset_pwd_merchant, data=param,
                                 headers={'Accept': 'application/json'})

        data = response.json()
        validate_status = data.get("success")
        validate_message = data.get("message")
        assert validate_status == bool(True)
        assert response.status_code == 200
        assert "Kami mengirimkan link untuk reset password ke e-mail" in validate_message

    def test_reset_password_wrong_email(self):
        param = {
            "email": settings.email_merchant_not_regist
        }

        response = requests.post(settings.url_reset_pwd_merchant, data=param,
                                 headers={'Accept': 'application/json'})

        data = response.json()
        validate_status = data.get("success")
        validate_message = data.get("message")
        assert validate_status == bool(False)
        assert response.status_code == 404
        assert "Kami tidak menemukan merchant dengan e-mail " in validate_message

    def test_reset_password_email_without_at(self):
        param = {
            "email": settings.email_merchant_without_at
        }

        response = requests.post(settings.url_reset_pwd_merchant, data=param,
                                 headers={'Accept': 'application/json'})

        data = response.json()
        validate_status = data.get("success")
        validate_message = data.get("message")["email"]
        assert validate_status == bool(False)
        assert response.status_code == 422
        assert "email harus merupakan alamat email yang valid." in validate_message

    def test_reset_password_email_with_space(self):
        param = {
            "email": settings.email_merchant_space
        }

        response = requests.post(settings.url_reset_pwd_merchant, data=param,
                                 headers={'Accept': 'application/json'})

        data = response.json()
        validate_status = data.get("success")
        validate_message = data.get("message")
        assert validate_status == bool(False)
        assert response.status_code == 404
        assert "Kami tidak menemukan merchant dengan e-mail" in validate_message

    def test_reset_password_email_empty(self):
        param = {
            "email": ""
        }

        response = requests.post(settings.url_reset_pwd_merchant, data=param,
                                 headers={'Accept': 'application/json'})

        data = response.json()
        validate_status = data.get("success")
        validate_message = data.get("message")["email"]
        assert validate_status == bool(False)
        assert response.status_code == 422
        assert "email tidak boleh kosong." in validate_message
