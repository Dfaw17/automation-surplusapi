import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerStoreCommentForum:

    def test_store_comment_forum_normal(self):
        param = {
            'post_id': '360',
            'comment': 'hahahha lol',
            'mentions[0]': 'kopiruangvirtual@gmail.com',
        }
        store_comment = requests.post(settings.url_store_comment_forum_customer,
                                      headers=settings.header_with_token_customer, data=param)

        assert store_comment.status_code == 201
        assert_that(store_comment.json().get('success')).is_equal_to(True)
        assert "Komentar berhasil diposting." in store_comment.json().get('message')
        assert_that(store_comment.json().get('data')).contains('id', 'post_id', 'author', 'content', 'like_count',
                                                               'is_like', 'is_report', 'time_difference', 'created_at',
                                                               'updated_at', 'mentions')

    def test_store_comment_forum_wrong_token(self):
        param = {
            'post_id': '10',
            'comment': 'hahahha lol',
            'mentions[0]': 'kopiruangvirtual@gmail.com',
        }
        store_comment = requests.post(settings.url_store_comment_forum_customer,
                                      headers=settings.header_wrong_token_customer, data=param)

        assert store_comment.status_code == 401
        assert_that(store_comment.json().get('success')).is_equal_to(False)
        assert_that(store_comment.json().get('message')).is_equal_to("Unauthorized")

    def test_store_comment_forum_token_empty(self):
        param = {
            'post_id': '10',
            'comment': 'hahahha lol',
            'mentions[0]': 'kopiruangvirtual@gmail.com',
        }
        store_comment = requests.post(settings.url_store_comment_forum_customer,
                                      headers=settings.header_without_token_customer, data=param)

        assert store_comment.status_code == 401
        assert_that(store_comment.json().get('success')).is_equal_to(False)
        assert_that(store_comment.json().get('message')).is_equal_to("Unauthorized")

    def test_store_comment_forum_wrong_post_id(self):
        param = {
            'post_id': '99999999',
            'comment': 'hahahha lol',
            'mentions[0]': 'kopiruangvirtual@gmail.com',
        }
        store_comment = requests.post(settings.url_store_comment_forum_customer,
                                      headers=settings.header_with_token_customer, data=param)

        assert store_comment.status_code == 500
        assert_that(store_comment.json().get('success')).is_equal_to(False)
        assert "Aduh!" in store_comment.json().get('message')

    def test_store_comment_forum_without_post_id(self):
        param = {
            # 'post_id': '99999999',
            'comment': 'hahahha lol',
            'mentions[0]': 'kopiruangvirtual@gmail.com',
        }
        store_comment = requests.post(settings.url_store_comment_forum_customer,
                                      headers=settings.header_with_token_customer, data=param)

        assert store_comment.status_code == 422
        assert_that(store_comment.json().get('success')).is_equal_to(False)
        assert "post id tidak boleh kosong." in store_comment.json().get('message')['post_id']

    def test_store_comment_forum_empty_post_id(self):
        param = {
            'post_id': '',
            'comment': 'hahahha lol',
            'mentions[0]': 'kopiruangvirtual@gmail.com',
        }
        store_comment = requests.post(settings.url_store_comment_forum_customer,
                                      headers=settings.header_with_token_customer, data=param)

        assert store_comment.status_code == 422
        assert_that(store_comment.json().get('success')).is_equal_to(False)
        assert "post id tidak boleh kosong." in store_comment.json().get('message')['post_id']

    def test_store_comment_forum_string_post_id(self):
        param = {
            'post_id': 'a',
            'comment': 'hahahha lol',
            'mentions[0]': 'kopiruangvirtual@gmail.com',
        }
        store_comment = requests.post(settings.url_store_comment_forum_customer,
                                      headers=settings.header_with_token_customer, data=param)

        assert store_comment.status_code == 422
        assert_that(store_comment.json().get('success')).is_equal_to(False)
        assert "post id harus berupa angka." in store_comment.json().get('message')['post_id']

    def test_store_comment_forum_without_comment(self):
        param = {
            'post_id': '10',
            # 'comment': 'hahahha lol',
            'mentions[0]': 'kopiruangvirtual@gmail.com',
        }
        store_comment = requests.post(settings.url_store_comment_forum_customer,
                                      headers=settings.header_with_token_customer, data=param)

        assert store_comment.status_code == 422
        assert_that(store_comment.json().get('success')).is_equal_to(False)
        assert "Komentar tidak boleh kosong." in store_comment.json().get('message')['comment']

    def test_store_comment_forum_empty_comment(self):
        param = {
            'post_id': '10',
            'comment': '',
            'mentions[0]': 'kopiruangvirtual@gmail.com',
        }
        store_comment = requests.post(settings.url_store_comment_forum_customer,
                                      headers=settings.header_with_token_customer, data=param)

        assert store_comment.status_code == 422
        assert_that(store_comment.json().get('success')).is_equal_to(False)
        assert "Komentar tidak boleh kosong." in store_comment.json().get('message')['comment']

    def test_store_comment_forum_without_mentions(self):
        param = {
            'post_id': '360',
            'comment': 'hahaha lol',
            # 'mentions[0]': 'kopiruangvirtual@gmail.com',
        }
        store_comment = requests.post(settings.url_store_comment_forum_customer,
                                      headers=settings.header_with_token_customer, data=param)

        assert store_comment.status_code == 201
        assert_that(store_comment.json().get('success')).is_equal_to(True)

    def test_store_comment_forum_wrong_mentions(self):
        param = {
            'post_id': '10',
            'comment': 'hahaha lol',
            'mentions[0]': 'kopiruangvirtual99@gmail.com',
        }
        store_comment = requests.post(settings.url_store_comment_forum_customer,
                                      headers=settings.header_with_token_customer, data=param)

        assert store_comment.status_code == 400
        assert_that(store_comment.json().get('success')).is_equal_to(False)
        assert "Tidak ada pengguna dengan email kopiruangvirtual99@gmail.com" in store_comment.json().get('message')
