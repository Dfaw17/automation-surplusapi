import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestLogout:

    def test_logout_normal(self):
        token = settings.var_login_merchant().json().get("token")
        param = {
            "token": token
        }

        response = requests.post(settings.url_logout_merchant, data=param,
                                 headers={'Accept': 'application/json'})

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert validate_status == bool(True)
        assert response.status_code == 200
        assert validate_message == "User logged out successfully"

    def test_logout_wrong_token(self):
        param = {
            "token": "WRONG TOKEN !!!"
        }

        response = requests.post(settings.url_logout_merchant, data=param,
                                 headers={'Accept': 'application/json'})

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert validate_status == bool(False)
        assert response.status_code == 401
        assert validate_message == "Unauthorized"

    def test_logout_empty_token(self):
        response = requests.post(settings.url_logout_merchant, headers={'Accept': 'application/json'})

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert validate_status == bool(False)
        assert response.status_code == 401
        assert validate_message == "Unauthorized"
