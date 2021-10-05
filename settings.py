import requests
import mysql.connector

# ENVIRONTMENT
production = "https://adminsurplus.net"
stagging = "https://staging.adminsurplus.net"
sandbox = "https://sandbox.adminsurplus.net"
use_env = sandbox

# ACCOUNT MERCHANT
email_merchant = "jangandipakai1@gmail.com"
email_merchant_freeze = "jangandipakai3@gmail.com"
email_merchant_without_at = "jangandipakai1gmail.com"
email_merchant_space = "jangan di pakai1@gmail.com"
pwd_merchant = "12345678"
email_merchant_not_regist = "sdet999@gmail.com"
pwd_merchant_wrong = "000000000"
pwd_kurang_char = "123"
wrong_token_merchant = "AAAAABBBBCCCCDDDD"

# URL MERCHANT
url_login_merchant = f"{use_env}/api/v2/merchant/auth/login"
url_logout_merchant = f"{use_env}/api/v2/merchant/auth/logout"
url_reset_pwd_merchant = f"{use_env}/api/v2/merchant/auth/password-reset"
url_show_profile_merchant = f"{use_env}/api/v2/merchant/profiles"
url_verify_merchant = f"{use_env}/api/v2/merchant/verify-request"

# DATABASE
mydb = mysql.connector.connect(
    host="aa93f9gb1m7iap.clslftpx6d63.ap-southeast-1.rds.amazonaws.com",
    user="root",
    password="rahasia0502",
    database="ebdb"
)
query = mydb.cursor()


# VARIABLE
def var_login_merchant():
    param = {
        "email": email_merchant,
        "password": pwd_merchant
    }

    login = requests.post(url_login_merchant, data=param, headers={'Accept': 'application/json'})
    return login
def var_reject_verify_merchant():
    query.execute('SELECT `id` FROM verify_requests where merchant_id = 10269 ORDER BY id DESC LIMIT 1')
    id = int(query.fetchone()[0])
    query.execute(f'UPDATE verify_requests SET status_verify_request_id=2 WHERE id={id}')
    mydb.commit()
    print(query.rowcount, "record(s) affected")


# HEADER SETTING
header_with_token_merchant = {"Authorization": f"Bearer {var_login_merchant().json().get('token')}","Accept": "application/json"}
header_without_token_merchant = {"Authorization": f"Bearer ","Accept": "application/json"}
header_wrong_token_merchant = {"Authorization": f"Bearer {wrong_token_merchant}","Accept": "application/json"}
