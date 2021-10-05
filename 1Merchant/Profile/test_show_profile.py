import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestShowProfile:

    def test_show_profile_normal(self):
        token = settings.var_login_merchant().json().get("token")
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {token}"
        }
        response = requests.get(settings.url_show_profile_merchant, headers=headers)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")
        validate_data = data.get("data")["name"]
        validate_email = data.get("data")["email"]
        validate_outlet = data.get("data")["outlet"]
        validate_location = data.get("data")["location"]

        assert validate_status == bool(True)
        assert response.status_code == 200
        assert "Data merchant ditemukan." in validate_message
        assert_that(validate_data).is_not_empty()
        assert_that(validate_outlet).is_not_empty()
        assert_that(validate_location).is_not_empty()
        assert validate_email == settings.email_merchant

    def test_show_profile_wrong_token(self):
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {settings.wrong_token_merchant}"
        }
        response = requests.get(settings.url_show_profile_merchant, headers=headers)
        data = response.json()
        validate_status = data.get("success")
        validate_message = data.get("message")

        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message
        assert response.status_code == 401

    def test_show_profile_empty_token(self):
        headers = {
            "Accept": "application/json",
            "Authorization": ""
        }
        response = requests.get(settings.url_show_profile_merchant, headers=headers)
        data = response.json()
        validate_status = data.get("success")
        validate_message = data.get("message")

        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message
        assert response.status_code == 401

    def test_show_profile_no_auth(self):
        response = requests.get(settings.url_show_profile_merchant)
        data = response.text

        assert "Unauthorized" in data
        assert response.status_code == 401
