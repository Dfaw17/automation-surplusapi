import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestDeleteMerchantMenuBulk:

    def test_delete_bulk_menu_normal(self):
        data = {
            "menu_ids[0]": str(settings.var_deleted_menu())
        }
        response = requests.delete(settings.url_bulk_delete, params=data, headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 201
        assert validate_status == bool(True)
        assert "Data menu berhasil dihapus." in validate_message

    def test_api_set_delete_bulk_without_token(self):
        data = {
            "menu_ids[0]": str(settings.var_deleted_menu())
        }
        response = requests.delete(settings.url_bulk_delete, params=data, headers=settings.header_without_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message

    def test_api_set_delete_bulk_wrong_token(self):
        data = {
            "menu_ids[0]": str(settings.var_deleted_menu())
        }
        response = requests.delete(settings.url_bulk_delete, params=data, headers=settings.header_wrong_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message

    def test_api_set_delete_bulk_menu_menu_id_empty(self):
        data = {
            "menu_ids[0]": ''
        }
        response = requests.delete(settings.url_bulk_delete, params=data, headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")['menu_ids.0']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "menu_ids.0 harus berupa angka." in validate_message

    def test_api_set_delete_bulk_menu_menu_id_wrong(self):
        data = {
            "menu_ids[0]": '9999999'
        }
        response = requests.delete(settings.url_bulk_delete, params=data, headers=settings.header_with_token_merchant)
        data = response.json()
        print(data)
        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 404
        assert validate_status == bool(False)
        assert "Salah satu atau beberapa menu tidak ditemukan" in validate_message

    def test_api_set_delete_bulk_menu_menu_id_string(self):
        data = {
            "menu_ids[0]": 'aaa'
        }
        response = requests.delete(settings.url_bulk_delete, params=data, headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")['menu_ids.0']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "menu_ids.0 harus berupa angka." in validate_message

    def test_api_set_delete_bulk_menu_menu_id_no_param(self):
        data = {
            # "menu_ids[0]": 'aaa'
        }
        response = requests.delete(settings.url_bulk_delete, params=data, headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")['menu_ids']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "menu ids tidak boleh kosong." in validate_message
