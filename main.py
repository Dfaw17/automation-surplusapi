import mysql.connector
import requests
import sys
import settings
from pprint import pprint
from datetime import *

sys.path.append('.../IntegrationTest')

# ================================================================================================
param2 = {
    'latitude': 'aaa',
    'longitude': settings.long
}
show_merchants = requests.get(settings.url_show_merchants_customer + str(settings.var_list_menu_discover().json().get('data')['nearby_merchant'][0]['merchant_id']),
                         params=param2, headers=settings.header_with_token_customer)
data = show_merchants.json()
print(data)
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
