import mysql.connector
import requests
import sys
import settings
from pprint import pprint
from datetime import *

sys.path.append('.../IntegrationTest')

# ================================================================================================
param = {
    'title': f'Test Voucherr Automation Danger 1 ongkir {settings.now}',
    'fixed_discount': '3000',
    'min_purchase': '1000',
    'max_usage': 3,
    'start_at': settings.today,
    'end_at': settings.seven_days,
    'target_id': 2,
    'is_branch_joinable': 0,
}
response = requests.post(settings.url_voucher_merchant, data=param, headers=settings.header_with_token_merchant)
data = response.json()
print(data)
print(response)
# ================================================================================================
# mydb = mysql.connector.connect(
#     host="aa93f9gb1m7iap.clslftpx6d63.ap-southeast-1.rds.amazonaws.com",
#     user="root",
#     password="rahasia0502",
#     database="ebdb"
# )
# query = mydb.cursor()
# query.execute('SELECT `id` FROM verify_requests where merchant_id = 10269 ORDER BY id DESC LIMIT 1')
# id = int(query.fetchone()[0])
# query.execute(f'UPDATE verify_requests SET status_verify_request_id=2 WHERE id={id}')
# mydb.commit()
# print(query.rowcount, "record(s) affected")
