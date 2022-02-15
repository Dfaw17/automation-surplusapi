import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerReportMenu:

    def test_get_report_types_normal(self):

        get_type = requests.get(settings.url_type_report_menu, headers=settings.header_with_token_customer)

        validate_status = get_type.json().get('success')
        validate_message = get_type.json().get('message')
        validate_data = len(get_type.json().get('data'))

        assert get_type.status_code == 200
        assert validate_status == bool(True)
        assert "Data tipe laporan berhasil didapatkan." in validate_message
        assert_that(validate_data).is_equal_to(4)

    def test_get_report_types_without_token(self):

        get_type = requests.get(settings.url_type_report_menu, headers=settings.header_without_token_customer)

        validate_status = get_type.json().get('success')
        validate_message = get_type.json().get('message')

        assert get_type.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message

    def test_get_report_type_token_wrong(self):

        get_type = requests.get(settings.url_type_report_menu, headers=settings.header_wrong_token_customer)

        validate_status = get_type.json().get('success')
        validate_message = get_type.json().get('message')

        assert get_type.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message