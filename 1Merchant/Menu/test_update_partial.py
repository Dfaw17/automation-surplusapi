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

        response = requests.patch(settings.url_set_active_menu_merchant + settings.menu_sayur + "/partial", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')
        validate_stock = data.get('data')['stock']

        assert response.status_code == 201
        assert validate_status == bool(True)
        assert_that(validate_stock).is_equal_to(777)
        assert "Stock penjualan berhasil diubah" in validate_message

    def test_update_activate_kat_sayur(self):
        param = {
            "event": "activate",
            "max_active_date": "2022-09-09",
            "waktu_mulai_penjemputan": "01:00",
            "waktu_akhir_penjemputan": "23:00",
        }

        response = requests.patch(settings.url_set_active_menu_merchant + settings.menu_sayur + "/partial", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')
        validate_max_active_date = data.get('data')['max_active_date']
        validate_waktu_mulai_penjemputan = data.get('data')['waktu_mulai_penjemputan']
        validate_waktu_akhir_penjemputan = data.get('data')['waktu_akhir_penjemputan']

        assert response.status_code == 201
        assert validate_status == bool(True)
        assert "Waktu pengambilan berhasil diubah" in validate_message
        assert_that(validate_max_active_date).is_equal_to('2022-09-09')
        assert_that(validate_waktu_mulai_penjemputan).is_equal_to('01:00')
        assert_that(validate_waktu_akhir_penjemputan).is_equal_to('23:00')

    def test_update_expired_kat_sayur(self):
        param = {
            "event": "expired_limit ",
            "max_storage_days": "15",
        }

        response = requests.patch(settings.url_set_active_menu_merchant + settings.menu_sayur + "/partial", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')
        validate_max_storage_days = data.get('data')['max_storage_days']

        assert response.status_code == 201
        assert validate_status == bool(True)
        assert "Batas penyimpanan berhasil diperbarui" in validate_message
        assert_that(validate_max_storage_days).is_equal_to(15)

    def test_update_stock_non_kat_sayur(self):
        param = {
            "event": "stock",
            "stock": "777",
        }

        response = requests.patch(settings.url_set_active_menu_merchant + settings.menu_non_sayur + "/partial",
                                  data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')
        validate_stock = data.get('data')['stock']

        assert response.status_code == 201
        assert validate_status == bool(True)
        assert_that(validate_stock).is_equal_to(777)
        assert "Stock penjualan berhasil diubah" in validate_message

    def test_update_activate_kat_non_sayur(self):
        param = {
            "event": "activate",
            "max_active_date": "2022-09-09",
            "waktu_mulai_penjemputan": "01:00",
            "waktu_akhir_penjemputan": "23:00",
        }

        response = requests.patch(settings.url_set_active_menu_merchant + settings.menu_non_sayur + "/partial",
                                  data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')
        validate_max_active_date = data.get('data')['max_active_date']
        validate_waktu_mulai_penjemputan = data.get('data')['waktu_mulai_penjemputan']
        validate_waktu_akhir_penjemputan = data.get('data')['waktu_akhir_penjemputan']

        assert response.status_code == 201
        assert validate_status == bool(True)
        assert "Waktu pengambilan berhasil diubah" in validate_message
        assert_that(validate_max_active_date).is_equal_to('2022-09-09')
        assert_that(validate_waktu_mulai_penjemputan).is_equal_to('01:00')
        assert_that(validate_waktu_akhir_penjemputan).is_equal_to('23:00')

    def test_update_expired_kat_non_sayur(self):
        param = {
            "event": "expired_limit ",
            "expired_date": "2023-09-09",
        }

        response = requests.patch(settings.url_set_active_menu_merchant + settings.menu_non_sayur + "/partial",
                                  data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')
        validate_expired_date = data.get('data')['expired_date']

        assert response.status_code == 201
        assert validate_status == bool(True)
        assert "Batas penyimpanan berhasil diperbarui" in validate_message
        assert_that(validate_expired_date).is_equal_to("2023-09-09")

    def test_update_stock_non_kat_sayur_empty(self):
        param = {
            "event": "stock",
            "stock": "",
        }

        response = requests.patch(settings.url_set_active_menu_merchant + settings.menu_non_sayur + "/partial",
                                  data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['stock']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "stock tidak boleh kosong ketika event adalah stock." in validate_message

    def test_update_stock_non_kat_sayur_string(self):
        param = {
            "event": "stock",
            "stock": "aaa",
        }

        response = requests.patch(settings.url_set_active_menu_merchant + settings.menu_non_sayur + "/partial",
                                  data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['stock']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'stock harus berupa angka.' in validate_message

    def test_update_stock_non_kat_sayur_no_param(self):
        param = {
            "event": "stock",
            # "stock": "",
        }

        response = requests.patch(settings.url_set_active_menu_merchant + settings.menu_non_sayur + "/partial",
                                  data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['stock']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "stock tidak boleh kosong ketika event adalah stock." in validate_message

    def test_update_expired_kat_sayur_empty(self):
        param = {
            "event": "expired_limit ",
            "max_storage_days": "",
        }

        response = requests.patch(settings.url_set_active_menu_merchant + settings.menu_sayur + "/partial", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['max_storage_days']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Lama penyimpanan tidak boleh kosong." in validate_message

    def test_update_expired_kat_sayur_no_param(self):
        param = {
            "event": "expired_limit ",
            # "max_storage_days": "",
        }

        response = requests.patch(settings.url_set_active_menu_merchant + settings.menu_sayur + "/partial", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['max_storage_days']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Lama penyimpanan tidak boleh kosong." in validate_message

    def test_update_expired_kat_sayur_string(self):
        param = {
            "event": "expired_limit ",
            "max_storage_days": "aaa",
        }

        response = requests.patch(settings.url_set_active_menu_merchant + settings.menu_sayur + "/partial", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['max_storage_days']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Lama penyimpanan harus berupa angka." in validate_message

    def test_update_expired_kat_non_sayur_empty(self):
        param = {
            "event": "expired_limit ",
            "expired_date": "",
        }

        response = requests.patch(settings.url_set_active_menu_merchant + settings.menu_non_sayur + "/partial",
                                  data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['expired_date']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Tanggal kadaluarsa tidak boleh kosong." in validate_message

    def test_update_expired_kat_non_sayur_no_param(self):
        param = {
            "event": "expired_limit ",
            # "expired_date": "",
        }

        response = requests.patch(settings.url_set_active_menu_merchant + settings.menu_non_sayur + "/partial",
                                  data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['expired_date']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Tanggal kadaluarsa tidak boleh kosong." in validate_message

    def test_update_expired_kat_non_sayur_string(self):
        param = {
            "event": "expired_limit ",
            "expired_date": "aaa",
        }

        response = requests.patch(settings.url_set_active_menu_merchant + settings.menu_non_sayur + "/partial",
                                  data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['expired_date']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert'Tanggal kadaluarsa bukan format tanggal yang valid.' in validate_message
