import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')

class TestMerchantBranchIndex:

    def test_index_branch_normal(self):
        branch = requests.get(settings.url_branch_merchant, headers=settings.header_with_token_merchant)

        validate_status = branch.json().get('success')
        validate_message = branch.json().get('message')
        validate_data = branch.json().get('data')

        assert branch.status_code == 200
        assert validate_status == bool(True)
        assert "Data cabang berhasil ditemukan." in validate_message
        assert_that(validate_data).is_not_none()
        assert_that(validate_data[0]).contains('id', 'name', 'email', 'status', 'area', 'merchant_logo')

    def test_index_branch_wrong_token(self):
        branch = requests.get(settings.url_branch_merchant, headers=settings.header_wrong_token_merchant)

        validate_status = branch.json().get('success')
        validate_message = branch.json().get('message')
        validate_data = branch.json().get('data')

        assert branch.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message

    def test_index_branch_token_empty(self):
        branch = requests.get(settings.url_branch_merchant, headers=settings.header_without_token_merchant)

        validate_status = branch.json().get('success')
        validate_message = branch.json().get('message')
        validate_data = branch.json().get('data')

        assert branch.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message
