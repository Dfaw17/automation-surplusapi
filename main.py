import mysql.connector
import requests
import sys
import settings
sys.path.append('.../IntegrationTest')


# ================================================================================================
# token = settings.var_login_merchant().json().get("token")
# param = {
#     "certifications[certifications][0][certification_id]": 1,
#     "certifications[certifications][0][name]": 'null',
# }
# response = requests.post(settings.url_verify_merchant, data=param, headers={"Authorization": f"Bearer {token}","Accept": "application/json"}, files={
#     'certifications[images][0]': open("img/telkomsel.png", 'rb'),
# })
# data = response.json()
# print(data)
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
