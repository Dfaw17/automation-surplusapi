import requests
import mysql.connector
from datetime import *
from faker import Faker

fake = Faker()

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
menu_sayur = 947
menu_non_sayur = 948
menu_barnch = 995
merchant_central = '10269'
merchant_branch = '10270'
now = datetime.today().strftime('%Y%m%d')
today = datetime.today().strftime('%Y-%m-%d')
calc = datetime.today() + timedelta(days=7)
seven_days = calc.strftime('%Y-%m-%d')
# ---------------------------------------------------------------------------
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
url_voucher_merchant = f"{use_env}/api/v2/merchant/voucher"
url_get_voucher_central_merchant = f"{use_env}/api/v2/merchant/voucher-central"

# ACCOUNT CUSTOMER
fake_email = fake.email()
kata_sandi = "12345678"
email_has_registered = 'kopi.ruang.rehat@gmail.com'
email_belum_register = 'kopiruangvirtual99@gmail.com'
email_oauth = "daffafawwazmaulana170901@gmail.com"
origin_id = "2840811776172986"
origin = "facebook"
wrong_token_customer = "AAAAABBBBCCCCDDDD"
lat = '-6.3823317'
long = '107.1162607'
id_merchant_pusat = '10269'
# ---------------------------------------------------------------------------
url_register_email_customer = f"{use_env}/api/v2/customer/auth/register/email"
url_register_oauth_customer = f"{use_env}/api/v2/customer/auth/register/oauth"
url_delete_account_customer = f"{use_env}/api/v2/customer/profiles"
url_login_auth_customer = f"{use_env}/api/v2/customer/auth/login/oauth"
url_login_email_customer = f"{use_env}/api/v2/customer/auth/login/email"
url_register_progress_customer = f"{use_env}/api/v2/customer/auth/register/progress"
url_check_email_customer = f"{use_env}/api/v2/customer/auth/register/check-email"
url_reset_password_customer = f"{use_env}/api/v2/customer/auth/password-reset"
url_logout_customer = f"{use_env}/api/v2/customer/auth/logout"
url_discover_customer = f"{use_env}/api/v2/customer/discover"
url_search_customer = f"{use_env}/api/v2/customer/search"
url_show_menu_customer = f"{use_env}/api/v2/customer/menus/"
url_show_merchants_customer = f"{use_env}/api/v2/customer/merchants/"
url_like_merchant_customer = f"{use_env}/api/v2/customer/merchants/"
url_list_merchant_customer = f"{use_env}/api/v2/customer/merchants"
url_index_menu_customer = f"{use_env}/api/v2/customer/menus"
url_banner_customer = f"{use_env}/api/v2/customer/banners"
url_index_address_customer = f"{use_env}/api/v2/customer/address/"
url_show_address_customer = f"{use_env}/api/v2/customer/address/"
url_create_address_customer = f"{use_env}/api/v2/customer/address"
url_delete_address_customer = f"{use_env}/api/v2/customer/address/"
url_show_profiles_customer = f"{use_env}/api/v2/customer/profiles"
url_list_voucher_customer = f"{use_env}/api/v2/customer/vouchers"
url_fav_merchant_customer = f"{use_env}/api/v2/customer/profiles/favorite-merchant"
url_update_private_data_customer = f"{use_env}/api/v2/customer/profiles/private-data"
url_update_password_customer = f"{use_env}/api/v2/customer/profiles/password"
url_index_voucher_customer = f"{use_env}/api/v2/customer/vouchers"
url_show_voucher_customer = f"{use_env}/api/v2/customer/vouchers/"
url_list_order_customer = f"{use_env}/api/v2/customer/orders"
url_detail_order_customer = f"{use_env}/api/v2/customer/orders/"
url_show_payment_status_customer = f"{use_env}/api/v2/customer/orders/"
url_checkout_customer = f"{use_env}/api/v2/customer/orders/checkout"
url_index_review_customer = f"{use_env}/api/v2/customer/public/reviews"
url_like_unlike_review_customer = f"{use_env}/api/v2/customer/reviews/"
url_like_report_unreport_customer = f"{use_env}/api/v2/customer/reviews/"
url_index_forum_customer = f"{use_env}/api/v2/customer/forums"
url_show_forum_customer = f"{use_env}/api/v2/customer/forums/"
url_get_comment_forum_customer = f"{use_env}/api/v2/customer/comments"
url_profile_forum_customer = f"{use_env}/api/v2/customer/profile-forums"
url_store_forum_customer = f"{use_env}/api/v2/customer/forums"
url_like_unlike_forum_customer = f"{use_env}/api/v2/customer/likes"
url_store_comment_forum_customer = f"{use_env}/api/v2/customer/comments"
url_reports_comment_forum_customer = f"{use_env}/api/v2/customer/reports/comment"


# VARIABLE
def var_login_customer():
    param = {
        'email': email_has_registered,
        'password': kata_sandi
    }
    login = requests.post(url_login_email_customer, data=param, headers={'Accept': 'application/json'})
    return login


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


def var_list_menu_discover():
    param2 = {
        'latitude': lat,
        'longitude': long
    }
    discover = requests.get(url_discover_customer, params=param2, headers=header_with_token_customer)
    return discover


def var_list_menu_merchant():
    list_menu = requests.get(url_get_all_merchant_menu_merchant, headers=header_with_token_merchant)
    return list_menu


def var_list_order_merchant():
    order = requests.get(url_index_order_merchant + '?type=finish', headers=header_with_token_merchant)
    return order


def var_list_voucher_customer():
    voucher = requests.get(url_index_address_customer, headers=header_with_token_customer)
    return voucher


def var_reject_verify_merchant():
    query.execute('SELECT `id` FROM verify_requests where merchant_id = 10269 ORDER BY id DESC LIMIT 1')
    id = int(query.fetchone()[0])
    query.execute(f'UPDATE verify_requests SET status_verify_request_id=2 WHERE id={id}')
    mydb.commit()
    print(query.rowcount, "record(s) affected")


def var_deleted_menu():
    deleted_menu = var_list_menu_merchant().json().get('data')

    if deleted_menu[0]['id'] == menu_sayur or deleted_menu[0]['id'] == menu_non_sayur:
        if deleted_menu[1]['id'] == menu_sayur or deleted_menu[0]['id'] == menu_non_sayur:
            menu = deleted_menu[2]['id']
        else:
            menu = deleted_menu[1]['id']
    else:
        menu = deleted_menu[0]['id']

    return menu


def var_list_order_customer():
    param2 = {
        'status_order': 'done'
    }
    list_order = requests.get(url_list_order_customer, params=param2, headers=header_with_token_customer)
    return list_order


def var_index_forum():
    index = requests.get(url_index_forum_customer, headers=header_with_token_customer)
    return index


def var_index_review():
    param = {
        'filter_by': 'all',
        'merchant_id': id_merchant_pusat
    }

    review = requests.get(url_index_review_customer, params=param,
                          headers=header_with_token_customer)
    return review


# HEADER SETTING
header_with_token_merchant = {"Authorization": f"Bearer {var_login_merchant().json().get('token')}",
                              "Accept": "application/json"}
header_branch = {"Authorization": f"Bearer {var_login_merchant_branch().json().get('token')}",
                 "Accept": "application/json"}
header_without_token_merchant = {"Authorization": f"Bearer ", "Accept": "application/json"}
header_wrong_token_merchant = {"Authorization": f"Bearer {wrong_token_merchant}", "Accept": "application/json"}

header_with_token_customer = {"Authorization": f"Bearer {var_login_customer().json().get('token')}",
                              "Accept": "application/json"}
header_wrong_token_customer = {"Authorization": f"Bearer {wrong_token_customer}", "Accept": "application/json"}
header_without_token_customer = {"Authorization": f"Bearer ", "Accept": "application/json"}
