import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestUpdateAvailable:

    def test_update_available_menu_normal(self):
        param = {
            'menu_ids[0]': settings.var_list_menu_merchant().json().get('data')[0]['id']
        }

        response = requests.post(settings.url_available_menu_merchant, data=param, headers=settings.header_branch)

        data = response.json()
        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 200
        assert_that(validate_status).is_equal_to(bool(True))
        assert_that(validate_message).is_equal_to('Menu berhasil ditampilkan dalam katalog')

    def test_update_available_menu_more_1(self):
        param = {
            'menu_ids[0]': settings.var_list_menu_merchant().json().get('data')[0]['id'],
            'menu_ids[1]': settings.var_list_menu_merchant().json().get('data')[1]['id']
        }

        response = requests.post(settings.url_available_menu_merchant, data=param, headers=settings.header_branch)

        data = response.json()
        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 200
        assert_that(validate_status).is_equal_to(bool(True))
        assert_that(validate_message).is_equal_to('Menu berhasil ditampilkan dalam katalog')

    def test_update_available_menu_wrong_id(self):
        param = {
            'menu_ids[0]': '99999'
        }

        response = requests.post(settings.url_available_menu_merchant, data=param, headers=settings.header_branch)

        data = response.json()
        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 400
        assert_that(validate_status).is_equal_to(bool(False))
        assert 'tidak tersedia pada merchant pusat' in validate_message

    def test_update_available_menu_wrong_token(self):
        param = {
            'menu_ids[0]': settings.var_list_menu_merchant().json().get('data')[0]['id']
        }

        response = requests.post(settings.url_available_menu_merchant, data=param, headers=settings.header_wrong_token_merchant)

        data = response.json()
        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 401
        assert_that(validate_status).is_equal_to(bool(False))
        assert_that(validate_message).is_equal_to('Unauthorized')

    def test_update_available_menu_without_token(self):
        param = {
            'menu_ids[0]': settings.var_list_menu_merchant().json().get('data')[0]['id']
        }

        response = requests.post(settings.url_available_menu_merchant, data=param, headers=settings.header_without_token_merchant)

        data = response.json()
        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 401
        assert_that(validate_status).is_equal_to(bool(False))
        assert_that(validate_message).is_equal_to('Unauthorized')
