import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestSetInActiveMenu:

    def test_set_inactive_menu_normal(self):
        response = requests.patch(settings.url_set_inactive_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + "/inactive",
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert "berhasil di non-aktifkan" in validate_message

    def test_set_inactive_menu_wrong_token(self):
        response = requests.patch(settings.url_set_inactive_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + "/inactive",
                                  headers=settings.header_wrong_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message

    def test_set_inactive_menu_empty_token(self):
        response = requests.patch(settings.url_set_inactive_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + "/inactive",
                                  headers=settings.header_without_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message