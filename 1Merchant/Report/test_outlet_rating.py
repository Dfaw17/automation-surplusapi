import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestMerchantOutletRating:

    def test_outlet_rating_normal(self):
        response = requests.get(settings.url_outlet_rating_merchant, headers=settings.header_with_token_merchant)

        validate_status = response.json().get('success')
        validate_message = response.json().get('message')
        validate_data = response.json().get('data')

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert "Data rating outlet berhasil ditemukan" in validate_message
        assert_that(validate_data).contains('rating_toko', 'terlaris', 'jarang_dibeli', 'rating', 'total_review',
                                            'rating_5', 'rating_4', 'rating_3', 'rating_2', 'rating_1','total_saved','total_saved_menu')

    def test_outlet_rating_wrong_token(self):
        response = requests.get(settings.url_outlet_rating_merchant, headers=settings.header_wrong_token_merchant)

        validate_status = response.json().get('success')
        validate_message = response.json().get('message')

        assert response.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message

    def test_outlet_rating_empty_token(self):
        response = requests.get(settings.url_outlet_rating_merchant, headers=settings.header_without_token_merchant)

        validate_status = response.json().get('success')
        validate_message = response.json().get('message')

        assert response.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message
