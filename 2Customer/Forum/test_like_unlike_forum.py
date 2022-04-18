import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerLikeUnlikeForum:

    def test_like_unlike_forum_normal(self):
        param = {
            'id': settings.forum_id,
            'event': 'forum'
        }
        like_unlike = requests.post(settings.url_like_unlike_forum_customer,
                                    headers=settings.header_with_token_customer, data=param)

        assert like_unlike.status_code == 200
        assert_that(like_unlike.json().get('success')).is_equal_to(True)

    def test_like_unlike_forum_wrong_token(self):
        param = {
            'id': '10',
            'event': 'forum'
        }
        like_unlike = requests.post(settings.url_like_unlike_forum_customer,
                                    headers=settings.header_wrong_token_customer, data=param)

        assert like_unlike.status_code == 401
        assert_that(like_unlike.json().get('success')).is_equal_to(False)

    def test_like_unlike_forum_empty_token(self):
        param = {
            'id': '10',
            'event': 'forum'
        }
        like_unlike = requests.post(settings.url_like_unlike_forum_customer,
                                    headers=settings.header_without_token_customer, data=param)

        assert like_unlike.status_code == 401
        assert_that(like_unlike.json().get('success')).is_equal_to(False)

    def test_like_unlike_forum_id_string(self):
        param = {
            'id': 'aa',
            'event': 'forum'
        }
        like_unlike = requests.post(settings.url_like_unlike_forum_customer,
                                    headers=settings.header_with_token_customer, data=param)

        assert like_unlike.status_code == 422
        assert_that(like_unlike.json().get('success')).is_equal_to(False)
        assert 'id harus berupa angka.' in like_unlike.json().get('message')['id']

    def test_like_unlike_forum_id_empty(self):
        param = {
            # 'id': 'aa',
            'event': 'forum'
        }
        like_unlike = requests.post(settings.url_like_unlike_forum_customer,
                                    headers=settings.header_with_token_customer, data=param)

        assert like_unlike.status_code == 422
        assert_that(like_unlike.json().get('success')).is_equal_to(False)
        assert 'id tidak boleh kosong.' in like_unlike.json().get('message')['id']

    def test_like_unlike_forum_id_not_found(self):
        param = {
            'id': '99999999',
            'event': 'forum'
        }
        like_unlike = requests.post(settings.url_like_unlike_forum_customer,
                                    headers=settings.header_with_token_customer, data=param)

        assert like_unlike.status_code == 404
        assert_that(like_unlike.json().get('success')).is_equal_to(False)
        assert 'Forum tidak ditemukan' in like_unlike.json().get('message')
