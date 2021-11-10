import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerProfileForum:

    def test_profile_forum_normal(self):
        profile = requests.get(settings.url_profile_forum_customer, headers=settings.header_with_token_customer)

        assert profile.status_code == 200
        assert_that(profile.json().get('message')).is_equal_to("Data profile forum berhasil ditemukan.")
        assert_that(profile.json().get('data')).contains('post_count', 'like_count', 'bookmark_count', 'newest_posts',
                                                         'saved_posts', 'liked_posts')

    def test_profile_forum_empty_token(self):
        profile = requests.get(settings.url_profile_forum_customer, headers=settings.header_without_token_customer)

        assert profile.status_code == 401
        assert_that(profile.json().get('message')).is_equal_to("Unauthorized")

    def test_profile_forum_wrong_token(self):
        profile = requests.get(settings.url_profile_forum_customer, headers=settings.header_wrong_token_customer)

        assert profile.status_code == 401
        assert_that(profile.json().get('message')).is_equal_to("Unauthorized")