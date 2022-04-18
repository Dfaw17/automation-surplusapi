import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerRegisterEmail:

    def test_register_with_email_normal(self):
        param = {
            "email": settings.fake_email,
            "password": settings.kata_sandi,
            "re-password": settings.kata_sandi
        }
        response = requests.post(settings.url_register_email_customer, data=param,
                                 headers={"Accept": "application/json"})
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')
        validate_data = data.get('data')['id']
        validate_email = data.get('data')['email']

        assert response.status_code == 201
        assert validate_status == bool(True)
        assert 'Registrasi berhasil.' in validate_message
        assert_that(validate_data).is_type_of(int)
        assert validate_email == settings.fake_email

    def test_register_with_email_sudah_terdaftar(self):
        param = {
            "email": settings.email_has_registered,
            "password": settings.kata_sandi,
            "re-password": settings.kata_sandi
        }
        response = requests.post(settings.url_register_email_customer, data=param,
                                 headers={"Accept": "application/json"})
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 404
        assert validate_status == bool(False)
        assert 'sudah terdaftar' in validate_message

    def test_register_with_email_empty_value(self):
        param = {
            "email": '',
            "password": settings.kata_sandi,
            "re-password": settings.kata_sandi
        }
        response = requests.post(settings.url_register_email_customer, data=param,
                                 headers={"Accept": "application/json"})
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')['email']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'email tidak boleh kosong.' in validate_message

    def test_register_with_email_without_param_email(self):
        param = {
            "email": '',
            "password": settings.kata_sandi,
            "re-password": settings.kata_sandi
        }
        response = requests.post(settings.url_register_email_customer, data=param,
                                 headers={"Accept": "application/json"})
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')['email']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'email tidak boleh kosong.' in validate_message

    def test_register_with_email_without_at(self):
        param = {
            "email": "halo gmail.com",
            "password": settings.kata_sandi,
            "re-password": settings.kata_sandi
        }
        response = requests.post(settings.url_register_email_customer, data=param,
                                 headers={"Accept": "application/json"})
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')['email']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'email harus merupakan alamat email yang valid.' in validate_message

    def test_register_with_email_using_space(self):
        param = {
            "email": "halo @gmail.com",
            "password": settings.kata_sandi,
            "re-password": settings.kata_sandi
        }
        response = requests.post(settings.url_register_email_customer, data=param,
                                 headers={"Accept": "application/json"})
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 404
        assert validate_status == bool(False)

    def test_register_with_email_password_empty_value(self):
        param = {
            "email": settings.fake_email,
            "password": '',
            "re-password": settings.kata_sandi
        }
        response = requests.post(settings.url_register_email_customer, data=param,
                                 headers={"Accept": "application/json"})
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')['password']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'Kata sandi tidak boleh kosong.' in validate_message

    def test_register_with_email_without_param_password(self):
        param = {
            "email": settings.fake_email,
            # "password": '',
            "re-password": settings.kata_sandi
        }
        response = requests.post(settings.url_register_email_customer, data=param,
                                 headers={"Accept": "application/json"})
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')['password']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'Kata sandi tidak boleh kosong.' in validate_message

    def test_register_with_email_repassword_empty_value(self):
        param = {
            "email": settings.fake_email,
            "password": settings.kata_sandi,
            "re-password": ''
        }
        response = requests.post(settings.url_register_email_customer, data=param,
                                 headers={"Accept": "application/json"})
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')['re-password']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 're-password tidak boleh kosong.' in validate_message

    def test_register_with_email_without_param_repassword(self):
        param = {
            "email": settings.fake_email,
            "password": settings.kata_sandi,
            # "re-password": ''
        }
        response = requests.post(settings.url_register_email_customer, data=param,
                                 headers={"Accept": "application/json"})
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')['re-password']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 're-password tidak boleh kosong.' in validate_message

    def test_register_with_email_pass_repass_doesnt_match(self):
        param = {
            "email": settings.fake_email,
            "password": settings.kata_sandi,
            "re-password": '12345679'
        }
        response = requests.post(settings.url_register_email_customer, data=param,
                                 headers={"Accept": "application/json"})
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')['re-password']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 're-password dan Kata sandi harus sama.' in validate_message