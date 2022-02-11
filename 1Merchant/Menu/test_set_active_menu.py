import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestSetActiveMenu:

    def test_set_menu_active_today_normal(self):
        param = {
            "is_tomorrow": "0",
            "stock": "100",
            'max_active_date': '2023-12-12'
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(settings.menu_non_sayur) + "/active", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert "berhasil diaktifkan" in validate_message

    def test_set_menu_active_tomorrow_normal(self):
        param = {
            "is_tomorrow": "1",
            "stock": "100",
            'max_active_date': '2023-12-12'
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(settings.menu_non_sayur) + "/active", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert "berhasil diaktifkan" in validate_message

    def test_set_menu_active_stock_empty(self):
        param = {
            "max_active_date": "2022-12-12",
            "stock": "",
            "is_tomorrow": "0",
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(settings.menu_non_sayur) + "/active", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['stock']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "stock tidak boleh kosong." in validate_message

    def test_set_menu_active_stock_string(self):
        param = {
            "max_active_date": "2022-12-12",
            "stock": "qaqa",
            "is_tomorrow": "0",
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(settings.menu_non_sayur) + "/active", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['stock']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "stock harus berupa angka." in validate_message

    def test_set_menu_active_without_param_stock(self):
        param = {
            "max_active_date": "2022-12-12",
            "is_tomorrow": "0",
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(settings.menu_non_sayur) + "/active", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['stock']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "stock tidak boleh kosong." in validate_message

    def test_set_active_menu_max_active_date_empty(self):
        param = {
            "max_active_date": "",
            "stock": "100",
            "is_tomorrow": "0",
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(settings.menu_non_sayur) + "/active", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['max_active_date']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Tanggal maksimal menu aktif tidak boleh kosong." in validate_message

    def test_set_active_menu_max_active_date_kurang_today(self):
        param = {
            "max_active_date": "2021-12-12",
            "stock": "100",
            "is_tomorrow": "0",
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(settings.menu_non_sayur) + "/active", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['max_active_date']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Tanggal maksimal menu aktif tidak boleh kurang dari tanggal sekarang" in validate_message

    def test_set_active_menu_without_max_active_date(self):
        param = {
            # "max_active_date": "2021-12-12",
            "stock": "100",
            "is_tomorrow": "0",
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(settings.menu_non_sayur) + "/active", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['max_active_date']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Tanggal maksimal menu aktif tidak boleh kosong." in validate_message
