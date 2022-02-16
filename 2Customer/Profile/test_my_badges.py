import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerGetMyBadges:

    def test_get_badges_normal(self):
        my_badges = requests.get(settings.url_my_badges, headers=settings.header_with_token_customer)

        validate_status = my_badges.json().get('success')
        validate_message = my_badges.json().get('message')
        validate_data_badges = len(my_badges.json().get('data')['progress_badge'])

        assert my_badges.status_code == 200
        assert validate_status == bool(True)
        assert "Data customer berhasil ditemukan." in validate_message
        assert_that(validate_data_badges).is_equal_to(6)

    def test_get_badges_wrong_token(self):
        my_badges = requests.get(settings.url_my_badges, headers=settings.header_wrong_token_customer)

        validate_status = my_badges.json().get('success')
        validate_message = my_badges.json().get('message')

        assert my_badges.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message

    def test_get_badges_empty_token(self):
        my_badges = requests.get(settings.url_my_badges, headers=settings.header_without_token_customer)

        validate_status = my_badges.json().get('success')
        validate_message = my_badges.json().get('message')

        assert my_badges.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message

