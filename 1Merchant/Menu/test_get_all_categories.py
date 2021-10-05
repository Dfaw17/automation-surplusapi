import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')

class TestGetAllCategories:
    def test_get_all_categories_menu_normal(self):

        response = requests.get(settings.url_get_all_category_merchant, headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")
        validate_len_data = len(data.get("data"))
        validate_data = data.get("data")

        assert validate_status == bool(True)
        assert response.status_code == 200
        assert "Data menu ditemukan." in validate_message
        assert validate_len_data >= 1
        assert_that(validate_data[0]['nama']).is_equal_to('Makanan Berat')
        assert_that(validate_data[1]['nama']).is_equal_to('Makanan Vegan')
        assert_that(validate_data[2]['nama']).is_equal_to('Roti & Kue')
        assert_that(validate_data[3]['nama']).is_equal_to('Bahan Makanan')
        assert_that(validate_data[4]['nama']).is_equal_to('Buah & Sayur')
        assert_that(validate_data[5]['nama']).is_equal_to('Cemilan')
        assert_that(validate_data[6]['nama']).is_equal_to('Minuman')

    def test_get_all_categories_menu_wrong_token(self):
        response = requests.get(settings.url_get_all_category_merchant, headers=settings.header_wrong_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")

        assert validate_status == bool(False)
        assert response.status_code == 401
        assert "Unauthorized" in validate_message

    def test_get_all_categories_menu_empty_token(self):
        response = requests.get(settings.url_get_all_category_merchant, headers=settings.header_without_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")

        assert validate_status == bool(False)
        assert response.status_code == 401
        assert "Unauthorized" in validate_message