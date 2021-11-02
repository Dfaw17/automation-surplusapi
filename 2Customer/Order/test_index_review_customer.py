import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerIndexReview:

    def test_index_review_normal(self):
        param = {
            'filter_by': 'all',
            'merchant_id': settings.id_merchant_pusat
        }

        review = requests.get(settings.url_index_review_customer, params=param,
                              headers=settings.header_with_token_customer)

        assert review.status_code == 200
        assert_that(review.json().get('data')).contains('filter_by', 'merchant_id', 'rating', 'total_review',
                                                        'merchant_name', 'reviews')
        assert_that(review.json().get('data')['merchant_id']).is_equal_to(settings.id_merchant_pusat)
        assert_that(review.json().get('data')['reviews'][0]).contains('id', 'order_id', 'merchant_id', 'user_id',
                                                                      'is_hide_name', 'rating', 'review', 'created_at',
                                                                      'updated_at', 'merchant_name',
                                                                      'merchant_category', 'badge', 'badge_id', 'time',
                                                                      'name', 'is_like', 'is_report', 'images')

    def test_index_wrong_token(self):
        param = {
            'filter_by': 'all',
            'merchant_id': settings.id_merchant_pusat
        }

        review = requests.get(settings.url_index_review_customer, params=param,
                              headers=settings.header_wrong_token_customer)

        assert review.status_code == 200

    def test_index_empty_token(self):
        param = {
            'filter_by': 'all',
            'merchant_id': settings.id_merchant_pusat
        }

        review = requests.get(settings.url_index_review_customer, params=param,
                              headers=settings.header_without_token_customer)

        assert review.status_code == 200

    def test_without_filter_index_review(self):
        param = {
            # 'filter_by': 'all',
            'merchant_id': settings.id_merchant_pusat
        }

        review = requests.get(settings.url_index_review_customer, params=param,
                              headers=settings.header_with_token_customer)

        assert review.status_code == 422
        assert 'filter by tidak boleh kosong.' in review.json().get('message')['filter_by']

    def test_empty_filter_index_review(self):
        param = {
            'filter_by': '',
            'merchant_id': settings.id_merchant_pusat
        }

        review = requests.get(settings.url_index_review_customer, params=param,
                              headers=settings.header_with_token_customer)

        assert review.status_code == 422
        assert 'filter by tidak boleh kosong.' in review.json().get('message')['filter_by']

    def test_wrong_filter_index_review(self):
        param = {
            'filter_by': 'alls',
            'merchant_id': settings.id_merchant_pusat
        }

        review = requests.get(settings.url_index_review_customer, params=param,
                              headers=settings.header_with_token_customer)

        assert review.status_code == 422
        assert 'filter by yang dipilih tidak tersedia.' in review.json().get('message')['filter_by']

    def test_without_merchant_id_index_review(self):
        param = {
            'filter_by': 'all',
            # 'merchant_id': settings.id_merchant_pusat
        }

        review = requests.get(settings.url_index_review_customer, params=param,
                              headers=settings.header_with_token_customer)

        assert review.status_code == 422
        assert 'merchant id tidak boleh kosong.' in review.json().get('message')['merchant_id']

    def test_empty_index_review(self):
        param = {
            'filter_by': 'all',
            'merchant_id': ''
        }

        review = requests.get(settings.url_index_review_customer, params=param,
                              headers=settings.header_with_token_customer)

        assert review.status_code == 422
        assert 'merchant id tidak boleh kosong.' in review.json().get('message')['merchant_id']
