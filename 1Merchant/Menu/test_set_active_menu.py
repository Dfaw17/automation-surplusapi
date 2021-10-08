import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestSetActiveMenu:

    def test_set_menu_active_kat_non_sayur_today_normal(self):
        header = {"Authorization": f"Bearer {settings.var_login_merchant().json().get('token')}","Accept": "application/json"}
        param = {
            "is_tomorrow": "0",
            "stock": "100",
            "waktu_mulai_penjemputan": "01:00",
            "waktu_akhir_penjemputan": "23:00",
            'expired_date': '2023-12-12'
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + "/active", data=param,
                                  headers=header)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert "berhasil diaktifkan" in validate_message

    def test_set_menu_active_kat_sayur_today_normal(self):
        param = {
            "is_tomorrow": "0",
            "stock": "100",
            "waktu_mulai_penjemputan": "01:00",
            "waktu_akhir_penjemputan": "23:00",
            'max_storage_days': '5'
        }

        response = requests.patch(settings.url_set_active_menu_merchant + "628" + "/active", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert "berhasil diaktifkan" in validate_message

    def test_set_menu_active_kat_non_sayur_tomorrow_normal(self):
        param = {
            "is_tomorrow": "1",
            "stock": "100",
            "waktu_mulai_penjemputan": "01:00",
            "waktu_akhir_penjemputan": "23:00",
            'expired_date': '2023-12-12'
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + "/active", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert "berhasil diaktifkan" in validate_message

    def test_set_menu_active_kat_sayur_tomorrow_normal(self):
        param = {
            "is_tomorrow": "1",
            "stock": "100",
            "waktu_mulai_penjemputan": "01:00",
            "waktu_akhir_penjemputan": "23:00",
            'max_storage_days': '5'
        }

        response = requests.patch(settings.url_set_active_menu_merchant + "628" + "/active", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert "berhasil diaktifkan" in validate_message

    def test_set_menu_active_kat_non_sayur_special_time_normal(self):
        param = {
            "max_active_date": "2022-12-12",
            "stock": "100",
            "waktu_mulai_penjemputan": "01:00",
            "waktu_akhir_penjemputan": "23:00",
            'expired_date': '2023-12-12'
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + "/active", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert "berhasil diaktifkan" in validate_message

    def test_set_menu_active_kat_sayur_special_time_normal(self):
        param = {
            "max_active_date": "2022-12-12",
            "stock": "100",
            "waktu_mulai_penjemputan": "01:00",
            "waktu_akhir_penjemputan": "23:00",
            'max_storage_days': '3'
        }

        response = requests.patch(settings.url_set_active_menu_merchant + '628' + "/active", data=param,
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
            "waktu_mulai_penjemputan": "01:00",
            "waktu_akhir_penjemputan": "23:00",
            'expired_date': '2023-12-12'
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + "/active", data=param,
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
            "waktu_mulai_penjemputan": "01:00",
            "waktu_akhir_penjemputan": "23:00",
            'expired_date': '2023-12-12'
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + "/active", data=param,
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
            "waktu_mulai_penjemputan": "01:00",
            "waktu_akhir_penjemputan": "23:00",
            'expired_date': '2023-12-12'
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + "/active", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['stock']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "stock tidak boleh kosong." in validate_message

    def test_set_menu_active_waktu_mulai_empty(self):
        param = {
            "max_active_date": "2022-12-12",
            "stock": 100,
            "waktu_mulai_penjemputan": "",
            "waktu_akhir_penjemputan": "23:00",
            'expired_date': '2023-12-12'
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + "/active", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['waktu_mulai_penjemputan']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Waktu mulai penjemputan tidak boleh kosong." in validate_message

    def test_set_menu_active_without_param_waktu_mulai(self):
        param = {
            "max_active_date": "2022-12-12",
            "stock": 100,
            # "waktu_mulai_penjemputan": "",
            "waktu_akhir_penjemputan": "23:00",
            'expired_date': '2023-12-12'
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + "/active", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['waktu_mulai_penjemputan']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Waktu mulai penjemputan tidak boleh kosong." in validate_message

    def test_set_menu_active_waktu_mulai_string(self):
        param = {
            "max_active_date": "2022-12-12",
            "stock": 100,
            "waktu_mulai_penjemputan": "aaaa",
            "waktu_akhir_penjemputan": "23:00",
            'expired_date': '2023-12-12'
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + "/active", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['waktu_mulai_penjemputan']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Waktu mulai penjemputan tidak cocok dengan format H:i." in validate_message

    def test_set_menu_active_waktu_akhir_empty(self):
        param = {
            "max_active_date": "2022-12-12",
            "stock": 100,
            "waktu_mulai_penjemputan": "01:00",
            "waktu_akhir_penjemputan": "",
            'expired_date': '2023-12-12'
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + "/active", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['waktu_akhir_penjemputan']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Waktu akhir penjemputan tidak boleh kosong." in validate_message

    def test_set_menu_active_without_param_waktu_akhir(self):
        param = {
            "max_active_date": "2022-12-12",
            "stock": 100,
            "waktu_mulai_penjemputan": "01:00",
            # "waktu_akhir_penjemputan": "23:00",
            'expired_date': '2023-12-12'
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + "/active", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['waktu_akhir_penjemputan']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Waktu akhir penjemputan tidak boleh kosong." in validate_message

    def test_set_menu_active_waktu_akhir_string(self):
        param = {
            "max_active_date": "2022-12-12",
            "stock": 100,
            "waktu_mulai_penjemputan": "01:00",
            "waktu_akhir_penjemputan": "aa",
            'expired_date': '2023-12-12'
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + "/active", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['waktu_akhir_penjemputan']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Waktu akhir penjemputan tidak cocok dengan format H:i." in validate_message

    def test_set_menu_active_waktu_akhir_kurang_dari_awal(self):
        param = {
            "max_active_date": "2022-12-12",
            "stock": 100,
            "waktu_mulai_penjemputan": "17:00",
            "waktu_akhir_penjemputan": "13:00",
            'expired_date': '2023-12-12'
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + "/active", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['waktu_akhir_penjemputan']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Batas waktu penjemputan tidak benar" in validate_message

    def test_set_active_menu_wrong_id(self):
        param = {
            "is_tomorrow": "0",
            "stock": "100",
            "waktu_mulai_penjemputan": "01:00",
            "waktu_akhir_penjemputan": "23:00",
            'expired_date': '2023-12-12'
        }

        response = requests.patch(settings.url_set_active_menu_merchant + "999/active", data=param,headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 404
        assert validate_status == bool(False)
        assert "Menu tidak ditemukan" in validate_message

    def test_set_menu_active_kat_sayur_max_storage_days_empty(self):
        param = {
            "is_tomorrow": "0",
            "stock": "100",
            "waktu_mulai_penjemputan": "01:00",
            "waktu_akhir_penjemputan": "23:00",
            'max_storage_days': ''
        }

        response = requests.patch(settings.url_set_active_menu_merchant + "628" + "/active", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['max_storage_days']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Lama penyimpanan tidak boleh kosong." in validate_message

    def test_set_menu_active_kat_sayur_without_param_max_storage_days(self):
        param = {
            "is_tomorrow": "0",
            "stock": "100",
            "waktu_mulai_penjemputan": "01:00",
            "waktu_akhir_penjemputan": "23:00",
            # 'max_storage_days': ''
        }

        response = requests.patch(settings.url_set_active_menu_merchant + "628" + "/active", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['max_storage_days']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Lama penyimpanan tidak boleh kosong." in validate_message

    def test_set_menu_active_kat_sayur_max_storage_days_string(self):
        param = {
            "is_tomorrow": "0",
            "stock": "100",
            "waktu_mulai_penjemputan": "01:00",
            "waktu_akhir_penjemputan": "23:00",
            'max_storage_days': 'aaa'
        }

        response = requests.patch(settings.url_set_active_menu_merchant + "628" + "/active", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['max_storage_days']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Lama penyimpanan harus berupa angka." in validate_message

    def test_set_menu_active_kat_non_sayur_expired_date_empty(self):
        param = {
            "is_tomorrow": "0",
            "stock": "100",
            "waktu_mulai_penjemputan": "01:00",
            "waktu_akhir_penjemputan": "23:00",
            'expired_date': ''
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + "/active", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')

        assert response.status_code == 422
        assert validate_status == bool(False)

    def test_set_menu_active_kat_non_sayur_without_param_expired_date(self):
        param = {
            "is_tomorrow": "0",
            "stock": "100",
            "waktu_mulai_penjemputan": "01:00",
            "waktu_akhir_penjemputan": "23:00",
            # 'expired_date': ''
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + "/active", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['expired_date']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Tanggal kadaluarsa tidak boleh kosong." in validate_message

    def test_set_menu_active_kat_non_sayur_expired_date_string(self):
        param = {
            "is_tomorrow": "0",
            "stock": "100",
            "waktu_mulai_penjemputan": "01:00",
            "waktu_akhir_penjemputan": "23:00",
            'expired_date': 'aaa'
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + "/active", data=param,
                                  headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['expired_date']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Tanggal kadaluarsa bukan format tanggal yang valid." in validate_message
