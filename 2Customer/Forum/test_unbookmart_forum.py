import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerUnBookmartPostForum:

    def test_unbookmart_post_normal(self):
        unbookmart_comment = requests.delete(settings.url_bookmart_forum_customer + '/10',
                                             headers=settings.header_with_token_customer)

        assert unbookmart_comment.status_code == 200
        assert_that(unbookmart_comment.json().get('success')).is_equal_to(True)
        assert_that(unbookmart_comment.json().get('message')).is_equal_to("Simpan forum berhasil dibatalkan")

    def test_unbookmart_post_wrong_token(self):
        unbookmart_comment = requests.delete(settings.url_bookmart_forum_customer + '/10',
                                             headers=settings.header_wrong_token_customer)

        assert unbookmart_comment.status_code == 401
        assert_that(unbookmart_comment.json().get('success')).is_equal_to(False)
        assert_that(unbookmart_comment.json().get('message')).is_equal_to("Unauthorized")

    def test_unbookmart_post_empty_token(self):
        unbookmart_comment = requests.delete(settings.url_bookmart_forum_customer + '/10',
                                             headers=settings.header_without_token_customer)

        assert unbookmart_comment.status_code == 401
        assert_that(unbookmart_comment.json().get('success')).is_equal_to(False)
        assert_that(unbookmart_comment.json().get('message')).is_equal_to("Unauthorized")

    def test_unbookmart_post_wrong_id(self):
        unbookmart_comment = requests.delete(settings.url_bookmart_forum_customer + '/9999999',
                                             headers=settings.header_with_token_customer)

        assert unbookmart_comment.status_code == 500
        assert_that(unbookmart_comment.json().get('success')).is_equal_to(False)

    def test_unbookmart_post_empty_id(self):
        unbookmart_comment = requests.delete(settings.url_bookmart_forum_customer + '',
                                             headers=settings.header_with_token_customer)

        assert unbookmart_comment.status_code == 405
        assert_that(unbookmart_comment.json().get('success')).is_equal_to(False)
