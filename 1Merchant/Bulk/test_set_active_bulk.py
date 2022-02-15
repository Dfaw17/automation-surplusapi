import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestSetActiveMenu:

    def test_set_menu_active_bulk_tomorrow_normal(self):
        param = {
            "is_tomorrow": "1",
            'max_active_date': '2023-12-12',
            "stocks[0]": "991",
            "stocks[1]": "991",
            "menu_ids[0]": "4704",
            "menu_ids[1]": "4726",
        }

        response = requests.patch(settings.url_bulk_set_active, data=param, headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert "berhasil diaktifkan" in validate_message

    def test_set_menu_active_bulk_normal(self):
        param = {
            "is_tomorrow": "0",
            'max_active_date': '2023-12-12',
            "stocks[0]": "991",
            "stocks[1]": "991",
            "menu_ids[0]": "4704",
            "menu_ids[1]": "4726",
        }

        response = requests.patch(settings.url_bulk_set_active, data=param, headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert "berhasil diaktifkan" in validate_message

    def test_set_menu_api_set_active_menu_stock_more_1000(self):
        param = {
            "is_tomorrow": "0",
            'max_active_date': '2023-12-12',
            "stocks[0]": "2000",
            "stocks[1]": "2000",
            "menu_ids[0]": "4704",
            "menu_ids[1]": "4726",
        }

        response = requests.patch(settings.url_bulk_set_active, data=param, headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['stocks.0']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "stocks.0 tidak boleh lebih dari 999." in validate_message

    def test_api_set_active_menu_stock_menu_not_match(self):
        param = {
            "is_tomorrow": "0",
            'max_active_date': '2023-12-12',
            "stocks[0]": "991",
            # "stocks[1]": "991",
            "menu_ids[0]": "4704",
            "menu_ids[1]": "4726",
        }

        response = requests.patch(settings.url_bulk_set_active, data=param, headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 500
        assert validate_status == bool(False)
        assert "Aduh!" in validate_message

    def test_api_set_active_menu_token_empty(self):
        param = {
            "is_tomorrow": "0",
            'max_active_date': '2023-12-12',
            "stocks[0]": "991",
            "stocks[1]": "991",
            "menu_ids[0]": "4704",
            "menu_ids[1]": "4726",
        }

        response = requests.patch(settings.url_bulk_set_active, data=param,
                                  headers=settings.header_without_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message

    def test_api_set_active_menu_token_wrong(self):
        param = {
            "is_tomorrow": "0",
            'max_active_date': '2023-12-12',
            "stocks[0]": "991",
            "stocks[1]": "991",
            "menu_ids[0]": "4704",
            "menu_ids[1]": "4726",
        }

        response = requests.patch(settings.url_bulk_set_active, data=param,
                                  headers=settings.header_wrong_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message

    def test_api_set_active_menu_without_param_stock(self):
        param = {
            "is_tomorrow": "0",
            'max_active_date': '2023-12-12',
            "menu_ids[0]": "4704",
            # "menu_ids[1]": "4726",
            # "stocks[0]": "991",
            # "stocks[1]": "991",
        }

        response = requests.patch(settings.url_bulk_set_active, data=param, headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['stocks']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "stocks tidak boleh kosong." in validate_message

    def test_api_set_active_menu_stock_empty(self):
        param = {
            "is_tomorrow": "0",
            'max_active_date': '2023-12-12',
            "menu_ids[0]": "4704",
            # "menu_ids[1]": "4726",
            "stocks[0]": "",
            # "stocks[1]": "991",
        }

        response = requests.patch(settings.url_bulk_set_active, data=param, headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['stocks.0']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "stocks.0 harus berupa angka." in validate_message

    def test_api_set_active_menu_stock_string(self):
        param = {
            "is_tomorrow": "0",
            'max_active_date': '2023-12-12',
            "menu_ids[0]": "4704",
            # "menu_ids[1]": "4726",
            "stocks[0]": "aaa",
            # "stocks[1]": "991",
        }

        response = requests.patch(settings.url_bulk_set_active, data=param, headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['stocks.0']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "stocks.0 harus berupa angka." in validate_message

    def test_api_set_active_menu_stock_minus(self):
        param = {
            "is_tomorrow": "0",
            'max_active_date': '2023-12-12',
            "menu_ids[0]": "4704",
            # "menu_ids[1]": "4726",
            "stocks[0]": "-100",
            # "stocks[1]": "991",
        }

        response = requests.patch(settings.url_bulk_set_active, data=param, headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['stocks.0']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert  "stocks.0 setidaknya harus 1." in validate_message

    def test_api_set_active_menu_max_active_date_kurang_today(self):
        param = {
            "is_tomorrow": "0",
            'max_active_date': '2021-12-12',
            "menu_ids[0]": "4704",
            "menu_ids[1]": "4726",
            "stocks[0]": "100",
            "stocks[1]": "991",
        }

        response = requests.patch(settings.url_bulk_set_active, data=param, headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['max_active_date']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Tanggal maksimal menu aktif tidak boleh kurang dari tanggal sekarang" in validate_message

    def test_api_set_active_menu_max_active_date_null(self):
        param = {
            "is_tomorrow": "0",
            'max_active_date': '',
            "menu_ids[0]": "4704",
            "menu_ids[1]": "4726",
            "stocks[0]": "100",
            "stocks[1]": "991",
        }

        response = requests.patch(settings.url_bulk_set_active, data=param, headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['max_active_date']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Tanggal maksimal menu aktif tidak boleh kosong." in validate_message

    def test_api_set_active_menu_max_active_date_wrong_data(self):
        param = {
            "is_tomorrow": "0",
            'max_active_date': '17:00',
            "menu_ids[0]": "4704",
            "menu_ids[1]": "4726",
            "stocks[0]": "100",
            "stocks[1]": "991",
        }

        response = requests.patch(settings.url_bulk_set_active, data=param, headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['max_active_date']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Tanggal maksimal menu aktif bukan format tanggal yang valid." in validate_message

    def test_api_set_active_menu_without_param_max_active_date(self):
        param = {
            "is_tomorrow": "0",
            # 'max_active_date': '17:00',
            "menu_ids[0]": "4704",
            "menu_ids[1]": "4726",
            "stocks[0]": "100",
            "stocks[1]": "991",
        }

        response = requests.patch(settings.url_bulk_set_active, data=param, headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['max_active_date']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Tanggal maksimal menu aktif tidak boleh kosong." in validate_message
