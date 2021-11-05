import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestBranchGeneral:

    def test_merchant_central_look_branch_active_menu(self):
        response = requests.get(settings.url_get_all_merchant_menu_merchant + f'?is_active=1&merchant_branch_id={settings.merchant_branch}',
                                headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert "Data menu berhasil ditemukan." in validate_message

    def test_merchant_central_look_branch_all_menu(self):
        response = requests.get(settings.url_get_all_merchant_menu_merchant + f'?merchant_branch_id={settings.merchant_branch}',
                                headers=settings.header_with_token_merchant)
        data = response.json()
        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert "Data menu berhasil ditemukan." in validate_message

    def test_merchnat_central_look_branch_history_trx(self):
        response = requests.get(
            settings.url_history_trx_merchant + f'?merchant_branch_id={settings.merchant_branch}',
            headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert "Data riwayat transaksi berhasil ditemukan" in validate_message

    def test_merchnat_central_look_branch_history_income(self):
        param = {
            "filter_by": "custom",
            "start_date": "2019-04-01",
            "end_date": "2022-04-01",
            "merchant_branch_id": f'{settings.merchant_branch}'
        }
        response = requests.get(settings.url_history_income_merchant, params=param,
                                headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert "Data riwayat pemasukan berhasil ditemukan" in validate_message

    def test_branch_login(self):
        param = {
            "email": settings.email_merchant_branch,
            "password": settings.pwd_merchant
        }

        response = requests.post(settings.url_login_merchant, data=param,
                                 headers={'Accept': 'application/json'})
        data = response.json()
        validate_message = data.get("message")
        validate_status = data.get("success")
        validate_data = data.get("data")['branch_status']

        assert validate_message == "Login merchant berhasil."
        assert validate_status == bool(True)
        assert response.status_code == 200
        assert_that(validate_data).is_equal_to('branch')

    def test_branch_get_menu(self):
        response = requests.get(settings.url_get_all_merchant_menu_merchant,
                                headers=settings.header_branch)
        data = response.json()
        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert "Data menu berhasil ditemukan." in validate_message

    def test_branch_get_menu_active(self):
        response = requests.get(settings.url_get_all_merchant_menu_merchant + '?is_active=1',
                                headers=settings.header_branch)
        data = response.json()
        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert "Data menu berhasil ditemukan." in validate_message

    def test_branch_set_active_menu(self):
        param = {
            "max_active_date": "2022-12-12",
            "stock": "100",
            "waktu_mulai_penjemputan": "01:00",
            "waktu_akhir_penjemputan": "23:00",
            'expired_date': '2023-12-12'
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(settings.menu_non_sayur) + "/active", data=param,
                                  headers=settings.header_branch)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert "berhasil diaktifkan" in validate_message

    def test_branch_update_stock(self):
        param = {
            "event": "stock",
            "stock": "777",
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(settings.menu_non_sayur) + "/partial", data=param,
                                  headers=settings.header_branch)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 201
        assert validate_status == bool(True)
        assert "Stock penjualan berhasil diubah" in validate_message

    def test_branch_update_time(self):
        param = {
            "event":"activate",
            "max_active_date": "2022-09-09",
            "waktu_mulai_penjemputan": "00:30",
            "waktu_akhir_penjemputan": "23:00"
        }

        response = requests.patch(settings.url_set_active_menu_merchant + str(settings.menu_non_sayur) + "/partial", data=param,
                                  headers=settings.header_branch)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 201
        assert validate_status == bool(True)
        assert 'Waktu pengambilan berhasil diubah' in validate_message

    def test_branch_history_trx(self):
        response = requests.get(settings.url_history_trx_merchant,headers=settings.header_branch)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert "Data riwayat transaksi berhasil ditemukan" in validate_message

    def test_branch_history_income(self):
        param = {
            "filter_by": "custom",
            "start_date": "2019-04-01",
            "end_date": "2022-04-01",
        }
        response = requests.get(settings.url_history_income_merchant, params=param,
                                headers=settings.header_branch)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert "Data riwayat pemasukan berhasil ditemukan" in validate_message

    def test_branch_profile(self):
        response = requests.get(settings.url_show_profile_merchant, headers=settings.header_branch)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")
        validate_data = data.get("data")["name"]
        validate_email = data.get("data")["email"]
        validate_outlet = data.get("data")["outlet"]
        validate_location = data.get("data")["location"]

        assert validate_status == bool(True)
        assert response.status_code == 200
        assert "Data merchant ditemukan." in validate_message
        assert_that(validate_data).is_not_empty()
        assert_that(validate_outlet).is_not_empty()
        assert_that(validate_location).is_not_empty()
        assert validate_email == settings.email_merchant_branch

