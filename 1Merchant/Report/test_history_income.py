import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestOrderHistoryIncome:

    def test_history_income_normal(self):
        param = {
            "filter_by": "custom",
            "start_date": "2019-04-01",
            "end_date": "2022-04-01"
        }
        response = requests.get(settings.url_history_income_merchant, params=param,
                                headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")
        validate_data = data.get("data")
        validate_data_omset = data.get("data")['omset']

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert "Data riwayat pemasukan berhasil ditemukan" in validate_message
        assert_that(validate_data_omset).is_type_of(int)
        assert_that(validate_data).contains('omset', 'total_transaksi', 'date_range', 'total_item', 'orders')

    def test_history_income_wrong_token(self):
        param = {
            "filter_by": "custom",
            "start_date": "2019-04-01",
            "end_date": "2022-04-01"
        }
        response = requests.get(settings.url_history_income_merchant, params=param,
                                headers=settings.header_wrong_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message

    def test_history_income_token_empty_value(self):
        param = {
            "filter_by": "custom",
            "start_date": "2019-04-01",
            "end_date": "2022-04-01"
        }
        response = requests.get(settings.url_history_income_merchant, params=param,
                                headers=settings.header_wrong_token_merchant)
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_history_income_start_date_empty_value(self):
        param = {
            "filter_by": "custom",
            "start_date": "",
            "end_date": "2022-04-01"
        }
        response = requests.get(settings.url_history_income_merchant, params=param,
                                headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')['start_date']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'Tanggal awal tidak cocok dengan format Y-m-d.' in validate_message

    def test_history_income_without_param_start_sate(self):
        param = {
            "filter_by": "custom",
            "end_date": "2022-04-01"
        }
        response = requests.get(settings.url_history_income_merchant, params=param,
                                headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 500
        assert validate_status == bool(False)
        assert 'Aduh!' in validate_message

    def test_history_income_start_date_text_value(self):
        param = {
            "filter_by": "custom",
            "start_date": "aaa",
            "end_date": "2022-04-01"
        }
        response = requests.get(settings.url_history_income_merchant, params=param,
                                headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')['start_date']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Tanggal awal tidak cocok dengan format Y-m-d." in validate_message

    def test_history_income_start_date_wrong_format_value(self):
        param = {
            "filter_by": "custom",
            "start_date": "2019/01/01",
            "end_date": "2022-04-01"
        }
        response = requests.get(settings.url_history_income_merchant, params=param,
                                headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')['start_date']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'Tanggal awal tidak cocok dengan format Y-m-d.' in validate_message

    def test_history_income_end_date_empty_value(self):
        param = {
            "filter_by": "custom",
            "start_date": "2019-01-01",
            "end_date": ""
        }
        response = requests.get(settings.url_history_income_merchant, params=param,
                                headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')['end_date']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'Tanggal akhir tidak cocok dengan format Y-m-d.' in validate_message

    def test_history_income_without_param_end_date(self):
        param = {
            "filter_by": "custom",
            "start_date": "2019-01-01",
            # "end_date": ""
        }
        response = requests.get(settings.url_history_income_merchant, params=param,
                                headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 500
        assert validate_status == bool(False)
        assert 'Aduh' in validate_message

    def test_history_income_end_date_text_value(self):
        param = {
            "filter_by": "custom",
            "start_date": "2019-01-01",
            "end_date": "aaa"
        }
        response = requests.get(settings.url_history_income_merchant, params=param,
                                headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')['end_date']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'Tanggal akhir tidak cocok dengan format Y-m-d.' in validate_message

    def test_history_income_end_date_wrong_format_value(self):
        param = {
            "filter_by": "custom",
            "start_date": "2019-01-01",
            "end_date": "2022/01/01"
        }
        response = requests.get(settings.url_history_income_merchant, params=param,
                                headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get('success')
        validate_message = data.get('message')['end_date']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'Tanggal akhir tidak cocok dengan format Y-m-d.' in validate_message

    def test_history_income_normal_daily(self):
        param = {
            "filter_by": "day",
        }
        response = requests.get(settings.url_history_income_merchant, params=param,
                                headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert "riwayat pemasukan" in validate_message

    def test_history_income_normal_week(self):
        param = {
            "filter_by": "week",
        }
        response = requests.get(settings.url_history_income_merchant, params=param,
                                headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert "riwayat pemasukan" in validate_message

    def test_history_income_normal_month(self):
        param = {
            "filter_by": "month",
        }
        response = requests.get(settings.url_history_income_merchant, params=param,
                                headers=settings.header_with_token_merchant)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert "riwayat pemasukan" in validate_message



