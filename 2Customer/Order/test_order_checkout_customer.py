import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerCheckout:

    def test_checkout_normal(self):
        param = {
            'email': 'kopiruangvirtual@gmail.com',
            'delivery_price': '21000',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
        }
        checkout = requests.post(settings.url_checkout_customer, params=param,
                                 headers=settings.header_with_token_customer)

        validate_status = checkout.json().get('success')
        validate_message = checkout.json().get('message')['menu']
        validate_data = checkout.json().get('data')

        assert checkout.status_code == 200
        assert_that(validate_status).is_equal_to(True)
        assert_that(validate_message).is_equal_to("Data menu berhasil ditemukan.")
        assert_that(validate_data).contains('errors', 'order_items', 'donation_price', 'delivery_price',
                                            'surplus_discount', 'lunchbox_discount', 'voucher_discount',
                                            'voucher_target_id', 'grand_total', 'subtotal', 'saving', 'merchant_fee',
                                            'surplus_fee', 'pickup_time')

    def test_checkout_wrong_token(self):
        param = {
            'email': 'kopiruangvirtual@gmail.com',
            'delivery_price': '21000',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
        }
        checkout = requests.post(settings.url_checkout_customer, params=param,
                                 headers=settings.header_wrong_token_customer)

        validate_status = checkout.json().get('success')
        validate_message = checkout.json().get('message')

        assert checkout.status_code == 401
        assert_that(validate_status).is_equal_to(False)
        assert_that(validate_message).is_equal_to("Unauthorized")

    def test_checkout_emprty_token(self):
        param = {
            'email': 'kopiruangvirtual@gmail.com',
            'delivery_price': '21000',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
        }
        checkout = requests.post(settings.url_checkout_customer, params=param,
                                 headers=settings.header_without_token_customer)

        validate_status = checkout.json().get('success')
        validate_message = checkout.json().get('message')

        assert checkout.status_code == 401
        assert_that(validate_status).is_equal_to(False)
        assert_that(validate_message).is_equal_to("Unauthorized")

    def test_checkout_without_delivery_price(self):
        param = {
            'email': 'kopiruangvirtual@gmail.com',
            # 'delivery_price': '21000',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
        }
        checkout = requests.post(settings.url_checkout_customer, params=param,
                                 headers=settings.header_with_token_customer)

        validate_status = checkout.json().get('success')
        validate_message = checkout.json().get('message')['menu']
        validate_data = checkout.json().get('data')

        assert checkout.status_code == 200
        assert_that(validate_status).is_equal_to(True)
        assert_that(validate_message).is_equal_to("Data menu berhasil ditemukan.")
        assert_that(validate_data).contains('errors', 'order_items', 'donation_price', 'delivery_price',
                                            'surplus_discount', 'lunchbox_discount', 'voucher_discount',
                                            'voucher_target_id', 'grand_total', 'subtotal', 'saving', 'merchant_fee',
                                            'surplus_fee', 'pickup_time')

    def test_checkout_empty_delivery_price(self):
        param = {
            'email': 'kopiruangvirtual@gmail.com',
            'delivery_price': '',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
        }
        checkout = requests.post(settings.url_checkout_customer, params=param,
                                 headers=settings.header_with_token_customer)

        validate_status = checkout.json().get('success')

        assert checkout.status_code == 422
        assert_that(validate_status).is_equal_to(False)

    def test_checkout_text_delivery_price(self):
        param = {
            'email': 'kopiruangvirtual@gmail.com',
            'delivery_price': 'aabbcc',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
        }
        checkout = requests.post(settings.url_checkout_customer, params=param,
                                 headers=settings.header_with_token_customer)

        validate_status = checkout.json().get('success')
        validate_message = checkout.json().get('message')['delivery_price']

        assert checkout.status_code == 422
        assert_that(validate_status).is_equal_to(False)

    def test_checkout_wrong_format_delivery_price(self):
        param = {
            'email': 'kopiruangvirtual@gmail.com',
            'delivery_price': '11:00',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
        }
        checkout = requests.post(settings.url_checkout_customer, params=param,
                                 headers=settings.header_with_token_customer)

        validate_status = checkout.json().get('success')
        validate_message = checkout.json().get('message')['delivery_price']

        assert checkout.status_code == 422
        assert_that(validate_status).is_equal_to(False)

    def test_checkout_minus_delivery_price(self):
        param = {
            'email': 'kopiruangvirtual@gmail.com',
            'delivery_price': '-11000',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
        }
        checkout = requests.post(settings.url_checkout_customer, params=param,
                                 headers=settings.header_with_token_customer)

        validate_status = checkout.json().get('success')
        validate_message = checkout.json().get('message')['menu']

        assert checkout.status_code == 200
        assert_that(validate_status).is_equal_to(True)
        assert_that(validate_message).is_equal_to("Data menu berhasil ditemukan.")

    def test_checkout_without_lunchbox(self):
        param = {
            'email': 'kopiruangvirtual@gmail.com',
            'delivery_price': '21000',
            # 'is_lunchbox': '0',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
        }
        checkout = requests.post(settings.url_checkout_customer, params=param,
                                 headers=settings.header_with_token_customer)

        validate_status = checkout.json().get('success')
        validate_message = checkout.json().get('message')['is_lunchbox']

        assert checkout.status_code == 422
        assert_that(validate_status).is_equal_to(False)

    def test_checkout_text_lunchbox(self):
        param = {
            'email': 'kopiruangvirtual@gmail.com',
            'delivery_price': '21000',
            'is_lunchbox': 'aa',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
        }
        checkout = requests.post(settings.url_checkout_customer, params=param,
                                 headers=settings.header_with_token_customer)

        validate_status = checkout.json().get('success')

        assert checkout.status_code == 422
        assert_that(validate_status).is_equal_to(False)

    def test_checkout_not_boolean_lunchbox(self):
        param = {
            'email': 'kopiruangvirtual@gmail.com',
            'delivery_price': '21000',
            'is_lunchbox': '3',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
        }
        checkout = requests.post(settings.url_checkout_customer, params=param,
                                 headers=settings.header_with_token_customer)

        validate_status = checkout.json().get('success')

        assert checkout.status_code == 422
        assert_that(validate_status).is_equal_to(False)

    def test_checkout_empty_lunchbox(self):
        param = {
            'email': 'kopiruangvirtual@gmail.com',
            'delivery_price': '21000',
            'is_lunchbox': '',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
        }
        checkout = requests.post(settings.url_checkout_customer, params=param,
                                 headers=settings.header_with_token_customer)

        validate_status = checkout.json().get('success')

        assert checkout.status_code == 422
        assert_that(validate_status).is_equal_to(False)

    def test_checkout_empty_donation(self):
        param = {
            'email': 'kopiruangvirtual@gmail.com',
            'delivery_price': '21000',
            'is_lunchbox': '0',
            'donation_price': '',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
        }
        checkout = requests.post(settings.url_checkout_customer, params=param,
                                 headers=settings.header_with_token_customer)

        validate_status = checkout.json().get('success')

        assert checkout.status_code == 422
        assert_that(validate_status).is_equal_to(False)

    def test_checkout_without_donation(self):
        param = {
            'email': 'kopiruangvirtual@gmail.com',
            'delivery_price': '21000',
            'is_lunchbox': '0',
            # 'donation_price': '',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
        }
        checkout = requests.post(settings.url_checkout_customer, params=param,
                                 headers=settings.header_with_token_customer)

        validate_status = checkout.json().get('success')

        assert checkout.status_code == 200
        assert_that(validate_status).is_equal_to(True)

    def test_checkout_kurang_2500_donation(self):
        param = {
            'email': 'kopiruangvirtual@gmail.com',
            'delivery_price': '21000',
            'is_lunchbox': '0',
            'donation_price': '1000',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
        }
        checkout = requests.post(settings.url_checkout_customer, params=param,
                                 headers=settings.header_with_token_customer)

        validate_status = checkout.json().get('success')

        assert checkout.status_code == 422
        assert_that(validate_status).is_equal_to(False)

    def test_checkout_text_donation(self):
        param = {
            'email': 'kopiruangvirtual@gmail.com',
            'delivery_price': '21000',
            'is_lunchbox': '0',
            'donation_price': 'aa',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '1',
        }
        checkout = requests.post(settings.url_checkout_customer, params=param,
                                 headers=settings.header_with_token_customer)

        validate_status = checkout.json().get('success')

        assert checkout.status_code == 422
        assert_that(validate_status).is_equal_to(False)

    def test_checkout_empty_qty(self):
        param = {
            'email': 'kopiruangvirtual@gmail.com',
            'delivery_price': '21000',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '',
        }
        checkout = requests.post(settings.url_checkout_customer, params=param,
                                 headers=settings.header_with_token_customer)

        validate_status = checkout.json().get('success')

        assert checkout.status_code == 422
        assert_that(validate_status).is_equal_to(False)

    def test_checkout_without_qty_id(self):
        param = {
            'email': 'kopiruangvirtual@gmail.com',
            'delivery_price': '21000',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[qty]': '1',
        }
        checkout = requests.post(settings.url_checkout_customer, params=param,
                                 headers=settings.header_with_token_customer)

        validate_status = checkout.json().get('success')

        assert checkout.status_code == 422
        assert_that(validate_status).is_equal_to(False)

    def test_checkout_text_qty(self):
        param = {
            'email': 'kopiruangvirtual@gmail.com',
            'delivery_price': '21000',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': 'a',
        }
        checkout = requests.post(settings.url_checkout_customer, params=param,
                                 headers=settings.header_with_token_customer)

        validate_status = checkout.json().get('success')

        assert checkout.status_code == 422
        assert_that(validate_status).is_equal_to(False)

    def test_checkout_qty_more_than_stock(self):
        param = {
            'email': 'kopiruangvirtual@gmail.com',
            'delivery_price': '21000',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'order_items[0][stock_id]': settings.var_list_menu_discover().json().get('data')['nearby_menu'][0][
                'stock_id'],
            'order_items[0][qty]': '999',
        }
        checkout = requests.post(settings.url_checkout_customer, params=param,
                                 headers=settings.header_with_token_customer)

        validate_status = checkout.json().get('success')

        assert checkout.status_code == 200
        assert_that(validate_status).is_equal_to(True)

    def test_checkout_empty_stock_id(self):
        param = {
            'email': 'kopiruangvirtual@gmail.com',
            'delivery_price': '21000',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'order_items[0][stock_id]': '',
            'order_items[0][qty]': '1',
        }
        checkout = requests.post(settings.url_checkout_customer, params=param,
                                 headers=settings.header_with_token_customer)

        validate_status = checkout.json().get('success')

        assert checkout.status_code == 422
        assert_that(validate_status).is_equal_to(False)

    def test_checkout_without_stock_id(self):
        param = {
            'email': 'kopiruangvirtual@gmail.com',
            'delivery_price': '21000',
            'is_lunchbox': '0',
            'donation_price': '2500',
            # 'order_items[0][stock_id]': '',
            'order_items[0][qty]': '1',
        }
        checkout = requests.post(settings.url_checkout_customer, params=param,
                                 headers=settings.header_with_token_customer)

        validate_status = checkout.json().get('success')

        assert checkout.status_code == 422
        assert_that(validate_status).is_equal_to(False)

    def test_checkout_text_stock_id(self):
        param = {
            'email': 'kopiruangvirtual@gmail.com',
            'delivery_price': '21000',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'order_items[0][stock_id]': 'aaa',
            'order_items[0][qty]': '1',
        }
        checkout = requests.post(settings.url_checkout_customer, params=param,
                                 headers=settings.header_with_token_customer)

        validate_status = checkout.json().get('success')

        assert checkout.status_code == 422
        assert_that(validate_status).is_equal_to(False)

    def test_checkout_wrong_stock_id(self):
        param = {
            'email': 'kopiruangvirtual@gmail.com',
            'delivery_price': '21000',
            'is_lunchbox': '0',
            'donation_price': '2500',
            'order_items[0][stock_id]': '99667788',
            'order_items[0][qty]': '1',
        }
        checkout = requests.post(settings.url_checkout_customer, params=param,
                                 headers=settings.header_with_token_customer)

        validate_status = checkout.json().get('success')

        assert checkout.status_code == 500
        assert_that(validate_status).is_equal_to(False)

