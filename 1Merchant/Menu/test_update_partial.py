import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestUpdatePartial:

    def test_update_stock_kat_sayur(self):
        param = {
            "event": "stock",
            "stock": "777",
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(settings.menu_sayur) + "/partial", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')
        validate_stock = data.get('data')['stock']

        assert response.status_code == 201
        assert validate_status == bool(True)
        assert_that(validate_stock).is_equal_to(777)
        assert "Stock penjualan berhasil diubah" in validate_message

    def test_upadte_menu_active_max_active_date_normal(self):
        param = {
            "event": "max_active_date",
            "max_active_date": "2023-01-11",
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(settings.menu_sayur) + "/partial", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')
        validate = data.get('data')['max_active_date']

        assert response.status_code == 201
        assert validate_status == bool(True)
        assert_that(validate).is_equal_to("2023-01-11")
        assert "Masa aktif menu telah diubah" in validate_message

    def test_update_menu_active_stock_empty(self):
        param = {
            "event": "stock",
            "stock": "",
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(settings.menu_sayur) + "/partial", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['stock']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "stock tidak boleh kosong ketika event adalah stock." in validate_message

    def test_update_menu_active_stock_string_value(self):
        param = {
            "event": "stock",
            "stock": "aa",
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(settings.menu_sayur) + "/partial", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['stock']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "stock harus berupa angka." in validate_message

    def test_update_menu_active_without_param_stock(self):
        param = {
            "event": "stock",
            # "stock": "aa",
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(settings.menu_sayur) + "/partial", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['stock']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "stock tidak boleh kosong ketika event adalah stock." in validate_message

    def test_update_menu_max_active_date_empty(self):
        param = {
            "event": "max_active_date",
            "max_active_date": "",
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(settings.menu_sayur) + "/partial", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['max_active_date']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Tanggal maksimal menu aktif bukan format tanggal yang valid." in validate_message

    def test_update_menu_without_param_max_active_date(self):
        param = {
            "event": "max_active_date",
            # "max_active_date": "",
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(settings.menu_sayur) + "/partial", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 500
        assert validate_status == bool(False)
        assert "Aduh! Ada yang salah di sistem kami." in validate_message

    def test_update_menu_max_active_date_wrong_value(self):
        param = {
            "event": "max_active_date",
            "max_active_date": "aaa",
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(settings.menu_sayur) + "/partial", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['max_active_date']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Tanggal maksimal menu aktif bukan format tanggal yang valid." in validate_message
