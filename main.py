import mysql.connector
import requests
import sys
import settings
import time
from pprint import pprint
from datetime import *

sys.path.append('.../IntegrationTest')

# ================================================================================================
param = {
    'order_number': settings.var_insert_review().json().get('data')['registrasi_order_number'],
    'rating': '5',
    'review': 'ok',
    'is_hide_name': '3'
}
insert_review = requests.post(settings.url_insert_review_customer,params=param, headers=settings.header_with_token_customer)
print(insert_review.json())
