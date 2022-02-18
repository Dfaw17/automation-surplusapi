import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerRequestTopup:

    def test_create_topup_normal(self):
        data = {
            "amount": "15000",
            "bank_chosen[bank_name]": "BCA",
            "bank_chosen[account_name]": "PT EKONOMI SIKULAR INDONESIA",
            "bank_chosen[account_number]": "123459590",
        }
        req_topup = requests.post(settings.url_req_topup, data=data, headers=settings.header_with_token_customer)
        time.sleep(1)
        cancel_topup = requests.post(settings.url_update_status_topup, data={"event": "cancel", },
                                     headers=settings.header_with_token_customer)

        validate_status = req_topup.json().get('success')
        validate_msg = req_topup.json().get('message')
        validate_ammount = req_topup.json().get('data')['amount']
        validate_bank_name = req_topup.json().get('data')['bank_chosen']['bank_name']
        validate_bank_account = req_topup.json().get('data')['bank_chosen']['account_name']
        validate_bank_number = req_topup.json().get('data')['bank_chosen']['account_number']

        assert req_topup.status_code == 201
        assert validate_status == bool(True)
        assert "Data topup dibuat" in validate_msg
        assert_that(validate_ammount).is_equal_to(15000)
        assert_that(validate_bank_name).is_equal_to("BCA")
        assert_that(validate_bank_account).is_equal_to("PT EKONOMI SIKULAR INDONESIA")
        assert_that(validate_bank_number).is_equal_to("123459590")

    def test_create_topup_twice(self):
        data = {
            "amount": "15000",
            "bank_chosen[bank_name]": "BCA",
            "bank_chosen[account_name]": "PT EKONOMI SIKULAR INDONESIA",
            "bank_chosen[account_number]": "123459590",
        }
        req_topup = requests.post(settings.url_req_topup, data=data, headers=settings.header_with_token_customer)
        time.sleep(1)
        req_topup2 = requests.post(settings.url_req_topup, data=data, headers=settings.header_with_token_customer)
        time.sleep(1)
        cancel_topup = requests.post(settings.url_update_status_topup, data={"event": "cancel", },
                                     headers=settings.header_with_token_customer)

        validate_status = req_topup2.json().get('success')
        validate_msg = req_topup2.json().get('message')

        assert req_topup2.status_code == 400
        assert validate_status == bool(False)
        assert "Masih ada data top-up yang belum selesai diproses" in validate_msg

    def test_create_topup_kurang_10000(self):
        data = {
            "amount": "7000",
            "bank_chosen[bank_name]": "BCA",
            "bank_chosen[account_name]": "PT EKONOMI SIKULAR INDONESIA",
            "bank_chosen[account_number]": "123459590",
        }
        req_topup = requests.post(settings.url_req_topup, data=data, headers=settings.header_with_token_customer)

        validate_status = req_topup.json().get('success')
        validate_msg = req_topup.json().get('message')['amount']

        assert req_topup.status_code == 422
        assert validate_status == bool(False)
        assert "Minimal top-up Rp10.000" in validate_msg

    def test_create_topup_lebih_10000000(self):
        data = {
            "amount": "15000000",
            "bank_chosen[bank_name]": "BCA",
            "bank_chosen[account_name]": "PT EKONOMI SIKULAR INDONESIA",
            "bank_chosen[account_number]": "123459590",
        }
        req_topup = requests.post(settings.url_req_topup, data=data, headers=settings.header_with_token_customer)

        validate_status = req_topup.json().get('success')
        validate_msg = req_topup.json().get('message')['amount']

        assert req_topup.status_code == 422
        assert validate_status == bool(False)
        assert "Maksimal top-up Rp10.000.000" in validate_msg

    def test_craete_topup_bank_name_empty(self):
        data = {
            "amount": "15000",
            "bank_chosen[bank_name]": "",
            "bank_chosen[account_name]": "PT EKONOMI SIKULAR INDONESIA",
            "bank_chosen[account_number]": "123459590",
        }
        req_topup = requests.post(settings.url_req_topup, data=data, headers=settings.header_with_token_customer)

        validate_status = req_topup.json().get('success')
        validate_msg = req_topup.json().get('message')["bank_chosen.bank_name"]

        assert req_topup.status_code == 422
        assert validate_status == bool(False)
        assert "bank chosen.bank name tidak boleh kosong." in validate_msg

    def test_craete_topup_bank_name_integer(self):
        data = {
            "amount": "15000",
            "bank_chosen[bank_name]": "123",
            "bank_chosen[account_name]": "PT EKONOMI SIKULAR INDONESIA",
            "bank_chosen[account_number]": "123459590",
        }
        req_topup = requests.post(settings.url_req_topup, data=data, headers=settings.header_with_token_customer)

        validate_status = req_topup.json().get('success')
        validate_msg = req_topup.json().get('message')["bank_chosen.bank_name"]

        assert req_topup.status_code == 422
        assert validate_status == bool(False)
        assert "bank chosen.bank name yang dipilih tidak tersedia." in validate_msg

    def test_craete_topup_without_bank_name(self):
        data = {
            "amount": "15000",
            # "bank_chosen[bank_name]": "",
            "bank_chosen[account_name]": "PT EKONOMI SIKULAR INDONESIA",
            "bank_chosen[account_number]": "123459590",
        }
        req_topup = requests.post(settings.url_req_topup, data=data, headers=settings.header_with_token_customer)

        validate_status = req_topup.json().get('success')
        validate_msg = req_topup.json().get('message')["bank_chosen.bank_name"]

        assert req_topup.status_code == 422
        assert validate_status == bool(False)
        assert "bank chosen.bank name tidak boleh kosong." in validate_msg

    def test_craete_topup_without_bank_account(self):
        data = {
            "amount": "15000",
            "bank_chosen[bank_name]": "BCA",
            # "bank_chosen[account_name]": "PT EKONOMI SIKULAR INDONESIA",
            "bank_chosen[account_number]": "123459590",
        }
        req_topup = requests.post(settings.url_req_topup, data=data, headers=settings.header_with_token_customer)

        validate_status = req_topup.json().get('success')
        validate_msg = req_topup.json().get('message')["bank_chosen.account_name"]

        assert req_topup.status_code == 422
        assert validate_status == bool(False)
        assert "bank chosen.account name tidak boleh kosong." in validate_msg

    def test_craete_topup_bank_account_empty(self):
        data = {
            "amount": "15000",
            "bank_chosen[bank_name]": "BCA",
            "bank_chosen[account_name]": "",
            "bank_chosen[account_number]": "123459590",
        }
        req_topup = requests.post(settings.url_req_topup, data=data, headers=settings.header_with_token_customer)

        validate_status = req_topup.json().get('success')
        validate_msg = req_topup.json().get('message')["bank_chosen.account_name"]

        assert req_topup.status_code == 422
        assert validate_status == bool(False)
        assert "bank chosen.account name tidak boleh kosong." in validate_msg

    def test_craete_topup_bank_account_int(self):
        data = {
            "amount": "15000",
            "bank_chosen[bank_name]": "BCA",
            "bank_chosen[account_name]": "123",
            "bank_chosen[account_number]": "123459590",
        }
        req_topup = requests.post(settings.url_req_topup, data=data, headers=settings.header_with_token_customer)
        time.sleep(1)
        cancel_topup = requests.post(settings.url_update_status_topup, data={"event": "cancel", },
                                     headers=settings.header_with_token_customer)

        validate_status = req_topup.json().get('success')
        validate_msg = req_topup.json().get('message')
        validate_ammount = req_topup.json().get('data')['amount']
        validate_bank_name = req_topup.json().get('data')['bank_chosen']['bank_name']
        validate_bank_account = req_topup.json().get('data')['bank_chosen']['account_name']
        validate_bank_number = req_topup.json().get('data')['bank_chosen']['account_number']

        assert req_topup.status_code == 201
        assert validate_status == bool(True)
        assert "Data topup dibuat" in validate_msg
        assert_that(validate_ammount).is_equal_to(15000)
        assert_that(validate_bank_name).is_equal_to("BCA")
        assert_that(validate_bank_account).is_equal_to("123")
        assert_that(validate_bank_number).is_equal_to("123459590")

    def test_craete_topup_without_bank_account_number(self):
        data = {
            "amount": "15000",
            "bank_chosen[bank_name]": "BCA",
            "bank_chosen[account_name]": "PT EKONOMI SIKULAR INDONESIA",
            # "bank_chosen[account_number]": "123459590",
        }
        req_topup = requests.post(settings.url_req_topup, data=data, headers=settings.header_with_token_customer)

        validate_status = req_topup.json().get('success')
        validate_msg = req_topup.json().get('message')["bank_chosen.account_number"]

        assert req_topup.status_code == 422
        assert validate_status == bool(False)
        assert "bank chosen.account number tidak boleh kosong." in validate_msg

    def test_craete_topup_bank_account_number_empty(self):
        data = {
            "amount": "15000",
            "bank_chosen[bank_name]": "BCA",
            "bank_chosen[account_name]": "PT EKONOMI SIKULAR INDONESIA",
            "bank_chosen[account_number]": "",
        }
        req_topup = requests.post(settings.url_req_topup, data=data, headers=settings.header_with_token_customer)

        validate_status = req_topup.json().get('success')
        validate_msg = req_topup.json().get('message')["bank_chosen.account_number"]

        assert req_topup.status_code == 422
        assert validate_status == bool(False)
        assert "bank chosen.account number tidak boleh kosong." in validate_msg

    def test_craete_topup_bank_account_number_string(self):
        data = {
            "amount": "15000",
            "bank_chosen[bank_name]": "BCA",
            "bank_chosen[account_name]": "PT EKONOMI SIKULAR INDONESIA",
            "bank_chosen[account_number]": "aaa",
        }
        req_topup = requests.post(settings.url_req_topup, data=data, headers=settings.header_with_token_customer)
        time.sleep(1)
        cancel_topup = requests.post(settings.url_update_status_topup, data={"event": "cancel", },
                                     headers=settings.header_with_token_customer)

        validate_status = req_topup.json().get('success')
        validate_msg = req_topup.json().get('message')
        validate_ammount = req_topup.json().get('data')['amount']
        validate_bank_name = req_topup.json().get('data')['bank_chosen']['bank_name']
        validate_bank_account = req_topup.json().get('data')['bank_chosen']['account_name']
        validate_bank_number = req_topup.json().get('data')['bank_chosen']['account_number']

        assert req_topup.status_code == 201
        assert validate_status == bool(True)
        assert "Data topup dibuat" in validate_msg
        assert_that(validate_ammount).is_equal_to(15000)
        assert_that(validate_bank_name).is_equal_to("BCA")
        assert_that(validate_bank_account).is_equal_to("PT EKONOMI SIKULAR INDONESIA")
        assert_that(validate_bank_number).is_equal_to("aaa")
