import mysql.connector
import requests
import sys
import settings
from pprint import pprint
from datetime import *

sys.path.append('.../IntegrationTest')

# ================================================================================================
param = {
    "payment_method_id": "1",
    "is_lunchbox": "0",
    "donation_price": "2500",
    "voucher_id": "999999999",
    "order_items[0][qty]": "1",
    "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
        'stock_id'],
    "address": "Megaregency",
    "note": "Test Notes",
    "delivery_price": "21000",
    "delivery_provider": "GOSEND",
    "delivery_method": "Instant",
    "origin_contact_name": "Fawwaz 1",
    "origin_contact_phone": "081386356616",
    "origin_address": "Perumahan Megaregency 1",
    "origin_lat_long": "-6.3823027,107.1162164",
    "destination_contact_name": "Fawwaz 2",
    "destination_contact_phone": "0857108194",
    "destination_address": "Perumahan Megaregency 2",
    "destination_lat_long": "-6.3772882,107.1062917",
    "phone_number": "085710819443"
}
delivery = requests.post(settings.url_delivery_customer, data=param,
                         headers=settings.header_with_token_customer)

print(delivery.json())
