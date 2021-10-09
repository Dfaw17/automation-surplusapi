import mysql.connector
import requests
import sys
import settings
from pprint import pprint

sys.path.append('.../IntegrationTest')

# ================================================================================================
param = {
    "max_active_date": "2022-09-09",
    "waktu_mulai_penjemputan": "00:30",
    "waktu_akhir_penjemputan": "23:00"
}

response = requests.patch(settings.url_set_active_menu_merchant + "554" + "/partial", data=param,
                          headers=settings.header_branch)
data = response.json()
pprint(data)
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
