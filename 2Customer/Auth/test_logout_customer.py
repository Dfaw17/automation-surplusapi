import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerLogout:

    def test_logout_normal(self):
        param = {
            'email': settings.email_has_registered,
            'password': settings.kata_sandi
        }
        headers = {
            "Accept": "application/json"
        }
        login = requests.post(settings.url_login_email_customer, params=param, headers=headers)
        time.sleep(5)
        param2 = {
            'token': login.json().get('token')
        }
        logout = requests.post(settings.url_logout_customer, params=param2, headers=headers)

        validate_status = logout.json().get('success')
        validate_message = logout.json().get('message')

        assert logout.status_code == 200
        assert validate_status == bool(True)
        assert 'User logged out successfully' in validate_message

    def test_logout_wrong_token(self):
        param = {
            'email': settings.email_has_registered,
            'password': settings.kata_sandi
        }
        headers = {
            "Accept": "application/json"
        }
        login = requests.post(settings.url_login_email_customer, params=param, headers=headers)
        time.sleep(1)
        param2 = {
            'token': settings.wrong_token_customer
        }
        logout = requests.post(settings.url_logout_customer, params=param2, headers=headers)

        validate_status = logout.json().get('success')
        validate_message = logout.json().get('message')

        assert logout.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_logout_token_empty_value(self):
        param = {
            'email': settings.email_has_registered,
            'password': settings.kata_sandi
        }
        headers = {
            "Accept": "application/json"
        }
        login = requests.post(settings.url_login_email_customer, params=param, headers=headers)
        time.sleep(1)
        param2 = {
            'token': ''
        }
        logout = requests.post(settings.url_logout_customer, params=param2, headers=headers)

        validate_status = logout.json().get('success')
        validate_message = logout.json().get('message')

        assert logout.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_logout_without_param_token(self):
        param = {
            'email': settings.email_has_registered,
            'password': settings.kata_sandi
        }
        headers = {
            "Accept": "application/json"
        }
        login = requests.post(settings.url_login_email_customer, params=param, headers=headers)
        time.sleep(1)
        param2 = {
            # 'token': ''
        }
        logout = requests.post(settings.url_logout_customer, params=param2, headers=headers)

        validate_status = logout.json().get('success')
        validate_message = logout.json().get('message')

        assert logout.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message
