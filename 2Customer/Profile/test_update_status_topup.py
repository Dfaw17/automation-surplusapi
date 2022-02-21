import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerUpdateStatusTopup:

    def test_update_status_topup_confirmation(self):
        data = {
            "amount": "15000",
            "bank_chosen[bank_name]": "BCA",
            "bank_chosen[account_name]": "PT EKONOMI SIKULAR INDONESIA",
            "bank_chosen[account_number]": "123459590",
        }
        req_topup = requests.post(settings.url_req_topup, data=data, headers=settings.header_with_token_customer)
        time.sleep(1)
        confirmation_topup = requests.post(settings.url_update_status_topup, data={"event": "already_transferred", },
                                           headers=settings.header_with_token_customer)
        time.sleep(1)
        cancel = requests.post(settings.url_update_status_topup, data={"event": "cancel", },
                               headers=settings.header_with_token_customer)

        validate_status = confirmation_topup.json().get('success')
        validate_msg = confirmation_topup.json().get('message')
        validate_data = confirmation_topup.json().get('data')['status']

        assert confirmation_topup.status_code == 200
        assert validate_status == bool(True)
        assert "Data status topup berhasil di update" in validate_msg
        assert "already_transferred" in validate_data

    def test_update_status_topup_cancel(self):
        data = {
            "amount": "15000",
            "bank_chosen[bank_name]": "BCA",
            "bank_chosen[account_name]": "PT EKONOMI SIKULAR INDONESIA",
            "bank_chosen[account_number]": "123459590",
        }
        req_topup = requests.post(settings.url_req_topup, data=data, headers=settings.header_with_token_customer)
        time.sleep(1)
        cancel = requests.post(settings.url_update_status_topup, data={"event": "cancel", },
                               headers=settings.header_with_token_customer)

        validate_status = cancel.json().get('success')
        validate_msg = cancel.json().get('message')
        validate_data = cancel.json().get('data')['status']

        assert cancel.status_code == 200
        assert validate_status == bool(True)
        assert "Data status topup berhasil di update" in validate_msg
        assert "canceled" in validate_data

    def test_update_status_topup_upload_proof(self):
        data = {
            "amount": "15000",
            "bank_chosen[bank_name]": "BCA",
            "bank_chosen[account_name]": "PT EKONOMI SIKULAR INDONESIA",
            "bank_chosen[account_number]": "123459590",
        }
        req_topup = requests.post(settings.url_req_topup, data=data, headers=settings.header_with_token_customer)
        time.sleep(1)
        file = {
            'image_proof': open("img/mie.jpg", 'rb'),
        }
        upload_proof = requests.post(settings.url_update_status_topup, files=file, data={"event": "upload_proof", },
                                     headers=settings.header_with_token_customer)
        time.sleep(1)
        cancel = requests.post(settings.url_update_status_topup, data={"event": "cancel", },
                               headers=settings.header_with_token_customer)

        validate_status = upload_proof.json().get('success')
        validate_msg = upload_proof.json().get('message')
        validate_data = upload_proof.json().get('data')['status']

        assert upload_proof.status_code == 200
        assert validate_status == bool(True)
        assert "Data status topup berhasil di update" in validate_msg
        assert "already_transferred" in validate_data

    def test_update_status_topup_upload_proof_without_img(self):
        data = {
            "amount": "15000",
            "bank_chosen[bank_name]": "BCA",
            "bank_chosen[account_name]": "PT EKONOMI SIKULAR INDONESIA",
            "bank_chosen[account_number]": "123459590",
        }
        req_topup = requests.post(settings.url_req_topup, data=data, headers=settings.header_with_token_customer)
        time.sleep(1)
        file = {
            # 'image_proof': open("img/mie.jpg", 'rb'),
        }
        upload_proof = requests.post(settings.url_update_status_topup, files=file, data={"event": "upload_proof", },
                                     headers=settings.header_with_token_customer)
        time.sleep(1)
        cancel = requests.post(settings.url_update_status_topup, data={"event": "cancel", },
                               headers=settings.header_with_token_customer)

        validate_status = upload_proof.json().get('success')
        validate_msg = upload_proof.json().get('message')['image_proof']

        assert upload_proof.status_code == 422
        assert validate_status == bool(False)
        assert "image proof tidak boleh kosong ketika event adalah upload_proof." in validate_msg

    def test_update_status_topup_wrong_token(self):
        data = {
            "amount": "15000",
            "bank_chosen[bank_name]": "BCA",
            "bank_chosen[account_name]": "PT EKONOMI SIKULAR INDONESIA",
            "bank_chosen[account_number]": "123459590",
        }
        req_topup = requests.post(settings.url_req_topup, data=data, headers=settings.header_with_token_customer)
        time.sleep(1)
        confirmation_topup = requests.post(settings.url_update_status_topup, data={"event": "already_transferred", },
                                           headers=settings.header_wrong_token_customer)
        time.sleep(1)
        cancel = requests.post(settings.url_update_status_topup, data={"event": "cancel", },
                               headers=settings.header_with_token_customer)

        validate_status = confirmation_topup.json().get('success')
        validate_msg = confirmation_topup.json().get('message')

        assert confirmation_topup.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_msg

    def test_update_status_topup_empty_token(self):
        data = {
            "amount": "15000",
            "bank_chosen[bank_name]": "BCA",
            "bank_chosen[account_name]": "PT EKONOMI SIKULAR INDONESIA",
            "bank_chosen[account_number]": "123459590",
        }
        req_topup = requests.post(settings.url_req_topup, data=data, headers=settings.header_with_token_customer)
        time.sleep(1)
        confirmation_topup = requests.post(settings.url_update_status_topup, data={"event": "already_transferred", },
                                           headers=settings.header_without_token_customer)
        time.sleep(1)
        cancel = requests.post(settings.url_update_status_topup, data={"event": "cancel", },
                               headers=settings.header_with_token_customer)

        validate_status = confirmation_topup.json().get('success')
        validate_msg = confirmation_topup.json().get('message')

        assert confirmation_topup.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_msg
