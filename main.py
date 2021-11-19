import mysql.connector
import requests
import sys
import settings
from pprint import pprint
from datetime import *

sys.path.append('.../IntegrationTest')

# ================================================================================================
print(settings.var_order_selfpickup().json().get('data')['registrasi_order_number'])
