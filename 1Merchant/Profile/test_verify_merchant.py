import sys
import requests
import settings
from assertpy import assert_that
import warnings

sys.path.append('.../IntegrationTest')


class TestVerifyMerchant:

    def test_verify_normal(self):
        param = {
            "certifications[certifications][0][certification_id]": 1,
            "certifications[certifications][0][name]": 'null',
        }
        response = requests.post(settings.url_verify_merchant, data=param, headers=settings.header_with_token_merchant,
                                 files={'certifications[images][0]': open("img/telkomsel.png", 'rb')})
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
        warnings.filterwarnings("ignore", category=DeprecationWarning)
