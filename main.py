import mysql.connector
import requests
import sys
import settings
from pprint import pprint
from datetime import *

sys.path.append('.../IntegrationTest')

# ================================================================================================
show_voucher = requests.get(settings.url_show_voucher_customer + str(settings.var_list_voucher_customer().json().get('data')['voucher_surplus'][0]['id']),headers=settings.header_with_token_customer)
print(show_voucher.json())
