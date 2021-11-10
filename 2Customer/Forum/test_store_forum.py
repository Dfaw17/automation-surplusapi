import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerStoreForum:

    def test_store_forum_normal(self):
        param = {
            'category_id': '1',
            'content': 'Test Automation Store Forum',
            'link[url]': 'https://surplus.id',
            'link[title]': 'Surplus Indonesia',
            'link[image]': 'https://postku.site/assets/img/bg-postku2.png',
            'location[address]': 'Surplus Indonesia',
            'location[note]': 'Surplus Indonesia',
            'location[name]': 'Doyok',
            'location[phone]': '081386356616',
            'location[latitude]': '-6.1944617',
            'location[longitude]': '106.8657752',
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        store = requests.post(settings.url_store_forum_customer, headers=settings.header_with_token_customer,
                              data=param, files=file)

        assert store.status_code == 201
        assert_that(store.json().get('success')).is_equal_to(True)
        assert_that(store.json().get('message')).is_equal_to("Data forum berhasil diposting.")

    def test_store_forum_header_without_token(self):
        param = {
            'category_id': '1',
            'content': 'Test Automation Store Forum',
            'link[url]': 'https://surplus.id',
            'link[title]': 'Surplus Indonesia',
            'link[image]': 'https://postku.site/assets/img/bg-postku2.png',
            'location[address]': 'Surplus Indonesia',
            'location[note]': 'Surplus Indonesia',
            'location[name]': 'Doyok',
            'location[phone]': '081386356616',
            'location[latitude]': '-6.1944617',
            'location[longitude]': '106.8657752',
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        store = requests.post(settings.url_store_forum_customer, headers=settings.header_without_token_customer,
                              data=param, files=file)

        assert store.status_code == 401
        assert_that(store.json().get('success')).is_equal_to(False)
        assert_that(store.json().get('message')).is_equal_to("Unauthorized")

    def test_store_forum_header_empty_token(self):
        param = {
            'category_id': '1',
            'content': 'Test Automation Store Forum',
            'link[url]': 'https://surplus.id',
            'link[title]': 'Surplus Indonesia',
            'link[image]': 'https://postku.site/assets/img/bg-postku2.png',
            'location[address]': 'Surplus Indonesia',
            'location[note]': 'Surplus Indonesia',
            'location[name]': 'Doyok',
            'location[phone]': '081386356616',
            'location[latitude]': '-6.1944617',
            'location[longitude]': '106.8657752',
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        store = requests.post(settings.url_store_forum_customer, headers=settings.header_without_token_customer,
                              data=param, files=file)

        assert store.status_code == 401
        assert_that(store.json().get('success')).is_equal_to(False)
        assert_that(store.json().get('message')).is_equal_to("Unauthorized")

    def test_store_forum_header_wrong_token(self):
        param = {
            'category_id': '1',
            'content': 'Test Automation Store Forum',
            'link[url]': 'https://surplus.id',
            'link[title]': 'Surplus Indonesia',
            'link[image]': 'https://postku.site/assets/img/bg-postku2.png',
            'location[address]': 'Surplus Indonesia',
            'location[note]': 'Surplus Indonesia',
            'location[name]': 'Doyok',
            'location[phone]': '081386356616',
            'location[latitude]': '-6.1944617',
            'location[longitude]': '106.8657752',
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        store = requests.post(settings.url_store_forum_customer, headers=settings.header_wrong_token_customer,
                              data=param, files=file)

        assert store.status_code == 401
        assert_that(store.json().get('success')).is_equal_to(False)
        assert_that(store.json().get('message')).is_equal_to("Unauthorized")

    def test_store_forum_withot_category_id(self):
        param = {
            'category_id': '',
            'content': 'Test Automation Store Forum',
            'link[url]': 'https://surplus.id',
            'link[title]': 'Surplus Indonesia',
            'link[image]': 'https://postku.site/assets/img/bg-postku2.png',
            'location[address]': 'Surplus Indonesia',
            'location[note]': 'Surplus Indonesia',
            'location[name]': 'Doyok',
            'location[phone]': '081386356616',
            'location[latitude]': '-6.1944617',
            'location[longitude]': '106.8657752',
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        store = requests.post(settings.url_store_forum_customer, headers=settings.header_with_token_customer,
                              data=param, files=file)

        assert store.status_code == 422
        assert_that(store.json().get('success')).is_equal_to(False)
        assert "category id tidak boleh kosong." in store.json().get('message')['category_id']

    def test_store_forum_withot_category_wrong(self):
        param = {
            'category_id': '1000',
            'content': 'Test Automation Store Forum',
            'link[url]': 'https://surplus.id',
            'link[title]': 'Surplus Indonesia',
            'link[image]': 'https://postku.site/assets/img/bg-postku2.png',
            'location[address]': 'Surplus Indonesia',
            'location[note]': 'Surplus Indonesia',
            'location[name]': 'Doyok',
            'location[phone]': '081386356616',
            'location[latitude]': '-6.1944617',
            'location[longitude]': '106.8657752',
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        store = requests.post(settings.url_store_forum_customer, headers=settings.header_with_token_customer,
                              data=param, files=file)

        assert store.status_code == 500
        assert_that(store.json().get('success')).is_equal_to(False)
        assert 'Aduh!' in store.json().get('message')

    def test_store_forum_empty_category_id(self):
        param = {
            # 'category_id': '',
            'content': 'Test Automation Store Forum',
            'link[url]': 'https://surplus.id',
            'link[title]': 'Surplus Indonesia',
            'link[image]': 'https://postku.site/assets/img/bg-postku2.png',
            'location[address]': 'Surplus Indonesia',
            'location[note]': 'Surplus Indonesia',
            'location[name]': 'Doyok',
            'location[phone]': '081386356616',
            'location[latitude]': '-6.1944617',
            'location[longitude]': '106.8657752',
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        store = requests.post(settings.url_store_forum_customer, headers=settings.header_with_token_customer,
                              data=param, files=file)

        assert store.status_code == 422
        assert_that(store.json().get('success')).is_equal_to(False)
        assert "category id tidak boleh kosong." in store.json().get('message')['category_id']

    def test_store_forum_empty_content(self):
        param = {
            'category_id': '1',
            'content': '',
            'link[url]': 'https://surplus.id',
            'link[title]': 'Surplus Indonesia',
            'link[image]': 'https://postku.site/assets/img/bg-postku2.png',
            'location[address]': 'Surplus Indonesia',
            'location[note]': 'Surplus Indonesia',
            'location[name]': 'Doyok',
            'location[phone]': '081386356616',
            'location[latitude]': '-6.1944617',
            'location[longitude]': '106.8657752',
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        store = requests.post(settings.url_store_forum_customer, headers=settings.header_with_token_customer,
                              data=param, files=file)

        assert store.status_code == 422
        assert_that(store.json().get('success')).is_equal_to(False)
        assert "Isi tidak boleh kosong." in store.json().get('message')['content']

    def test_store_forum_without_content(self):
        param = {
            'category_id': '1',
            # 'content': '',
            'link[url]': 'https://surplus.id',
            'link[title]': 'Surplus Indonesia',
            'link[image]': 'https://postku.site/assets/img/bg-postku2.png',
            'location[address]': 'Surplus Indonesia',
            'location[note]': 'Surplus Indonesia',
            'location[name]': 'Doyok',
            'location[phone]': '081386356616',
            'location[latitude]': '-6.1944617',
            'location[longitude]': '106.8657752',
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        store = requests.post(settings.url_store_forum_customer, headers=settings.header_with_token_customer,
                              data=param, files=file)

        assert store.status_code == 422
        assert_that(store.json().get('success')).is_equal_to(False)
        assert "Isi tidak boleh kosong." in store.json().get('message')['content']
