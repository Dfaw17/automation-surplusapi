import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')

review = requests.post(settings.url_like_unlike_review_customer + str(
    settings.var_index_review().json().get('data')['reviews'][0]['id']) + '/like-dislike',
                       headers=settings.header_with_token_customer)
print(review.json())