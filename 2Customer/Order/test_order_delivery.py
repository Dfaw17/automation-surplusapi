import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerDelivery:

    def test_od_normal_gosend(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')
        verify_data = delivery.json().get('data')

        assert delivery.status_code == 201
        assert verify_status == bool(True)
        assert "Order Delivery berhasil dibuat" in verify_message
        assert_that(verify_data).is_not_none()

    def test_od_normal_grab(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "Test Notes",
            "delivery_price": "11000",
            "delivery_provider": "GRAB",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')
        verify_data = delivery.json().get('data')

        assert delivery.status_code == 201
        assert verify_status == bool(True)
        assert "Order Delivery berhasil dibuat" in verify_message
        assert_that(verify_data).is_not_none()

    def test_od_wrong_token(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
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
                                 headers=settings.header_wrong_token_customer)
        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')

        assert delivery.status_code == 401
        assert verify_status == bool(False)
        assert "Unauthorized" in verify_message

    def test_od_without_param_token(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
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
                                 headers=settings.header_without_token_customer)
        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')

        assert delivery.status_code == 401
        assert verify_status == bool(False)
        assert "Unauthorized" in verify_message

    def test_od_without_param_metode_pembayaran(self):
        param = {
            # "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')

        assert delivery.status_code == 400
        assert verify_status == bool(False)
        assert "Metode pembayaran harus dipilih" in verify_message

    def test_od_metode_pembayaran_empty_value(self):
        param = {
            "payment_method_id": "",
            "is_lunchbox": "0",
            "donation_price": "2500",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['payment_method_id']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Metode Pembayaran yang dipilih tidak tersedia." in verify_message

    def test_od_metode_pembayaran_text_value(self):
        param = {
            "payment_method_id": "cash",
            "is_lunchbox": "0",
            "donation_price": "2500",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['payment_method_id'][0]

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Metode Pembayaran yang dipilih tidak tersedia." in verify_message

    def test_od_metode_pembayaran_wrong_value(self):
        param = {
            "payment_method_id": "10",
            "is_lunchbox": "0",
            "donation_price": "2500",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['payment_method_id'][0]

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Metode Pembayaran yang dipilih tidak tersedia." in verify_message

    def test_od_lunchbox_empty_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "",
            "donation_price": "2500",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['is_lunchbox'][0]

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Kotak makan tidak boleh kosong." in verify_message

    def test_od_without_param_lunchbox(self):
        param = {
            "payment_method_id": "1",
            # "is_lunchbox": "",
            "donation_price": "2500",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['is_lunchbox'][0]

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Kotak makan tidak boleh kosong." in verify_message

    def test_od_lunchbox_text_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "a",
            "donation_price": "2500",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['is_lunchbox'][0]

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Kotak makan harus bernilai true atau false." in verify_message

    def test_od_lunchbox_not_bool_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "7",
            "donation_price": "2500",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['is_lunchbox'][0]

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Kotak makan harus bernilai true atau false." in verify_message

    def test_od_donation_empty_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['donation_price'][0]

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Jumlah donasi harus berupa angka." in verify_message

    def test_od_without_param_donation(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            # "donation_price": "",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')

        assert delivery.status_code == 201
        assert verify_status == bool(True)
        assert "Order Delivery berhasil dibuat" in verify_message

    def test_od_donation_text_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "aaa",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['donation_price']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Jumlah donasi harus berupa angka." in verify_message

    def test_od_donation_value_kurang_2500(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "1000",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['donation_price']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Jumlah donasi harus diantara 2500 dan 30000" in verify_message

    def test_od_voucher_empty_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "voucher_id": "",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['voucher_id']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Voucher harus berupa angka." in verify_message

    def test_od_without_param_voucher(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            # "voucher_id": "",
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

        verify_status = delivery.json().get('success')

        assert delivery.status_code == 201
        assert verify_status == bool(True)

    def test_od_voucher_not_found(self):
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')

        assert delivery.status_code == 500
        assert verify_status == bool(False)
        assert "Aduh!" in verify_message

    def test_od_voucher_text_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "voucher_id": "voucher",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['voucher_id']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Voucher harus berupa angka." in verify_message

    def test_od_stock_id_empty_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            # "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0]['stock_id'],
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['order_items.0.stock_id']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "order_items.0.stock_id tidak boleh kosong." in verify_message

    def test_od_without_param_stock_id(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            # "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0]['stock_id'],
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['order_items.0.stock_id']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "order_items.0.stock_id tidak boleh kosong." in verify_message

    def test_od_stock_id_text_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": 'makan',
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['order_items.0.stock_id']

        assert delivery.status_code == 422
        assert verify_status == bool(False)

    def test_od_stock_id_not_found(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": '9999999',
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')[0]['message']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Menu tidak ditemukan" in verify_message

    def test_od_qty_empty_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['order_items.0.qty']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "order_items.0.qty tidak boleh kosong." in verify_message

    def test_od_without_param_qty(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            # "order_items[0][qty]": "",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['order_items.0.qty']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "order_items.0.qty tidak boleh kosong." in verify_message

    def test_od_qty_value_text(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "a",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['order_items.0.qty']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "order_items.0.qty harus berupa angka." in verify_message

    def test_od_qty_minus_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "-10",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['order_items.0.qty']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "order_items.0.qty harus diantara 1 dan 999" in verify_message

    def test_od_qty_kurang_stock(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "999",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')[0]['message']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "tidak tersedia" in verify_message

    def test_od_without_param_note(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            # "note": "Test Notes",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')

        assert delivery.status_code == 500
        assert verify_status == bool(False)
        assert "Aduh!" in verify_message

    def test_od_note_empty_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')

        assert delivery.status_code == 201
        assert verify_status == bool(True)
        assert "Order Delivery berhasil dibuat" in verify_message

    def test_od_address_empty_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "",
            "note": "",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['address']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Alamat tidak boleh kosong." in verify_message

    def test_od_without_param_address(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            # "address": "",
            "note": "",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['address']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Alamat tidak boleh kosong." in verify_message

    def test_od_price_empty_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "",
            "delivery_price": "",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['delivery_price']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Ongkos kirim tidak boleh kosong." in verify_message

    def test_od_without_param_price(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "",
            # "delivery_price": "",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['delivery_price']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Ongkos kirim tidak boleh kosong." in verify_message

    def test_od_price_text_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "",
            "delivery_price": "aaa",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['delivery_price']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Ongkos kirim harus berupa angka." in verify_message

    def test_od_price_wrong_format(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "",
            "delivery_price": "19:00",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['delivery_price']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Ongkos kirim harus berupa angka." in verify_message

    def test_price_minus_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "",
            "delivery_price": "-21000",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')

        assert delivery.status_code == 500
        assert verify_status == bool(False)
        assert "Aduh!" in verify_message

    def test_od_methode_empty_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "",
            "delivery_price": "21000",
            "delivery_provider": "GOSEND",
            "delivery_method": "",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['delivery_method']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Metode pengiriman tidak boleh kosong." in verify_message

    def test_od_without_param_methode(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "",
            "delivery_price": "21000",
            "delivery_provider": "GOSEND",
            # "delivery_method": "",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['delivery_method']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Metode pengiriman tidak boleh kosong." in verify_message

    def test_od_methode_not_found(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "",
            "delivery_price": "21000",
            "delivery_provider": "GOSEND",
            "delivery_method": "AOI",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['delivery_method']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Metode pengiriman yang dipilih tidak tersedia." in verify_message

    def test_od_origin_contact_name_empty_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "Test Notes",
            "delivery_price": "21000",
            "delivery_provider": "GOSEND",
            "delivery_method": "Instant",
            "origin_contact_name": "",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['origin_contact_name']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Nama toko tidak boleh kosong." in verify_message

    def test_od_without_param_origin_contact_name(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "Test Notes",
            "delivery_price": "21000",
            "delivery_provider": "GOSEND",
            "delivery_method": "Instant",
            # "origin_contact_name": "",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['origin_contact_name']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Nama toko tidak boleh kosong." in verify_message

    def test_od_origin_contact_phone_empty_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "Test Notes",
            "delivery_price": "21000",
            "delivery_provider": "GOSEND",
            "delivery_method": "Instant",
            "origin_contact_name": "Fawwaz",
            "origin_contact_phone": "",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['origin_contact_phone']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "No. HP toko tidak boleh kosong." in verify_message

    def test_od_without_param_origin_contact_phone(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "Test Notes",
            "delivery_price": "21000",
            "delivery_provider": "GOSEND",
            "delivery_method": "Instant",
            "origin_contact_name": "Fawwaz",
            # "origin_contact_phone": "",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['origin_contact_phone']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "No. HP toko tidak boleh kosong." in verify_message

    def test_od_origin_contact_phone_text_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "Test Notes",
            "delivery_price": "21000",
            "delivery_provider": "GOSEND",
            "delivery_method": "Instant",
            "origin_contact_name": "Fawwaz",
            "origin_contact_phone": "aabbcc",
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

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['origin_contact_phone']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "The No. HP toko format wrong." in verify_message

    def test_od_origin_address_empty_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "Test Notes",
            "delivery_price": "21000",
            "delivery_provider": "GOSEND",
            "delivery_method": "Instant",
            "origin_contact_name": "Fawwaz",
            "origin_contact_phone": "081386356616",
            "origin_address": "",
            "origin_lat_long": "-6.3823027,107.1162164",
            "destination_contact_name": "Fawwaz 2",
            "destination_contact_phone": "0857108194",
            "destination_address": "Perumahan Megaregency 2",
            "destination_lat_long": "-6.3772882,107.1062917",
            "phone_number": "085710819443"
        }
        delivery = requests.post(settings.url_delivery_customer, data=param,
                                 headers=settings.header_with_token_customer)

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['origin_address']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Alamat toko tidak boleh kosong." in verify_message

    def test_od_without_param_origin_address(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "Test Notes",
            "delivery_price": "21000",
            "delivery_provider": "GOSEND",
            "delivery_method": "Instant",
            "origin_contact_name": "Fawwaz",
            "origin_contact_phone": "081386356616",
            # "origin_address": "",
            "origin_lat_long": "-6.3823027,107.1162164",
            "destination_contact_name": "Fawwaz 2",
            "destination_contact_phone": "0857108194",
            "destination_address": "Perumahan Megaregency 2",
            "destination_lat_long": "-6.3772882,107.1062917",
            "phone_number": "085710819443"
        }
        delivery = requests.post(settings.url_delivery_customer, data=param,
                                 headers=settings.header_with_token_customer)

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['origin_address']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Alamat toko tidak boleh kosong." in verify_message

    def test_od_origin_address_value_kurang_10(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "Test Notes",
            "delivery_price": "21000",
            "delivery_provider": "GOSEND",
            "delivery_method": "Instant",
            "origin_contact_name": "Fawwaz",
            "origin_contact_phone": "081386356616",
            "origin_address": "a",
            "origin_lat_long": "-6.3823027,107.1162164",
            "destination_contact_name": "Fawwaz 2",
            "destination_contact_phone": "0857108194",
            "destination_address": "Perumahan Megaregency 2",
            "destination_lat_long": "-6.3772882,107.1062917",
            "phone_number": "085710819443"
        }
        delivery = requests.post(settings.url_delivery_customer, data=param,
                                 headers=settings.header_with_token_customer)

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['origin_address']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Alamat toko setidaknya harus 10 karakter." in verify_message

    def test_od_origin_latlong_empty_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "Test Notes",
            "delivery_price": "21000",
            "delivery_provider": "GOSEND",
            "delivery_method": "Instant",
            "origin_contact_name": "Fawwaz",
            "origin_contact_phone": "081386356616",
            "origin_address": "Perumahan Megaregency 1",
            "origin_lat_long": "",
            "destination_contact_name": "Fawwaz 2",
            "destination_contact_phone": "0857108194",
            "destination_address": "Perumahan Megaregency 2",
            "destination_lat_long": "-6.3772882,107.1062917",
            "phone_number": "085710819443"
        }
        delivery = requests.post(settings.url_delivery_customer, data=param,
                                 headers=settings.header_with_token_customer)

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['origin_lat_long']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Titik lokasi toko tidak boleh kosong." in verify_message

    def test_od_without_param_origin_lat_long(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "Test Notes",
            "delivery_price": "21000",
            "delivery_provider": "GOSEND",
            "delivery_method": "Instant",
            "origin_contact_name": "Fawwaz",
            "origin_contact_phone": "081386356616",
            "origin_address": "Perumahan Megaregency 1",
            # "origin_lat_long": "",
            "destination_contact_name": "Fawwaz 2",
            "destination_contact_phone": "0857108194",
            "destination_address": "Perumahan Megaregency 2",
            "destination_lat_long": "-6.3772882,107.1062917",
            "phone_number": "085710819443"
        }
        delivery = requests.post(settings.url_delivery_customer, data=param,
                                 headers=settings.header_with_token_customer)

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['origin_lat_long']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Titik lokasi toko tidak boleh kosong." in verify_message

    def test_od_origin_latlong_text_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "Test Notes",
            "delivery_price": "21000",
            "delivery_provider": "GOSEND",
            "delivery_method": "Instant",
            "origin_contact_name": "Fawwaz",
            "origin_contact_phone": "081386356616",
            "origin_address": "Perumahan Megaregency 1",
            "origin_lat_long": "aa",
            "destination_contact_name": "Fawwaz 2",
            "destination_contact_phone": "0857108194",
            "destination_address": "Perumahan Megaregency 2",
            "destination_lat_long": "-6.3772882,107.1062917",
            "phone_number": "085710819443"
        }
        delivery = requests.post(settings.url_delivery_customer, data=param,
                                 headers=settings.header_with_token_customer)

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['origin_lat_long']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "The Titik lokasi toko must be latitude and longitude." in verify_message

    def test_od_origin_latlong_wrong_format_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "Test Notes",
            "delivery_price": "21000",
            "delivery_provider": "GOSEND",
            "delivery_method": "Instant",
            "origin_contact_name": "Fawwaz",
            "origin_contact_phone": "081386356616",
            "origin_address": "Perumahan Megaregency 1",
            "origin_lat_long": "19:00",
            "destination_contact_name": "Fawwaz 2",
            "destination_contact_phone": "0857108194",
            "destination_address": "Perumahan Megaregency 2",
            "destination_lat_long": "-6.3772882,107.1062917",
            "phone_number": "085710819443"
        }
        delivery = requests.post(settings.url_delivery_customer, data=param,
                                 headers=settings.header_with_token_customer)

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['origin_lat_long']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "The Titik lokasi toko must be latitude and longitude." in verify_message

    def test_od_destination_contact_name_empty_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "Test Notes",
            "delivery_price": "21000",
            "delivery_provider": "GOSEND",
            "delivery_method": "Instant",
            "origin_contact_name": "Fawwaz",
            "origin_contact_phone": "081386356616",
            "origin_address": "Perumahan Megaregency 1",
             "origin_lat_long": "-6.3823027,107.1162164",
            "destination_contact_name": "",
            "destination_contact_phone": "0857108194",
            "destination_address": "Perumahan Megaregency 2",
            "destination_lat_long": "-6.3772882,107.1062917",
            "phone_number": "085710819443"
        }
        delivery = requests.post(settings.url_delivery_customer, data=param,
                                 headers=settings.header_with_token_customer)

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['destination_contact_name']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Nama penerima tidak boleh kosong." in verify_message

    def test_od_without_param_destination_contact_name(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "Test Notes",
            "delivery_price": "21000",
            "delivery_provider": "GOSEND",
            "delivery_method": "Instant",
            "origin_contact_name": "Fawwaz",
            "origin_contact_phone": "081386356616",
            "origin_address": "Perumahan Megaregency 1",
             "origin_lat_long": "-6.3823027,107.1162164",
            # "destination_contact_name": "",
            "destination_contact_phone": "0857108194",
            "destination_address": "Perumahan Megaregency 2",
            "destination_lat_long": "-6.3772882,107.1062917",
            "phone_number": "085710819443"
        }
        delivery = requests.post(settings.url_delivery_customer, data=param,
                                 headers=settings.header_with_token_customer)

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['destination_contact_name']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Nama penerima tidak boleh kosong." in verify_message

    def test_od_destination_contact_phone_empty_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "Test Notes",
            "delivery_price": "21000",
            "delivery_provider": "GOSEND",
            "delivery_method": "Instant",
            "origin_contact_name": "Fawwaz",
            "origin_contact_phone": "081386356616",
            "origin_address": "Perumahan Megaregency 1",
             "origin_lat_long": "-6.3823027,107.1162164",
            "destination_contact_name": "Fawwaz",
            "destination_contact_phone": "",
            "destination_address": "Perumahan Megaregency 2",
            "destination_lat_long": "-6.3772882,107.1062917",
            "phone_number": "085710819443"
        }
        delivery = requests.post(settings.url_delivery_customer, data=param,
                                 headers=settings.header_with_token_customer)

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['destination_contact_phone']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "No. HP penerima tidak boleh kosong." in verify_message

    def test_od_without_param_destination_contact_phone (self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "Test Notes",
            "delivery_price": "21000",
            "delivery_provider": "GOSEND",
            "delivery_method": "Instant",
            "origin_contact_name": "Fawwaz",
            "origin_contact_phone": "081386356616",
            "origin_address": "Perumahan Megaregency 1",
             "origin_lat_long": "-6.3823027,107.1162164",
            "destination_contact_name": "Fawwaz",
            # "destination_contact_phone": "",
            "destination_address": "Perumahan Megaregency 2",
            "destination_lat_long": "-6.3772882,107.1062917",
            "phone_number": "085710819443"
        }
        delivery = requests.post(settings.url_delivery_customer, data=param,
                                 headers=settings.header_with_token_customer)

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['destination_contact_phone']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "No. HP penerima tidak boleh kosong." in verify_message

    def test_ad_destination_contact_phone_text_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "Test Notes",
            "delivery_price": "21000",
            "delivery_provider": "GOSEND",
            "delivery_method": "Instant",
            "origin_contact_name": "Fawwaz",
            "origin_contact_phone": "081386356616",
            "origin_address": "Perumahan Megaregency 1",
             "origin_lat_long": "-6.3823027,107.1162164",
            "destination_contact_name": "Fawwaz",
            "destination_contact_phone": "aaa",
            "destination_address": "Perumahan Megaregency 2",
            "destination_lat_long": "-6.3772882,107.1062917",
            "phone_number": "085710819443"
        }
        delivery = requests.post(settings.url_delivery_customer, data=param,
                                 headers=settings.header_with_token_customer)

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['destination_contact_phone']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "The No. HP penerima format wrong." in verify_message

    def test_od_destination_address_empty_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "Test Notes",
            "delivery_price": "21000",
            "delivery_provider": "GOSEND",
            "delivery_method": "Instant",
            "origin_contact_name": "Fawwaz",
            "origin_contact_phone": "081386356616",
            "origin_address": "Perumahan Megaregency 1",
             "origin_lat_long": "-6.3823027,107.1162164",
            "destination_contact_name": "Fawwaz",
            "destination_contact_phone": "085710819443",
            "destination_address": "",
            "destination_lat_long": "-6.3772882,107.1062917",
            "phone_number": "085710819443"
        }
        delivery = requests.post(settings.url_delivery_customer, data=param,
                                 headers=settings.header_with_token_customer)

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['destination_address']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Alamat penerima tidak boleh kosong." in verify_message

    def test_od_without_param_destination_address(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "Test Notes",
            "delivery_price": "21000",
            "delivery_provider": "GOSEND",
            "delivery_method": "Instant",
            "origin_contact_name": "Fawwaz",
            "origin_contact_phone": "081386356616",
            "origin_address": "Perumahan Megaregency 1",
             "origin_lat_long": "-6.3823027,107.1162164",
            "destination_contact_name": "Fawwaz",
            "destination_contact_phone": "085710819443",
            # "destination_address": "",
            "destination_lat_long": "-6.3772882,107.1062917",
            "phone_number": "085710819443"
        }
        delivery = requests.post(settings.url_delivery_customer, data=param,
                                 headers=settings.header_with_token_customer)

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['destination_address']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Alamat penerima tidak boleh kosong." in verify_message

    def test_od_destination_address_value_kurang_10(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "Test Notes",
            "delivery_price": "21000",
            "delivery_provider": "GOSEND",
            "delivery_method": "Instant",
            "origin_contact_name": "Fawwaz",
            "origin_contact_phone": "081386356616",
            "origin_address": "Perumahan Megaregency 1",
             "origin_lat_long": "-6.3823027,107.1162164",
            "destination_contact_name": "Fawwaz",
            "destination_contact_phone": "085710819443",
            "destination_address": "a",
            "destination_lat_long": "-6.3772882,107.1062917",
            "phone_number": "085710819443"
        }
        delivery = requests.post(settings.url_delivery_customer, data=param,
                                 headers=settings.header_with_token_customer)

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['destination_address']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Alamat penerima setidaknya harus 10 karakter." in verify_message

    def test_od_destination_latlong_empty_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "Test Notes",
            "delivery_price": "21000",
            "delivery_provider": "GOSEND",
            "delivery_method": "Instant",
            "origin_contact_name": "Fawwaz",
            "origin_contact_phone": "081386356616",
            "origin_address": "Perumahan Megaregency 1",
             "origin_lat_long": "-6.3823027,107.1162164",
            "destination_contact_name": "Fawwaz",
            "destination_contact_phone": "085710819443",
            "destination_address": "Perumahan Megaregency 2",
            "destination_lat_long": "",
            "phone_number": "085710819443"
        }
        delivery = requests.post(settings.url_delivery_customer, data=param,
                                 headers=settings.header_with_token_customer)

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['destination_lat_long']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Titik lokasi penerime tidak boleh kosong." in verify_message

    def test_od_without_param_destination_latlong(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "Test Notes",
            "delivery_price": "21000",
            "delivery_provider": "GOSEND",
            "delivery_method": "Instant",
            "origin_contact_name": "Fawwaz",
            "origin_contact_phone": "081386356616",
            "origin_address": "Perumahan Megaregency 1",
             "origin_lat_long": "-6.3823027,107.1162164",
            "destination_contact_name": "Fawwaz",
            "destination_contact_phone": "085710819443",
            "destination_address": "Perumahan Megaregency 2",
            # "destination_lat_long": "",
            "phone_number": "085710819443"
        }
        delivery = requests.post(settings.url_delivery_customer, data=param,
                                 headers=settings.header_with_token_customer)

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['destination_lat_long']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "Titik lokasi penerime tidak boleh kosong." in verify_message

    def test_od_destination_latlong_text_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "Test Notes",
            "delivery_price": "21000",
            "delivery_provider": "GOSEND",
            "delivery_method": "Instant",
            "origin_contact_name": "Fawwaz",
            "origin_contact_phone": "081386356616",
            "origin_address": "Perumahan Megaregency 1",
             "origin_lat_long": "-6.3823027,107.1162164",
            "destination_contact_name": "Fawwaz",
            "destination_contact_phone": "085710819443",
            "destination_address": "Perumahan Megaregency 2",
            "destination_lat_long": "a",
            "phone_number": "085710819443"
        }
        delivery = requests.post(settings.url_delivery_customer, data=param,
                                 headers=settings.header_with_token_customer)

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['destination_lat_long']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "The Titik lokasi penerime must be latitude and longitude." in verify_message

    def test_od_destination_latlong_wrong_format_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
            "order_items[0][qty]": "1",
            "order_items[0][stock_id]": settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            "address": "Megaregency",
            "note": "Test Notes",
            "delivery_price": "21000",
            "delivery_provider": "GOSEND",
            "delivery_method": "Instant",
            "origin_contact_name": "Fawwaz",
            "origin_contact_phone": "081386356616",
            "origin_address": "Perumahan Megaregency 1",
             "origin_lat_long": "-6.3823027,107.1162164",
            "destination_contact_name": "Fawwaz",
            "destination_contact_phone": "085710819443",
            "destination_address": "Perumahan Megaregency 2",
            "destination_lat_long": "19:00",
            "phone_number": "085710819443"
        }
        delivery = requests.post(settings.url_delivery_customer, data=param,
                                 headers=settings.header_with_token_customer)


        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['destination_lat_long']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "The Titik lokasi penerime must be latitude and longitude." in verify_message

    def test_od_phone_empty_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
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
            "phone_number": ""
        }
        delivery = requests.post(settings.url_delivery_customer, data=param,
                                 headers=settings.header_with_token_customer)

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['phone_number']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "No. HP tidak boleh kosong ketika Metode Pembayaran adalah 1." in verify_message

    def test_od_without_param_phone(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
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
            # "phone_number": ""
        }
        delivery = requests.post(settings.url_delivery_customer, data=param,
                                 headers=settings.header_with_token_customer)

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['phone_number']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "No. HP tidak boleh kosong ketika Metode Pembayaran adalah 1." in verify_message

    def test_od_phone_text_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
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
            "phone_number": "a"
        }
        delivery = requests.post(settings.url_delivery_customer, data=param,
                                 headers=settings.header_with_token_customer)

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['phone_number']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "The No. HP format wrong." in verify_message

    def test_od_phone_wrong_format_value(self):
        param = {
            "payment_method_id": "1",
            "is_lunchbox": "0",
            "donation_price": "2500",
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
            "phone_number": "19:00"
        }
        delivery = requests.post(settings.url_delivery_customer, data=param,
                                 headers=settings.header_with_token_customer)

        verify_status = delivery.json().get('success')
        verify_message = delivery.json().get('message')['phone_number']

        assert delivery.status_code == 422
        assert verify_status == bool(False)
        assert "The No. HP format wrong." in verify_message

