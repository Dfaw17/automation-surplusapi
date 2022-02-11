import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerSettlementOrder:

    def test_order_settlement_normal(self):
        number = settings.var_order_settlement().json().get('data')['registrasi_order_number']
        time.sleep(5)
        settlement_order = requests.post(
            settings.url_settlement_order_customer + number + '/settlement?_method=PATCH', headers=settings.header_with_token_customer)

        assert settlement_order.status_code == 200

    def test_order_settlement_wrong_token(self):
        number = settings.var_order_settlement().json().get('data')['registrasi_order_number']
        time.sleep(3)
        settlement_order = requests.post(
            settings.url_settlement_order_customer + number + '/settlement?_method=PATCH', headers=settings.header_wrong_token_customer)

        assert settlement_order.status_code == 401
        assert settlement_order.json().get('success') == bool(False)
        assert 'Unauthorized' in settlement_order.json().get('message')

    def test_order_settlement_empty_token(self):
        number = settings.var_order_settlement().json().get('data')['registrasi_order_number']
        time.sleep(3)
        settlement_order = requests.post(
            settings.url_settlement_order_customer + number + '/settlement?_method=PATCH', headers=settings.header_without_token_customer)

        assert settlement_order.status_code == 401
        assert settlement_order.json().get('success') == bool(False)
        assert 'Unauthorized' in settlement_order.json().get('message')

    def test_order_settlement_trx_id_empty(self):
        number = settings.var_order_settlement().json().get('data')['registrasi_order_number']
        time.sleep(3)
        settlement_order = requests.post(
            settings.url_settlement_order_customer + '' + '/settlement?_method=PATCH', headers=settings.header_with_token_customer)

        assert settlement_order.status_code == 404
        assert settlement_order.json().get('success') == bool(False)

    def test_order_settlement_trx_id_wrong(self):
        number = settings.var_order_settlement().json().get('data')['registrasi_order_number']
        time.sleep(3)
        settlement_order = requests.post(
            settings.url_settlement_order_customer + 'S112233445566' + '/settlement?_method=PATCH', headers=settings.header_with_token_customer)

        assert settlement_order.status_code == 500
        assert settlement_order.json().get('success') == bool(False)

