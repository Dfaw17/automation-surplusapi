import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')

class TestCustomerShowProfiles:

    def test_show_profile_normal(self):
        show_profile = requests.get(settings.url_show_profiles_customer, headers=settings.header_with_token_customer)

        validate_status = show_profile.json().get('success')
        validate_message = show_profile.json().get('message')
        validate_data_email = show_profile.json().get('data')['email']
        validate_data_name = show_profile.json().get('data')['name']
        validate_data_no_ponsel = show_profile.json().get('data')['no_ponsel']

        assert show_profile.status_code == 200
        assert validate_status == bool(True)
        assert 'Data customer berhasil ditemukan.' in validate_message
        assert validate_data_email == settings.email_has_registered
        assert_that(validate_data_name).is_not_none()
        assert_that(validate_data_no_ponsel).is_not_none()

    def test_show_profile_wrong_token(self):
        show_profile = requests.get(settings.url_show_profiles_customer, headers=settings.header_wrong_token_customer)

        validate_status = show_profile.json().get('success')
        validate_message = show_profile.json().get('message')

        assert show_profile.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_show_profile_token_empty_value(self):
        show_profile = requests.get(settings.url_show_profiles_customer, headers=settings.header_without_token_customer)

        validate_status = show_profile.json().get('success')
        validate_message = show_profile.json().get('message')

        assert show_profile.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message
