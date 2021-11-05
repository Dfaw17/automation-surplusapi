import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')

class TestCustomerIndexForum:

    def test_index_forum_normal(self):
        index = requests.get(settings.url_index_forum_customer, headers=settings.header_with_token_customer)

        assert index.status_code == 200
        assert_that(index.json().get('success')).is_equal_to(True)
        assert_that(index.json().get('data')).contains('donation_event', 'popular_posts', 'liked_posts', 'saved_posts', 'newest_posts')

    def test_index_forum_wrong_token(self):
        index = requests.get(settings.url_index_forum_customer, headers=settings.header_wrong_token_customer)

        assert index.status_code == 401
        assert_that(index.json().get('success')).is_equal_to(False)
        assert_that(index.json().get('message')).is_equal_to('Unauthorized')

    def test_index_forum_without_token(self):
        index = requests.get(settings.url_index_forum_customer, headers=settings.header_without_token_customer)

        assert index.status_code == 401
        assert_that(index.json().get('success')).is_equal_to(False)
        assert_that(index.json().get('message')).is_equal_to('Unauthorized')