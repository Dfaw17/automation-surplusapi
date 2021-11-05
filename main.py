import mysql.connector
import requests
import sys
import settings
from pprint import pprint
from datetime import *

sys.path.append('.../IntegrationTest')

# ================================================================================================
param = {
    'post_id': settings.var_index_forum().json().get('data')['popular_posts'][0]['id']
}
comment = requests.get(settings.url_get_comment_forum_customer, params=param,
                       headers=settings.header_wrong_token_customer)
print(comment.json())
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
