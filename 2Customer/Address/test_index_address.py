import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')

class TestCustomerIndexAddress:

    def test_index_address_normal(self):

        index = requests.get(settings.url_index_address_customer, headers=settings.header_with_token_customer)
        validate_status = index.json().get('success')
        validate_message = index.json().get('message')
        validate_data = index.json().get('data')[0]

        assert index.status_code == 200
        assert validate_status == bool(True)
        assert 'Data alamat berhasil ditemukan.' in validate_message
        assert_that(validate_data).contains_only('id', 'user_id', 'receiver', 'phone', 'address', 'kategori', 'title',
                                                 'note',
                                                 'created_at', 'updated_at', 'latitude', 'longitude')

    def test_index_address_token_empty_value(self):

        index = requests.get(settings.url_index_address_customer, headers=settings.header_without_token_customer)
        validate_status = index.json().get('success')
        validate_message = index.json().get('message')

        assert index.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message

    def test_index_address_wrong_token(self):
        index = requests.get(settings.url_index_address_customer, headers=settings.header_wrong_token_customer)
        validate_status = index.json().get('success')
        validate_message = index.json().get('message')

        assert index.status_code == 401
        assert validate_status == bool(False)
        assert 'Unauthorized' in validate_message