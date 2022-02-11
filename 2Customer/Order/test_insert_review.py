import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerInsertReviewOrder:

    def test_insert_review_normal(self):
        param = {
            'order_number': settings.var_insert_review().json().get('data')['registrasi_order_number'],
            'rating': '5',
            'review': 'oke',
            'is_hide_name': '0'
        }
        insert_review = requests.post(settings.url_insert_review_customer,params=param, headers=settings.header_with_token_customer)
        assert insert_review.status_code == 200
        assert insert_review.json().get('success') == True
        assert 'Berhasil' in insert_review.json().get('message')

    def test_insert_review_wrong_token(self):
        param = {
            'order_number': settings.var_insert_review().json().get('data')['registrasi_order_number'],
            'rating': '5',
            'review': 'oke',
            'is_hide_name': '0'
        }
        insert_review = requests.post(settings.url_insert_review_customer,params=param, headers=settings.header_wrong_token_customer)

        assert insert_review.status_code == 401
        assert insert_review.json().get('success') == False
        assert 'Unauthorized' in insert_review.json().get('message')

    def test_insert_review_without_token(self):
        param = {
            'order_number': settings.var_insert_review().json().get('data')['registrasi_order_number'],
            'rating': '5',
            'review': 'oke',
            'is_hide_name': '0'
        }
        insert_review = requests.post(settings.url_insert_review_customer,params=param, headers=settings.header_without_token_customer)

        assert insert_review.status_code == 401
        assert insert_review.json().get('success') == False
        assert 'Unauthorized' in insert_review.json().get('message')

    def test_insert_review_without_ordernumber(self):
        param = {
            # 'order_number': '',
            'rating': '5',
            'review': 'oke',
            'is_hide_name': '0'
        }
        insert_review = requests.post(settings.url_insert_review_customer,params=param, headers=settings.header_with_token_customer)

        assert insert_review.status_code == 422
        assert insert_review.json().get('success') == False
        assert 'order number tidak boleh kosong.' in insert_review.json().get('message')['order_number']

    def test_insert_review_empty_ordernumber(self):
        param = {
            'order_number': '',
            'rating': '5',
            'review': 'oke',
            'is_hide_name': '0'
        }
        insert_review = requests.post(settings.url_insert_review_customer,params=param, headers=settings.header_with_token_customer)

        assert insert_review.status_code == 422
        assert insert_review.json().get('success') == False
        assert 'order number tidak boleh kosong.' in insert_review.json().get('message')['order_number']

    def test_insert_review_wrong_ordernumber(self):
        param = {
            'order_number': 'S112233445566',
            'rating': '5',
            'review': 'oke',
            'is_hide_name': '0'
        }
        insert_review = requests.post(settings.url_insert_review_customer,params=param, headers=settings.header_with_token_customer)

        assert insert_review.status_code == 404
        assert insert_review.json().get('success') == False
        assert 'tidak ditemukan' in insert_review.json().get('message')

    def test_insert_review_without_rating(self):
        param = {
            'order_number': settings.var_insert_review().json().get('data')['registrasi_order_number'],
            # 'rating': '5',
            'review': 'oke',
            'is_hide_name': '0'
        }
        insert_review = requests.post(settings.url_insert_review_customer,params=param, headers=settings.header_with_token_customer)

        assert insert_review.status_code == 422
        assert insert_review.json().get('success') == False
        assert 'rating tidak boleh kosong.' in insert_review.json().get('message')['rating']

    def test_insert_review_empty_rating(self):
        param = {
            'order_number': settings.var_insert_review().json().get('data')['registrasi_order_number'],
            'rating': '',
            'review': 'oke',
            'is_hide_name': '0'
        }
        insert_review = requests.post(settings.url_insert_review_customer,params=param, headers=settings.header_with_token_customer)

        assert insert_review.status_code == 422
        assert insert_review.json().get('success') == False
        assert 'rating tidak boleh kosong.' in insert_review.json().get('message')['rating']

    def test_insert_review_more5_rating(self):
        param = {
            'order_number': settings.var_insert_review().json().get('data')['registrasi_order_number'],
            'rating': '10',
            'review': 'oke',
            'is_hide_name': '0'
        }
        insert_review = requests.post(settings.url_insert_review_customer,params=param, headers=settings.header_with_token_customer)

        assert insert_review.status_code == 200
        assert insert_review.json().get('success') == True

    def test_insert_review_less0_rating(self):
        param = {
            'order_number': settings.var_insert_review().json().get('data')['registrasi_order_number'],
            'rating': '-1',
            'review': 'oke',
            'is_hide_name': '0'
        }
        insert_review = requests.post(settings.url_insert_review_customer,params=param, headers=settings.header_with_token_customer)

        assert insert_review.status_code == 200
        assert insert_review.json().get('success') == True

    def test_insert_review_0_rating(self):
        param = {
            'order_number': 'S2202090934723',
            'rating': '5',
            'review': 'oke',
            'is_hide_name': '0'
        }
        insert_review = requests.post(settings.url_insert_review_customer,params=param, headers=settings.header_with_token_customer)

        assert insert_review.status_code == 404
        assert insert_review.json().get('success') == False
        assert 'Anda sudah memberikan rating pada order dengan nomor S2202090934723' in insert_review.json().get('message')

    def test_insert_review_empty_review(self):
        param = {
            'order_number': settings.var_insert_review().json().get('data')['registrasi_order_number'],
            'rating': '5',
            'review': '',
            'is_hide_name': '0'
        }
        insert_review = requests.post(settings.url_insert_review_customer,params=param, headers=settings.header_with_token_customer)

        assert insert_review.status_code == 200
        assert insert_review.json().get('success') == True
        assert 'Berhasil' in insert_review.json().get('message')

    def test_insert_review_without_review(self):
        param = {
            'order_number': settings.var_insert_review().json().get('data')['registrasi_order_number'],
            'rating': '5',
            # 'review': '',
            'is_hide_name': '0'
        }
        insert_review = requests.post(settings.url_insert_review_customer,params=param, headers=settings.header_with_token_customer)

        assert insert_review.status_code == 500
        assert insert_review.json().get('success') == False

    def test_insert_review_without_hide(self):
        param = {
            'order_number': settings.var_insert_review().json().get('data')['registrasi_order_number'],
            'rating': '5',
            'review': 'ok',
            # 'is_hide_name': '0'
        }
        insert_review = requests.post(settings.url_insert_review_customer,params=param, headers=settings.header_with_token_customer)

        assert insert_review.status_code == 422
        assert insert_review.json().get('success') == False

    def test_insert_review_empty_hide(self):
        param = {
            'order_number': settings.var_insert_review().json().get('data')['registrasi_order_number'],
            'rating': '5',
            'review': 'ok',
            # 'is_hide_name': '0'
        }
        insert_review = requests.post(settings.url_insert_review_customer,params=param, headers=settings.header_with_token_customer)

        assert insert_review.status_code == 422
        assert insert_review.json().get('success') == False

    def test_insert_review_not_boolean_hide(self):
        param = {
            'order_number': settings.var_insert_review().json().get('data')['registrasi_order_number'],
            'rating': '5',
            'review': 'ok',
            'is_hide_name': '3'
        }
        insert_review = requests.post(settings.url_insert_review_customer,params=param, headers=settings.header_with_token_customer)

        assert insert_review.status_code == 422
        assert insert_review.json().get('success') == False


