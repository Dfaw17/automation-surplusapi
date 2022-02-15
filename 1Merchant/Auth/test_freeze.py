import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestLogin:

    def test_login_freeze_normal(self):
        param = {
            "email": settings.email_merchant_freeze,
            "password": settings.pwd_merchant
        }

        response = requests.post(settings.url_login_merchant, data=param,
                                 headers={'Accept': 'application/json'})
        data = response.json()
        validate_message = data.get("message")
        validate_status = data.get("success")

        assert validate_message == "Outlet merchant telah dibekukan oleh sistem"
        assert validate_status == bool(False)
        assert response.status_code == 403
