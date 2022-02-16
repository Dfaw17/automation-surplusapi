import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerReportMenuCreate:

    def test_post_report_menu_normal(self):
        data = {
            "menu_stock_id": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0]['stock_id'],
            "menu_report_type_id": "2",
            "reason": "Pokoknya pingin report aja dah."
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
        }
        post_type = requests.post(settings.url_create_report_menu, data=data, files=file,
                                  headers=settings.header_with_token_customer)

        validate_status = post_type.json().get('success')
        validate_message = post_type.json().get('message')

        assert post_type.status_code == 201
        assert validate_status == bool(True)
        assert "Data laporan berhasil ditambahkan." in validate_message

    def test_post_report_menu_without_token(self):
        data = {
            "menu_stock_id": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0]['stock_id'],
            "menu_report_type_id": "2",
            "reason": "Pokoknya pingin report aja dah."
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
        }
        post_type = requests.post(settings.url_create_report_menu, data=data, files=file,
                                  headers=settings.header_without_token_customer)

        validate_status = post_type.json().get('success')
        validate_message = post_type.json().get('message')

        assert post_type.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message

    def test_post_reprot_menu_token_wrong(self):
        data = {
            "menu_stock_id": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0]['stock_id'],
            "menu_report_type_id": "2",
            "reason": "Pokoknya pingin report aja dah."
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
        }
        post_type = requests.post(settings.url_create_report_menu, data=data, files=file,
                                  headers=settings.header_wrong_token_customer)

        validate_status = post_type.json().get('success')
        validate_message = post_type.json().get('message')

        assert post_type.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message

    def test_post_report_menu_stock_id_empty(self):
        data = {
            # "menu_stock_id": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0]['stock_id'],
            "menu_report_type_id": "2",
            "reason": "Pokoknya pingin report aja dah."
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
        }
        post_type = requests.post(settings.url_create_report_menu, data=data, files=file,
                                  headers=settings.header_with_token_customer)

        validate_status = post_type.json().get('success')
        validate_message = post_type.json().get('message')['menu_stock_id']

        assert post_type.status_code == 422
        assert validate_status == bool(False)
        assert "menu stock id tidak boleh kosong." in validate_message

    def test_post_report_menu_without_stock_id(self):
        data = {
            "menu_stock_id": "",
            "menu_report_type_id": "2",
            "reason": "Pokoknya pingin report aja dah."
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
        }
        post_type = requests.post(settings.url_create_report_menu, data=data, files=file,
                                  headers=settings.header_with_token_customer)

        validate_status = post_type.json().get('success')
        validate_message = post_type.json().get('message')['menu_stock_id']

        assert post_type.status_code == 422
        assert validate_status == bool(False)
        assert "menu stock id tidak boleh kosong." in validate_message

    def test_post_report_menu_stock_id_wrong(self):
        data = {
            "menu_stock_id": "9999999",
            "menu_report_type_id": "2",
            "reason": "Pokoknya pingin report aja dah."
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
        }
        post_type = requests.post(settings.url_create_report_menu, data=data, files=file,
                                  headers=settings.header_with_token_customer)

        validate_status = post_type.json().get('success')
        validate_message = post_type.json().get('message')

        assert post_type.status_code == 400
        assert validate_status == bool(False)
        assert "Data stock tidak ditemukan." in validate_message

    def test_post_report_menu_stock_id_string(self):
        data = {
            "menu_stock_id": "aaa",
            "menu_report_type_id": "2",
            "reason": "Pokoknya pingin report aja dah."
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
        }
        post_type = requests.post(settings.url_create_report_menu, data=data, files=file,
                                  headers=settings.header_with_token_customer)

        validate_status = post_type.json().get('success')
        validate_message = post_type.json().get('message')['menu_stock_id']

        assert post_type.status_code == 422
        assert validate_status == bool(False)
        assert "menu stock id harus berupa angka." in validate_message

    def test_post_report_menu_without_type_id(self):
        data = {
            "menu_stock_id": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0]['stock_id'],
            # "menu_report_type_id": "2",
            "reason": "Pokoknya pingin report aja dah."
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
        }
        post_type = requests.post(settings.url_create_report_menu, data=data, files=file,
                                  headers=settings.header_with_token_customer)

        validate_status = post_type.json().get('success')
        validate_message = post_type.json().get('message')['menu_report_type_id']

        assert post_type.status_code == 422
        assert validate_status == bool(False)
        assert "menu report type id tidak boleh kosong." in validate_message

    def test_post_report_menu_type_id_empty(self):
        data = {
            "menu_stock_id": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0]['stock_id'],
            "menu_report_type_id": "",
            "reason": "Pokoknya pingin report aja dah."
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
        }
        post_type = requests.post(settings.url_create_report_menu, data=data, files=file,
                                  headers=settings.header_with_token_customer)

        validate_status = post_type.json().get('success')
        validate_message = post_type.json().get('message')['menu_report_type_id']

        assert post_type.status_code == 422
        assert validate_status == bool(False)
        assert "menu report type id tidak boleh kosong." in validate_message

    def test_post_report_menu_type_id_wrong_value(self):
        data = {
            "menu_stock_id": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0]['stock_id'],
            "menu_report_type_id": "999",
            "reason": "Pokoknya pingin report aja dah."
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
        }
        post_type = requests.post(settings.url_create_report_menu, data=data, files=file,
                                  headers=settings.header_with_token_customer)

        validate_status = post_type.json().get('success')
        validate_message = post_type.json().get('message')['menu_report_type_id']

        assert post_type.status_code == 422
        assert validate_status == bool(False)
        assert "menu report type id yang dipilih tidak tersedia." in validate_message

    def test_post_report_menu_type_id_string(self):
        data = {
            "menu_stock_id": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0]['stock_id'],
            "menu_report_type_id": "aaa",
            "reason": "Pokoknya pingin report aja dah."
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
        }
        post_type = requests.post(settings.url_create_report_menu, data=data, files=file,
                                  headers=settings.header_with_token_customer)

        validate_status = post_type.json().get('success')
        validate_message = post_type.json().get('message')['menu_report_type_id']

        assert post_type.status_code == 422
        assert validate_status == bool(False)
        assert "menu report type id harus berupa angka." in validate_message

    def test_post_report_menu_without_reason(self):
        data = {
            "menu_stock_id": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0]['stock_id'],
            "menu_report_type_id": "2",
            # "reason": "Pokoknya pingin report aja dah."
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
        }
        post_type = requests.post(settings.url_create_report_menu, data=data, files=file,
                                  headers=settings.header_with_token_customer)

        validate_status = post_type.json().get('success')
        validate_message = post_type.json().get('message')['reason']

        assert post_type.status_code == 422
        assert validate_status == bool(False)
        assert "reason tidak boleh kosong." in validate_message

    def test_post_report_menu_reason_empty(self):
        data = {
            "menu_stock_id": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0]['stock_id'],
            "menu_report_type_id": "2",
            "reason": ""
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
        }
        post_type = requests.post(settings.url_create_report_menu, data=data, files=file,
                                  headers=settings.header_with_token_customer)

        validate_status = post_type.json().get('success')
        validate_message = post_type.json().get('message')['reason']

        assert post_type.status_code == 422
        assert validate_status == bool(False)
        assert "reason tidak boleh kosong." in validate_message

    def test_post_report_menu_reason_integer(self):
        data = {
            "menu_stock_id": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0]['stock_id'],
            "menu_report_type_id": "2",
            "reason": 123321
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
        }
        post_type = requests.post(settings.url_create_report_menu, data=data, files=file,
                                  headers=settings.header_with_token_customer)

        validate_status = post_type.json().get('success')
        validate_message = post_type.json().get('message')['reason']

        assert post_type.status_code == 422
        assert validate_status == bool(False)
        assert  "reason setidaknya harus 25 karakter." in validate_message

    def test_post_report_menu_without_image(self):
        data = {
            "menu_stock_id": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0]['stock_id'],
            "menu_report_type_id": "2",
            "reason": "Pokoknya pingin report aja dah."
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
        }
        post_type = requests.post(settings.url_create_report_menu, data=data,
                                  headers=settings.header_with_token_customer)

        validate_status = post_type.json().get('success')
        validate_message = post_type.json().get('message')

        assert post_type.status_code == 201
        assert validate_status == bool(True)
        assert "Data laporan berhasil ditambahkan." in validate_message

    def test_post_report_menu_image_empty(self):
        data = {
            "menu_stock_id": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0]['stock_id'],
            "menu_report_type_id": "2",
            "reason": "Pokoknya pingin report aja dah."
        }
        file = {
            'images[0]': ""
        }
        post_type = requests.post(settings.url_create_report_menu, data=data, files=file,
                                  headers=settings.header_with_token_customer)
        validate_status = post_type.json().get('success')
        validate_message = post_type.json().get('message')['images.0']

        assert post_type.status_code == 422
        assert validate_status == bool(False)
        assert "The images.0 must be a file of type: jpeg, jpg, png." in validate_message
