import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerRegisterOauth:

    def test_register_with_oauth_normal(self):
        param = {
            "email": settings.email_oauth,
            'origin': settings.origin,
            'id_from_origin': settings.origin_id
        }
        response = requests.post(settings.url_register_oauth_customer, data=param, headers={"Accept": "application/json"})
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')
        validate_email = data.get('data')['email']
        validate_auth = data.get('data')['auth_origin']

        assert response.status_code == 201
        assert validate_status == bool(True)
        assert 'Registrasi berhasil.' in validate_message
        assert validate_email == settings.email_oauth
        assert validate_auth == settings.origin

        login_oauth = requests.post(settings.url_login_auth_customer, data=param)
        token = login_oauth.json().get('token')
        headers2 = {
            "Authorization": f"Bearer {token}"
        }
        delete_oauth = requests.delete(settings.url_delete_account_customer, headers=headers2)

    def test_register_with_oauth_email_empty_value(self):
        param = {
            "email": '',
            'origin': settings.origin,
            'id_from_origin': settings.origin_id
        }
        response = requests.post(settings.url_register_oauth_customer, data=param, headers={"Accept": "application/json"})
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')['email']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'email tidak boleh kosong.' in validate_message

    def test_register_with_oauth_without_param_email(self):
        param = {
            # "email": '',
            'origin': settings.origin,
            'id_from_origin': settings.origin_id
        }
        response = requests.post(settings.url_register_oauth_customer, data=param, headers={"Accept": "application/json"})
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')['email']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'email tidak boleh kosong.' in validate_message

    def test_register_with_oauth_origin_empty_value(self):
        param = {
            "email": settings.email_oauth,
            'origin': '',
            'id_from_origin': settings.origin_id
        }
        response = requests.post(settings.url_register_oauth_customer, data=param, headers={"Accept": "application/json"})
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['origin']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'Sosial media tidak boleh kosong.' in validate_message

    def test_register_with_oauth_without_param_origin(self):
        param = {
            "email": settings.email_oauth,
            # 'origin': '',
            'id_from_origin': settings.origin_id
        }
        response = requests.post(settings.url_register_oauth_customer, data=param, headers={"Accept": "application/json"})
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['origin']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'Sosial media tidak boleh kosong.' in validate_message

    def test_register_with_oauth_id_empty_value(self):
        param = {
            "email": settings.email_oauth,
            'origin': settings.origin,
            'id_from_origin': ''
        }
        response = requests.post(settings.url_register_oauth_customer, data=param, headers={"Accept": "application/json"})
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['id_from_origin']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'id from origin tidak boleh kosong.' in validate_message

    def test_register_with_oauth_without_param_id(self):
        param = {
            "email": settings.email_oauth,
            'origin': settings.origin,
            # 'id_from_origin': ''
        }
        response = requests.post(settings.url_register_oauth_customer, data=param, headers={"Accept": "application/json"})
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['id_from_origin']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'id from origin tidak boleh kosong.' in validate_message

    def test_register_with_oauth_email_without_at(self):
        param = {
            'email': 'halogmail.com',
            'origin': settings.origin,
            'id_from_origin': settings.origin_id
        }
        response = requests.post(settings.url_register_oauth_customer, data=param, headers={"Accept": "application/json"})
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['email']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'email harus merupakan alamat email yang valid.' in validate_message

    def test_register_with_oauth_email_using_space(self):
        param = {
            'email': 'halo gmail.com',
            'origin': settings.origin,
            'id_from_origin': settings.origin_id
        }
        response = requests.post(settings.url_register_oauth_customer, data=param, headers={"Accept": "application/json"})
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['email']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'email harus merupakan alamat email yang valid.' in validate_message

    def test_register_with_oauth_wrong_social_media(self):
        param = {
            'email': settings.email_oauth,
            'origin': 'facebookk',
            'id_from_origin': settings.origin_id
        }
        response = requests.post(settings.url_register_oauth_customer, data=param, headers={"Accept": "application/json"})
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['origin']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'Sosial media hanya boleh Google atau Facebook' in validate_message
