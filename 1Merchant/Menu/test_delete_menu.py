import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestDeleteMerchantMenu:

    def test_delete_menu_normal(self):
        response = requests.delete(settings.url_delete_menu_merchant + str(settings.var_deleted_menu()),
                                   headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 201
        assert validate_status == bool(True)
        assert "Data menu berhasil dihapus." in validate_message

    def test_delete_menu_wrong_id(self):
        response = requests.delete(settings.url_delete_menu_merchant + '10000',
                                   headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 500
        assert validate_status == bool(False)
        assert "Aduh!" in validate_message

    def test_delete_menu_empty_id(self):
        response = requests.delete(settings.url_delete_menu_merchant, headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 405
        assert validate_status == bool(False)
        assert 'Method Not Allowed' in validate_message

    def test_delete_menu_wrong_token(self):
        response = requests.delete(settings.url_delete_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']),
                                   headers=settings.header_wrong_token_merchant)

        data = response.json()
        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message

    def test_delete_menu_empty_token(self):
        response = requests.delete(settings.url_delete_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']),
                                   headers=settings.header_without_token_merchant)

        data = response.json()
        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message
