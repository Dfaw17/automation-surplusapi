import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerGetMyPoints:

    def test_get_point_all(self):
        param = {
            "filter": "all"
        }
        my_badges = requests.get(settings.url_my_points, params=param, headers=settings.header_with_token_customer)

        validate_status = my_badges.json().get('success')
        validate_message = my_badges.json().get('message')

        assert my_badges.status_code == 200
        assert validate_status == bool(True)
        assert "Data histori point berhasil ditemukan." in validate_message

    def test_get_poit_filter(self):
        param = {
            "filter": "in"
        }
        my_badges = requests.get(settings.url_my_points, params=param, headers=settings.header_with_token_customer)

        validate_status = my_badges.json().get('success')
        validate_message = my_badges.json().get('message')

        assert my_badges.status_code == 200
        assert validate_status == bool(True)
        assert "Data histori point berhasil ditemukan." in validate_message

    def test_get_point_wrong_token(self):
        param = {
            "filter": "in"
        }
        my_badges = requests.get(settings.url_my_points, params=param, headers=settings.header_wrong_token_customer)

        validate_status = my_badges.json().get('success')
        validate_message = my_badges.json().get('message')

        assert my_badges.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message

    def test_get_point_token_empty(self):
        param = {
            "filter": "in"
        }
        my_badges = requests.get(settings.url_my_points, params=param, headers=settings.header_without_token_customer)

        validate_status = my_badges.json().get('success')
        validate_message = my_badges.json().get('message')

        assert my_badges.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message
