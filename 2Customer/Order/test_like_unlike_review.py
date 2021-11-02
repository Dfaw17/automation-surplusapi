import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerLikeUnlikeReview:

    def test_like_unlike_review_normal(self):
        review = requests.post(settings.url_like_unlike_review_customer + str(
            settings.var_index_review().json().get('data')['reviews'][0]['id']) + '/like-dislike',
                               headers=settings.header_with_token_customer)

        assert review.status_code == 200
        assert_that(review.json().get('success')).is_equal_to(True)
        assert_that(review.json().get('data')).contains('id', 'review_id', 'user_id', 'is_like', 'is_report',
                                                        'created_at', 'updated_at')

    def test_like_unlike_review_wrong_token(self):
        review = requests.post(settings.url_like_unlike_review_customer + str(
            settings.var_index_review().json().get('data')['reviews'][0]['id']) + '/like-dislike',
                               headers=settings.header_wrong_token_customer)

        assert review.status_code == 401
        assert_that(review.json().get('success')).is_equal_to(False)
        assert_that(review.json().get('message')).is_equal_to('Unauthorized')

    def test_like_unlike_review_without_token(self):
        review = requests.post(settings.url_like_unlike_review_customer + str(
            settings.var_index_review().json().get('data')['reviews'][0]['id']) + '/like-dislike',
                               headers=settings.header_without_token_customer)

        assert review.status_code == 401
        assert_that(review.json().get('success')).is_equal_to(False)
        assert_that(review.json().get('message')).is_equal_to('Unauthorized')

    def test_like_unlike_review_wrong_id(self):
        review = requests.post(settings.url_like_unlike_review_customer + '998877665544332211' + '/like-dislike',
                               headers=settings.header_with_token_customer)

        assert review.status_code == 500
        assert_that(review.json().get('success')).is_equal_to(False)
        assert 'Aduh' in review.json().get('message')