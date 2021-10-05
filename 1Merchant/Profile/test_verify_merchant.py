import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestVerifyMerchant:

    def test_verify_certification_normal(self):
        param = {
            "certifications[certifications][0][certification_id]": 1,
            "certifications[certifications][0][name]": 'null',
            "certifications[certifications][1][certification_id]": 2,
            "certifications[certifications][1][name]": 'null',
            "certifications[certifications][2][certification_id]": 3,
            "certifications[certifications][2][name]": 'null',
        }
        file = {
            'certifications[images][0]': open("img/telkomsel.png", 'rb'),
            'certifications[images][1]': open("img/telkomsel.png", 'rb'),
            'certifications[images][2]': open("img/telkomsel.png", 'rb'),
        }
        response = requests.post(settings.url_verify_merchant, data=param, headers=settings.header_with_token_merchant,
                                 files=file)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')
        validate_merchant_id = data.get('data')['merchant_id']
        validate_status_verify_request_id = data.get('data')['status_verify_request_id']

        assert validate_status == bool(True)
        assert response.status_code == 200
        assert validate_message == "Pengajuan verifikasi toko berhasil."
        assert validate_merchant_id == 10269
        assert validate_status_verify_request_id == 3

        settings.var_reject_verify_merchant()

    # def test_verify_information_normal(self):
    #     param = {
    #         "informations[questions][0][information_id]": 1,
    #         "informations[questions][0][answer]": 'mantap 1',
    #         "informations[questions][1][information_id]": 2,
    #         "informations[questions][1][answer]": 'mantap 2',
    #     }
    #     file = {
    #         'informations[images][0][images][0]': open("img/telkomsel.png", 'rb'),
    #         'informations[images][1][images][0]': open("img/telkomsel.png", 'rb'),
    #     }
    #     response = requests.post(settings.url_verify_merchant, data=param, headers=settings.header_with_token_merchant,
    #                              files=file)
    #     data = response.json()
    #     validate_status = data.get('success')
    #     validate_message = data.get('message')
    #     validate_merchant_id = data.get('data')['merchant_id']
    #     validate_status_verify_request_id = data.get('data')['status_verify_request_id']
    #
    #     assert validate_status == bool(True)
    #     assert response.status_code == 200
    #     assert validate_message == "Pengajuan verifikasi toko berhasil."
    #     assert validate_merchant_id == 10269
    #     assert validate_status_verify_request_id == 3
    #
    #     settings.var_reject_verify_merchant()

    def test_insert_verify_certification_doest_match_image_and_data(self):
        param = {
            "certifications[certifications][0][certification_id]": 1,
            "certifications[certifications][0][name]": 'null',
            "certifications[certifications][1][certification_id]": 2,
            "certifications[certifications][1][name]": 'null',
            "certifications[certifications][2][certification_id]": 3,
            "certifications[certifications][2][name]": 'null',
        }
        file = {
            'certifications[images][0]': open("img/telkomsel.png", 'rb'),
            'certifications[images][1]': open("img/telkomsel.png", 'rb'),
        }
        response = requests.post(settings.url_verify_merchant, data=param, headers=settings.header_with_token_merchant,
                                 files=file)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert validate_status == bool(False)
        assert response.status_code == 404
        assert "Jumlah gambar harus sesuai jumlah sertifikat yaitu " in validate_message

    def test_insert_verify_without_token(self):
        param = {
            "certifications[certifications][0][certification_id]": 1,
            "certifications[certifications][0][name]": 'null',
            "certifications[certifications][1][certification_id]": 2,
            "certifications[certifications][1][name]": 'null',
        }
        file = {
            'certifications[images][0]': open("img/telkomsel.png", 'rb'),
            'certifications[images][1]': open("img/telkomsel.png", 'rb'),
        }
        response = requests.post(settings.url_verify_merchant, data=param, headers=settings.header_without_token_merchant,
                                 files=file)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert validate_status == bool(False)
        assert response.status_code == 401
        assert "Unauthorized" == validate_message

    def test_insert_verify_wrong_token(self):
        param = {
            "certifications[certifications][0][certification_id]": 1,
            "certifications[certifications][0][name]": 'null',
            "certifications[certifications][1][certification_id]": 2,
            "certifications[certifications][1][name]": 'null',
        }
        file = {
            'certifications[images][0]': open("img/telkomsel.png", 'rb'),
            'certifications[images][1]': open("img/telkomsel.png", 'rb'),
        }
        response = requests.post(settings.url_verify_merchant, data=param, headers=settings.header_wrong_token_merchant,
                                 files=file)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert validate_status == bool(False)
        assert response.status_code == 401
        assert "Unauthorized" == validate_message

    def test_insert_verify_without_param_certification_id(self):
        param = {
            # "certifications[certifications][0][certification_id]": 1,
            "certifications[certifications][0][name]": 'null',
        }
        file = {
            'certifications[images][0]': open("img/telkomsel.png", 'rb'),
        }
        response = requests.post(settings.url_verify_merchant, data=param, headers=settings.header_with_token_merchant,
                                 files=file)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert validate_status == bool(False)
        assert response.status_code == 500
        assert "Aduh!" in validate_message

    def test_insert_verify_without_param_certificate_name(self):
        param = {
            "certifications[certifications][0][certification_id]": 1,
            # "certifications[certifications][0][name]": 'null',
        }
        file = {
            'certifications[images][0]': open("img/telkomsel.png", 'rb'),
        }
        response = requests.post(settings.url_verify_merchant, data=param, headers=settings.header_with_token_merchant,
                                 files=file)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert validate_status == bool(False)
        assert response.status_code == 500
        assert "Aduh!" in validate_message

    def test_insert_verify_without_param_certificate_image(self):
        param = {
            "certifications[certifications][0][certification_id]": 1,
            "certifications[certifications][0][name]": 'null',
        }
        file = {
            # 'certifications[images][0]': open("img/telkomsel.png", 'rb'),
        }
        response = requests.post(settings.url_verify_merchant, data=param, headers=settings.header_with_token_merchant,
                                 files=file)
        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert validate_status == bool(False)
        assert response.status_code == 404
        assert "Jumlah gambar harus sesuai" in validate_message
