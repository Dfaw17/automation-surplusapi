import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerShowForum:

    def test_show_forum_normal(self):
        show = requests.get(settings.url_show_forum_customer + str(
            settings.var_index_forum().json().get('data')['newest_posts'][0]['id']),
                            headers=settings.header_with_token_customer)

        assert show.status_code == 200
        assert_that(show.json().get('success')).is_equal_to(True)
        assert_that(show.json().get('data')).contains('id', 'author', 'category_id', 'content', 'attachments',
                                                      'comment_count', 'like_count', 'is_like', 'is_report',
                                                      'is_bookmark', 'time_difference')
        assert_that(show.json().get('data')['author']).contains('id', 'name', 'badge_id', 'is_author', 'is_admin')
        assert_that(show.json().get('data')['attachments']).contains('link', 'location', 'images')

    def test_show_forum_wrong_id(self):
        show = requests.get(settings.url_show_forum_customer + '998877665544332211',
                            headers=settings.header_with_token_customer)

        assert show.status_code == 404
        assert_that(show.json().get('success')).is_equal_to(False)
        assert_that(show.json().get('message')).is_equal_to('Data forum tidak ditemukan')

    def test_show_forum_id_string(self):
        show = requests.get(settings.url_show_forum_customer + 'aabbccdd',
                            headers=settings.header_with_token_customer)

        assert show.status_code == 404
        assert_that(show.json().get('success')).is_equal_to(False)
        assert_that(show.json().get('message')).is_equal_to('Data forum tidak ditemukan')

    def test_show_forum_wrong_token(self):
        show = requests.get(settings.url_show_forum_customer + str(
            settings.var_index_forum().json().get('data')['newest_posts'][0]['id']),
                            headers=settings.header_wrong_token_customer)

        assert show.status_code == 401
        assert_that(show.json().get('success')).is_equal_to(False)
        assert_that(show.json().get('message')).is_equal_to('Unauthorized')

    def test_show_forum_empty_token(self):
        show = requests.get(settings.url_show_forum_customer + str(
            settings.var_index_forum().json().get('data')['newest_posts'][0]['id']),
                            headers=settings.header_without_token_customer)

        assert show.status_code == 401
        assert_that(show.json().get('success')).is_equal_to(False)
        assert_that(show.json().get('message')).is_equal_to('Unauthorized')
