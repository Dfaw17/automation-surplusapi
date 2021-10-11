import requests
import mysql.connector

# DATABASE
mydb = mysql.connector.connect(
    host="aa93f9gb1m7iap.clslftpx6d63.ap-southeast-1.rds.amazonaws.com",
    user="root",
    password="rahasia0502",
    database="ebdb"
)
query = mydb.cursor()

# ENVIRONTMENT
production = "https://adminsurplus.net"
stagging = "https://staging.adminsurplus.net"
sandbox = "https://sandbox.adminsurplus.net"
use_env = sandbox

# ACCOUNT MERCHANT
email_merchant = "jangandipakai1@gmail.com"
email_merchant_branch = "jangandipakai2@gmail.com"
email_merchant_freeze = "jangandipakai3@gmail.com"
email_merchant_without_at = "jangandipakai1gmail.com"
email_merchant_space = "jangan di pakai1@gmail.com"
pwd_merchant = "12345678"
email_merchant_not_regist = "sdet999@gmail.com"
pwd_merchant_wrong = "000000000"
pwd_kurang_char = "123"
wrong_token_merchant = "AAAAABBBBCCCCDDDD"
nama_makanan = "Cessin"
merchant_kategori_sayur = 5
merchant_kategori_non_sayur = 1
deskripsi = "Cessin Meikarta"
harga_asli = 20000
harga_jual = 10000
status_halal = 0
weight = 200
weight_string = "1 Mangkok"
menu_sayur = '628'
menu_non_sayur = '731'
merchant_central = '10269'
merchant_branch = '10270'
# URL MERCHANT
url_login_merchant = f"{use_env}/api/v2/merchant/auth/login"
url_logout_merchant = f"{use_env}/api/v2/merchant/auth/logout"
url_reset_pwd_merchant = f"{use_env}/api/v2/merchant/auth/password-reset"
url_show_profile_merchant = f"{use_env}/api/v2/merchant/profiles"
url_verify_merchant = f"{use_env}/api/v2/merchant/verify-request"
url_get_all_category_merchant = f"{use_env}/api/v2/merchant/categories"
url_get_all_merchant_menu_merchant = f"{use_env}/api/v2/merchant/menus/"
url_insert_menu_merchant = f"{use_env}/api/v2/merchant/menus"
url_update_menu_merchant = f"{use_env}/api/v2/merchant/menus/"
url_set_active_menu_merchant = f"{use_env}/api/v2/merchant/menus/"
url_set_inactive_menu_merchant = f"{use_env}/api/v2/merchant/menus/"
url_delete_menu_merchant = f"{use_env}/api/v2/merchant/menus/"
url_index_order_merchant = f"{use_env}/api/v2/merchant/orders"
url_show_order_merchant = f"{use_env}/api/v2/merchant/orders/"
url_history_trx_merchant = f"{use_env}/api/v2/merchant/reports/transaction-history"
url_history_income_merchant = f"{use_env}/api/v2/merchant/reports/income-history"
url_branch_merchant = f"{use_env}/api/v2/merchant/branches"
url_outlet_rating_merchant = f"{use_env}/api/v2/merchant/reports/outlet-rating"
url_available_menu_merchant = f"{use_env}/api/v2/merchant/menus/available"

# VARIABLE
def var_login_merchant():
    param = {
        "email": email_merchant,
        "password": pwd_merchant
    }

    login = requests.post(url_login_merchant, data=param, headers={'Accept': 'application/json'})
    return login


def var_login_merchant_branch():
    param = {
        "email": email_merchant_branch,
        "password": pwd_merchant
    }

    login = requests.post(url_login_merchant, data=param, headers={'Accept': 'application/json'})
    return login


def var_list_menu_merchant():
    list_menu = requests.get(url_get_all_merchant_menu_merchant, headers=header_with_token_merchant)
    return list_menu


def var_list_order_merchant():
    order = requests.get(url_index_order_merchant + '?type=finish', headers=header_with_token_merchant)
    return order


def var_reject_verify_merchant():
    query.execute('SELECT `id` FROM verify_requests where merchant_id = 10269 ORDER BY id DESC LIMIT 1')
    id = int(query.fetchone()[0])
    query.execute(f'UPDATE verify_requests SET status_verify_request_id=2 WHERE id={id}')
    mydb.commit()
    print(query.rowcount, "record(s) affected")


# HEADER SETTING
header_with_token_merchant = {"Authorization": f"Bearer {var_login_merchant().json().get('token')}","Accept": "application/json"}
header_branch= {"Authorization": f"Bearer {var_login_merchant_branch().json().get('token')}","Accept": "application/json"}
header_without_token_merchant = {"Authorization": f"Bearer ", "Accept": "application/json"}
header_wrong_token_merchant = {"Authorization": f"Bearer {wrong_token_merchant}", "Accept": "application/json"}
