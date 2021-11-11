import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerBookmartPostForum:

    def test_bookmart_post_normal(self):
        param = {
            'forum_id': '10',
        }
        bookmart_comment = requests.post(settings.url_bookmart_forum_customer,
                                         headers=settings.header_with_token_customer, data=param)

        assert bookmart_comment.status_code == 201
        assert_that(bookmart_comment.json().get('success')).is_equal_to(True)
        assert_that(bookmart_comment.json().get('message')).is_equal_to("Forum berhasil disimpan")

    def test_bookmart_post_without_token(self):
        param = {
            'forum_id': '10',
        }
        bookmart_comment = requests.post(settings.url_bookmart_forum_customer,
                                         headers=settings.header_without_token_customer, data=param)

        assert bookmart_comment.status_code == 401
        assert_that(bookmart_comment.json().get('success')).is_equal_to(False)
        assert_that(bookmart_comment.json().get('message')).is_equal_to("Unauthorized")

    def test_bookmart_post_wrong_token(self):
        param = {
            'forum_id': '10',
        }
        bookmart_comment = requests.post(settings.url_bookmart_forum_customer,
                                         headers=settings.header_wrong_token_customer, data=param)

        assert bookmart_comment.status_code == 401
        assert_that(bookmart_comment.json().get('success')).is_equal_to(False)
        assert_that(bookmart_comment.json().get('message')).is_equal_to("Unauthorized")

    def test_bookmart_post_id_wrong(self):
        param = {
            'forum_id': '9999999',
        }
        bookmart_comment = requests.post(settings.url_bookmart_forum_customer,
                                         headers=settings.header_with_token_customer, data=param)

        assert bookmart_comment.status_code == 404
        assert_that(bookmart_comment.json().get('success')).is_equal_to(False)
        assert_that(bookmart_comment.json().get('message')).is_equal_to('Forum tidak ditemukan')

    def test_bookmart_post_id_empty(self):
        param = {
            'forum_id': '',
        }
        bookmart_comment = requests.post(settings.url_bookmart_forum_customer,
                                         headers=settings.header_with_token_customer, data=param)

        assert bookmart_comment.status_code == 422
        assert_that(bookmart_comment.json().get('success')).is_equal_to(False)

    def test_bookmart_without_post_id(self):
        param = {
            # 'forum_id': '',
        }
        bookmart_comment = requests.post(settings.url_bookmart_forum_customer,
                                         headers=settings.header_with_token_customer, data=param)

        assert bookmart_comment.status_code == 422
        assert_that(bookmart_comment.json().get('success')).is_equal_to(False)
