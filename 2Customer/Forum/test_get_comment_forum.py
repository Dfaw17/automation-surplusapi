import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerGetComment:

    def test_get_comment_forum_normal(self):
        param = {
            'post_id': settings.var_index_forum().json().get('data')['popular_posts'][0]['id']
        }
        comment = requests.get(settings.url_get_comment_forum_customer, params=param,
                               headers=settings.header_with_token_customer)

        assert comment.status_code == 200
        assert comment.json().get('message') == "Komentar ditemukan"
        assert comment.json().get('success') == True
        assert_that(comment.json().get('data')[0]).contains('id', 'post_id', 'author', 'content', 'like_count',
                                                            'is_like', 'is_report', 'time_difference', 'created_at',
                                                            'updated_at', 'mentions')

    def test_get_comment_forum_wrong_id(self):
        param = {
            'post_id': 998877665544332211
        }
        comment = requests.get(settings.url_get_comment_forum_customer, params=param,
                               headers=settings.header_with_token_customer)

        assert comment.status_code == 200
        assert comment.json().get('message') == "Komentar ditemukan"
        assert comment.json().get('success') == True

    def test_get_comment_forum_string_post_id(self):
        param = {
            'post_id': 'aabbccdd'
        }
        comment = requests.get(settings.url_get_comment_forum_customer, params=param,
                               headers=settings.header_with_token_customer)

        assert comment.status_code == 422
        assert "post id harus berupa angka." in comment.json().get('message')['post_id']
        assert comment.json().get('success') == False

    def test_get_comment_forum_wrong_token(self):
        param = {
            'post_id': settings.var_index_forum().json().get('data')['popular_posts'][0]['id']
        }
        comment = requests.get(settings.url_get_comment_forum_customer, params=param,
                               headers=settings.header_wrong_token_customer)

        assert comment.status_code == 401
        assert comment.json().get('message') == "Unauthorized"
        assert comment.json().get('success') == False

    def test_get_comment_forum_empty_token(self):
        param = {
            'post_id': settings.var_index_forum().json().get('data')['popular_posts'][0]['id']
        }
        comment = requests.get(settings.url_get_comment_forum_customer, params=param,
                               headers=settings.header_without_token_customer)

        assert comment.status_code == 401
        assert comment.json().get('message') == "Unauthorized"
        assert comment.json().get('success') == False
