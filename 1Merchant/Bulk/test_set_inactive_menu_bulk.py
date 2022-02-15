import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestSetActiveMenu:

    def test_api_set_inactive_bulk_normal(self):
        param = {
            "menu_ids[0]": "4778",
        }

        response = requests.patch(settings.url_bulk_set_inactive, data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert "Menu berhasil di non-aktifkan" in validate_message

    def test_api_set_inactive_bulk_without_token(self):
        param = {
            "menu_ids[0]": "4778",
        }

        response = requests.patch(settings.url_bulk_set_inactive, data=param,
                                  headers=settings.header_without_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message

    def test_api_set_inactive_bulk_wrong_token(self):
        param = {
            "menu_ids[0]": "4778",
        }

        response = requests.patch(settings.url_bulk_set_inactive, data=param,
                                  headers=settings.header_wrong_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message

    def test_api_set_inactive_bulk_menu_menu_id_empty(self):
        param = {
            "menu_ids[0]": "",
        }

        response = requests.patch(settings.url_bulk_set_inactive, data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['menu_ids.0']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "menu_ids.0 harus berupa angka." in validate_message

    def test_api_set_inactive_bulk_menu_menu_id_wrong(self):
        param = {
            "menu_ids[0]": "99999",
        }

        response = requests.patch(settings.url_bulk_set_inactive, data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 404
        assert validate_status == bool(False)
        assert "Salah satu atau beberapa menu tidak ditemukan" in validate_message

    def test_api_set_inactive_bulk_menu_menu_id_string(self):
        param = {
            "menu_ids[0]": "aaa",
        }

        response = requests.patch(settings.url_bulk_set_inactive, data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['menu_ids.0']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "menu_ids.0 harus berupa angka." in validate_message

    def test_api_set_inactive_bulk_menu_menu_id_no_param(self):
        param = {
            # "menu_ids[0]": "4778",
        }

        response = requests.patch(settings.url_bulk_set_inactive, data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['menu_ids']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "menu ids tidak boleh kosong." in validate_message
