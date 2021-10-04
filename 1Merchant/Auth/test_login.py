import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestLogin:

    def test_login_normal(self):
        param = {
            "email": settings.email_merchant,
            "password": settings.pwd_merchant
        }

        response = requests.post(settings.url_login_merchant, data=param,
                                 headers={'Accept': 'application/json'})
        data = response.json()
        validate_message = data.get("message")
        validate_status = data.get("success")
        validate_data = data.get("data")
        validate_token = data.get("token")

        assert validate_message == "Login merchant berhasil."
        assert validate_status == bool(True)
        assert response.status_code == 200
        assert_that(validate_data).contains_only('branch_status', 'is_freeze')
        assert_that(data).contains_only('success', 'message', 'data', 'token')
        assert_that(validate_token).is_not_none()

    def test_login_akun_belum_register(self):
        param = {
            "email": settings.email_merchant_not_regist,
            "password": settings.pwd_merchant
        }

        response = requests.post(settings.url_login_merchant, data=param,
                                 headers={'Accept': 'application/json'})
        data = response.json()
        validate_message = data.get("message")
        validate_status = data.get("success")

        assert "tidak ada atau belum disetujui." in validate_message
        assert validate_status == bool(False)
        assert response.status_code == 404

    def test_login_salah_email(self):
        param = {
            "email": settings.email_merchant_not_regist,
            "password": settings.pwd_merchant
        }

        response = requests.post(settings.url_login_merchant, data=param,
                                 headers={'Accept': 'application/json'})
        data = response.json()
        validate_message = data.get("message")
        validate_status = data.get("success")

        assert "tidak ada atau belum disetujui." in validate_message
        assert validate_status == bool(False)
        assert response.status_code == 404

    def test_login_salah_password(self):
        param = {
            "email": settings.email_merchant,
            "password": settings.pwd_merchant_wrong
        }

        response = requests.post(settings.url_login_merchant, data=param,
                                 headers={'Accept': 'application/json'})
        data = response.json()
        validate_message = data.get("message")
        validate_status = data.get("success")

        assert validate_message == "Email atau password salah."
        assert validate_status == bool(False)
        assert response.status_code == 404

    def test_login_empty_password(self):
        param = {
            "email": settings.email_merchant,
            "password": ""
        }

        response = requests.post(settings.url_login_merchant, data=param,
                                 headers={'Accept': 'application/json'})
        data = response.json()
        validate_message = data.get("message")["password"]
        validate_status = data.get("success")

        assert "Kata sandi tidak boleh kosong." in validate_message
        assert validate_status == bool(False)
        assert response.status_code == 422

    def test_login_empty_email(self):
        param = {
            "email": "",
            "password": settings.pwd_merchant
        }

        response = requests.post(settings.url_login_merchant, data=param,
                                 headers={'Accept': 'application/json'})
        data = response.json()
        validate_message = data.get("message")["email"]
        validate_status = data.get("success")

        assert "email tidak boleh kosong." in validate_message
        assert validate_status == bool(False)
        assert response.status_code == 422

    def test_login_without_at(self):
        param = {
            "email": settings.email_merchant_without_at,
            "password": settings.pwd_merchant
        }

        response = requests.post(settings.url_login_merchant, data=param,
                                 headers={'Accept': 'application/json'})
        data = response.json()
        validate_message = data.get("message")["email"]
        validate_status = data.get("success")

        assert "email harus merupakan alamat email yang valid." in validate_message
        assert validate_status == bool(False)
        assert response.status_code == 422

    def test_kata_sandi_kurang_char(self):
        param = {
            "email": settings.email_merchant,
            "password": settings.pwd_kurang_char
        }

        response = requests.post(settings.url_login_merchant, data=param,
                                 headers={'Accept': 'application/json'})
        data = response.json()
        validate_message = data.get("message")["password"]
        validate_status = data.get("success")

        assert "Kata sandi harus diantara 6 dan 20 karakter." in validate_message
        assert validate_status == bool(False)
        assert response.status_code == 422

    def test_login_normal_freeze_account(self):
        param = {
            "email": settings.email_merchant_freeze,
            "password": settings.pwd_merchant
        }

        response = requests.post(settings.url_login_merchant, data=param,
                                 headers={'Accept': 'application/json'})
        data = response.json()
        validate_message = data.get("message")
        validate_status = data.get("success")
        validate_freeze = data.get("data")["is_freeze"]

        assert "Outlet merchant telah dibekukan oleh sistem" in validate_message
        assert validate_status == bool(False)
        assert response.status_code == 403
        validate_freeze == bool(True)
