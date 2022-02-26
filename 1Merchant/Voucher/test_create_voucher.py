import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCreateVoucher:

    def test_craete_vocher_ongkir(self):
        param = {
            'title': f'Test Voucher Automation Danger 1 ongkir {settings.now}',
            'fixed_discount': '3000',
            'min_purchase': '1000',
            'max_usage': '3',
            'start_at': settings.today,
            'end_at': settings.seven_days,
            'target_id': '2',
            'is_branch_joinable': '1',
        }
        response = requests.post(settings.url_voucher_merchant, data=param, headers=settings.header_with_token_merchant)

        data = response.json()
        print(data)
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 201
        assert 'berhasil ditambahkan.' in validate_message
        assert validate_status == bool(True)

    def test_craete_vocher_subsidi(self):
        param = {
            'title': f'Test Voucher Automation Danger 1 subsidi {settings.now}',
            'fixed_discount': '3000',
            'min_purchase': '1000',
            'max_usage': '3',
            'start_at': settings.today,
            'end_at': settings.seven_days,
            'target_id': '1',
            'is_branch_joinable': '0',
        }
        response = requests.post(settings.url_voucher_merchant, data=param, headers=settings.header_with_token_merchant)

        data = response.json()
        print(data)
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 201
        assert 'berhasil ditambahkan.' in validate_message
        assert validate_status == bool(True)

    def test_craete_vocher_without_name(self):
        param = {
            # 'title': f'Test Voucher Automation Danger 1 subsidi {settings.now}',
            'fixed_discount': '3000',
            'min_purchase': '1000',
            'max_usage': '3',
            'start_at': settings.today,
            'end_at': settings.seven_days,
            'target_id': '1',
            'is_branch_joinable': '0',
        }
        response = requests.post(settings.url_voucher_merchant, data=param, headers=settings.header_with_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 201
        assert 'berhasil ditambahkan.' in validate_message
        assert validate_status == bool(True)

    def test_craete_vocher_without_branch(self):
        param = {
            # 'title': f'Test Voucher Automation Danger 1 subsidi {settings.now}',
            'fixed_discount': '3000',
            'min_purchase': '1000',
            'max_usage': '3',
            'start_at': settings.today,
            'end_at': settings.seven_days,
            'target_id': '1',
            # 'is_branch_joinable': '0',
        }
        response = requests.post(settings.url_voucher_merchant, data=param, headers=settings.header_with_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 201
        assert 'berhasil ditambahkan.' in validate_message
        assert validate_status == bool(True)

    def test_craete_vocher_without_token(self):
        param = {
            # 'title': f'Test Voucher Automation Danger 1 subsidi {settings.now}',
            'fixed_discount': '3000',
            'min_purchase': '1000',
            'max_usage': '3',
            'start_at': settings.today,
            'end_at': settings.seven_days,
            'target_id': '1',
            # 'is_branch_joinable': '0',
        }
        response = requests.post(settings.url_voucher_merchant, data=param,
                                 headers=settings.header_without_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 401
        assert 'Unauthorized' in validate_message
        assert validate_status == bool(False)

    def test_craete_vocher_token_empty(self):
        param = {
            # 'title': f'Test Voucher Automation Danger 1 subsidi {settings.now}',
            'fixed_discount': '3000',
            'min_purchase': '1000',
            'max_usage': '3',
            'start_at': settings.today,
            'end_at': settings.seven_days,
            'target_id': '1',
            # 'is_branch_joinable': '0',
        }
        response = requests.post(settings.url_voucher_merchant, data=param,
                                 headers=settings.header_without_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 401
        assert 'Unauthorized' in validate_message
        assert validate_status == bool(False)

    def test_craete_vocher_fix_discount_empty(self):
        param = {
            # 'title': f'Test Voucher Automation Danger 1 subsidi {settings.now}',
            'fixed_discount': '',
            'min_purchase': '1000',
            'max_usage': '3',
            'start_at': settings.today,
            'end_at': settings.seven_days,
            'target_id': '1',
            # 'is_branch_joinable': '0',
        }
        response = requests.post(settings.url_voucher_merchant, data=param, headers=settings.header_with_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['fixed_discount']

        assert response.status_code == 422
        assert 'fixed discount tidak boleh kosong.' in validate_message
        assert validate_status == bool(False)

    def test_craete_vocher_fix_discount_string(self):
        param = {
            # 'title': f'Test Voucher Automation Danger 1 subsidi {settings.now}',
            'fixed_discount': 'aaa',
            'min_purchase': '1000',
            'max_usage': '3',
            'start_at': settings.today,
            'end_at': settings.seven_days,
            'target_id': '1',
            # 'is_branch_joinable': '0',
        }
        response = requests.post(settings.url_voucher_merchant, data=param, headers=settings.header_with_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['fixed_discount']

        assert response.status_code == 422
        assert 'fixed discount harus berupa angka.' in validate_message
        assert validate_status == bool(False)

    def test_craete_vocher_without_fix_discount(self):
        param = {
            # 'title': f'Test Voucher Automation Danger 1 subsidi {settings.now}',
            'fixed_discount': '',
            'min_purchase': '1000',
            'max_usage': '3',
            'start_at': settings.today,
            'end_at': settings.seven_days,
            'target_id': '1',
            # 'is_branch_joinable': '0',
        }
        response = requests.post(settings.url_voucher_merchant, data=param, headers=settings.header_with_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['fixed_discount']

        assert response.status_code == 422
        assert 'fixed discount tidak boleh kosong.' in validate_message
        assert validate_status == bool(False)

    def test_craete_vocher_min_purchase_empty(self):
        param = {
            'title': f'Test Voucher Automation Danger 1 ongkir {settings.now}',
            'fixed_discount': '3000',
            'min_purchase': '',
            'max_usage': '3',
            'start_at': settings.today,
            'end_at': settings.seven_days,
            'target_id': '2',
            'is_branch_joinable': '0',
        }
        response = requests.post(settings.url_voucher_merchant, data=param, headers=settings.header_with_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['min_purchase']

        assert response.status_code == 422
        assert 'min purchase tidak boleh kosong.' in validate_message
        assert validate_status == bool(False)

    def test_craete_vocher_without_min_purchase(self):
        param = {
            'title': f'Test Voucher Automation Danger 1 ongkir {settings.now}',
            'fixed_discount': '3000',
            # 'min_purchase': '',
            'max_usage': '3',
            'start_at': settings.today,
            'end_at': settings.seven_days,
            'target_id': '2',
            'is_branch_joinable': '0',
        }
        response = requests.post(settings.url_voucher_merchant, data=param, headers=settings.header_with_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['min_purchase']

        assert response.status_code == 422
        assert 'min purchase tidak boleh kosong.' in validate_message
        assert validate_status == bool(False)

    def test_craete_vocher_min_purchase_string(self):
        param = {
            'title': f'Test Voucher Automation Danger 1 ongkir {settings.now}',
            'fixed_discount': '3000',
            'min_purchase': 'aaa',
            'max_usage': '3',
            'start_at': settings.today,
            'end_at': settings.seven_days,
            'target_id': '2',
            'is_branch_joinable': '0',
        }
        response = requests.post(settings.url_voucher_merchant, data=param, headers=settings.header_with_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['min_purchase']

        assert response.status_code == 422
        assert 'min purchase harus berupa angka.' in validate_message
        assert validate_status == bool(False)

    def test_craete_vocher_max_usage_empty(self):
        param = {
            'title': f'Test Voucher Automation Danger 1 ongkir {settings.now}',
            'fixed_discount': '3000',
            'min_purchase': '1000',
            'max_usage': '',
            'start_at': settings.today,
            'end_at': settings.seven_days,
            'target_id': '2',
            'is_branch_joinable': '0',
        }
        response = requests.post(settings.url_voucher_merchant, data=param, headers=settings.header_with_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['max_usage']

        assert response.status_code == 422
        assert 'max usage tidak boleh kosong.' in validate_message
        assert validate_status == bool(False)

    def test_craete_vocher_without_max_usage(self):
        param = {
            'title': f'Test Voucher Automation Danger 1 ongkir {settings.now}',
            'fixed_discount': '3000',
            'min_purchase': '1000',
            # 'max_usage': '',
            'start_at': settings.today,
            'end_at': settings.seven_days,
            'target_id': '2',
            'is_branch_joinable': '0',
        }
        response = requests.post(settings.url_voucher_merchant, data=param, headers=settings.header_with_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['max_usage']

        assert response.status_code == 422
        assert 'max usage tidak boleh kosong.' in validate_message
        assert validate_status == bool(False)

    def test_craete_vocher_max_usage_string(self):
        param = {
            'title': f'Test Voucher Automation Danger 1 ongkir {settings.now}',
            'fixed_discount': '3000',
            'min_purchase': '1000',
            'max_usage': 'aaa',
            'start_at': settings.today,
            'end_at': settings.seven_days,
            'target_id': '2',
            'is_branch_joinable': '0',
        }
        response = requests.post(settings.url_voucher_merchant, data=param, headers=settings.header_with_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['max_usage']

        assert response.status_code == 422
        assert 'max usage harus berupa angka.' in validate_message
        assert validate_status == bool(False)

    def test_craete_vocher_start_at_empty(self):
        param = {
            'title': f'Test Voucher Automation Danger 1 ongkir {settings.now}',
            'fixed_discount': '3000',
            'min_purchase': '1000',
            'max_usage': '3',
            'start_at': '',
            'end_at': settings.seven_days,
            'target_id': '2',
            'is_branch_joinable': '0',
        }
        response = requests.post(settings.url_voucher_merchant, data=param, headers=settings.header_with_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['start_at']

        assert response.status_code == 422
        assert 'start at bukan format tanggal yang valid.' in validate_message
        assert validate_status == bool(False)

    def test_craete_vocher_start_at_non_date(self):
        param = {
            'title': f'Test Voucher Automation Danger 1 ongkir {settings.now}',
            'fixed_discount': '3000',
            'min_purchase': '1000',
            'max_usage': '3',
            'start_at': 'aaa',
            'end_at': settings.seven_days,
            'target_id': '2',
            'is_branch_joinable': '0',
        }
        response = requests.post(settings.url_voucher_merchant, data=param, headers=settings.header_with_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['start_at']

        assert response.status_code == 422
        assert 'start at bukan format tanggal yang valid.' in validate_message
        assert validate_status == bool(False)

    def test_craete_vocher_without_start_at(self):
        param = {
            'title': f'Test Voucher Automation Danger 1 ongkir {settings.now}',
            'fixed_discount': '3000',
            'min_purchase': '1000',
            'max_usage': '3',
            # 'start_at': '',
            'end_at': settings.seven_days,
            'target_id': '2',
            'is_branch_joinable': '0',
        }
        response = requests.post(settings.url_voucher_merchant, data=param, headers=settings.header_with_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 400
        assert 'Parameter start_at atau end_at tidak boleh kurang dari hari ini.' in validate_message
        assert validate_status == bool(False)

    def test_craete_vocher_end_at_empty(self):
        param = {
            'title': f'Test Voucher Automation Danger 1 ongkir {settings.now}',
            'fixed_discount': '3000',
            'min_purchase': '1000',
            'max_usage': '3',
            'start_at': settings.today,
            'end_at': '',
            'target_id': '2',
            'is_branch_joinable': '0',
        }
        response = requests.post(settings.url_voucher_merchant, data=param, headers=settings.header_with_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['end_at']

        assert response.status_code == 422
        assert 'end at bukan format tanggal yang valid.' in validate_message
        assert validate_status == bool(False)

    def test_craete_vocher_end_at_non_date(self):
        param = {
            'title': f'Test Voucher Automation Danger 1 ongkir {settings.now}',
            'fixed_discount': '3000',
            'min_purchase': '1000',
            'max_usage': '3',
            'start_at': settings.today,
            'end_at': 'aaa',
            'target_id': '2',
            'is_branch_joinable': '0',
        }
        response = requests.post(settings.url_voucher_merchant, data=param, headers=settings.header_with_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['end_at']

        assert response.status_code == 422
        assert 'end at bukan format tanggal yang valid.' in validate_message
        assert validate_status == bool(False)

    def test_craete_vocher_without_end_at(self):
        param = {
            'title': f'Test Voucher Automation Danger 1 ongkir {settings.now}',
            'fixed_discount': '3000',
            'min_purchase': '1000',
            'max_usage': '3',
            'start_at': settings.today,
            # 'end_at': settings.seven_days,
            'target_id': '2',
            'is_branch_joinable': '0',
        }
        response = requests.post(settings.url_voucher_merchant, data=param, headers=settings.header_with_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')

        assert response.status_code == 400
        assert 'Data tanggal tidak valid. end_at kurang dari start_at.' in validate_message
        assert validate_status == bool(False)

    def test_craete_vocher_target_id_empty(self):
        param = {
            'title': f'Test Voucher Automation Danger 1 ongkir {settings.now}',
            'fixed_discount': '3000',
            'min_purchase': '1000',
            'max_usage': '3',
            'start_at': settings.today,
            'end_at': settings.seven_days,
            'target_id': '',
            'is_branch_joinable': '0',
        }
        response = requests.post(settings.url_voucher_merchant, data=param, headers=settings.header_with_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['target_id']

        assert response.status_code == 422
        assert 'target id tidak boleh kosong.' in validate_message
        assert validate_status == bool(False)

    def test_craete_vocher_without_target_id(self):
        param = {
            'title': f'Test Voucher Automation Danger 1 ongkir {settings.now}',
            'fixed_discount': '3000',
            'min_purchase': '1000',
            'max_usage': '3',
            'start_at': settings.today,
            'end_at': settings.seven_days,
            # 'target_id': '',
            'is_branch_joinable': '0',
        }
        response = requests.post(settings.url_voucher_merchant, data=param, headers=settings.header_with_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['target_id']

        assert response.status_code == 422
        assert 'target id tidak boleh kosong.' in validate_message
        assert validate_status == bool(False)

    def test_craete_vocher_target_id_string(self):
        param = {
            'title': f'Test Voucher Automation Danger 1 ongkir {settings.now}',
            'fixed_discount': '3000',
            'min_purchase': '1000',
            'max_usage': '3',
            'start_at': settings.today,
            'end_at': settings.seven_days,
            'target_id': 'aaa',
            'is_branch_joinable': '0',
        }
        response = requests.post(settings.url_voucher_merchant, data=param, headers=settings.header_with_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['target_id']

        assert response.status_code == 422
        assert 'target id harus merupakan sebuah nomor.' in validate_message
        assert validate_status == bool(False)

    def test_craete_vocher_target_id_wrong(self):
        param = {
            'title': f'Test Voucher Automation Danger 1 ongkir {settings.now}',
            'fixed_discount': '3000',
            'min_purchase': '1000',
            'max_usage': '3',
            'start_at': settings.today,
            'end_at': settings.seven_days,
            'target_id': '99',
            'is_branch_joinable': '0',
        }
        response = requests.post(settings.url_voucher_merchant, data=param, headers=settings.header_with_token_merchant)

        data = response.json()
        validate_status = data.get('success')
        validate_message = data.get('message')['target_id']

        assert response.status_code == 422
        assert "target id tidak boleh lebih dari 2." in validate_message
        assert validate_status == bool(False)
