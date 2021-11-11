import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerReportPostForum:

    def test_report_post_normal(self):
        param = {
            'forum_id': '10',
            'forum_report_kategori_id': '1',
            'content': 'parah cuk'
        }
        reports_comment = requests.post(settings.url_reports_post_forum_customer,
                                        headers=settings.header_with_token_customer, data=param)

        assert reports_comment.status_code == 200
        assert_that(reports_comment.json().get('success')).is_equal_to(True)
        assert_that(reports_comment.json().get('message')).is_equal_to("Forum berhasil dilaporkan")

    def test_report_post_wrong_token(self):
        param = {
            'forum_id': '10',
            'forum_report_kategori_id': '1',
            'content': 'parah cuk'
        }
        reports_comment = requests.post(settings.url_reports_post_forum_customer,
                                        headers=settings.header_wrong_token_customer, data=param)

        assert reports_comment.status_code == 401
        assert_that(reports_comment.json().get('success')).is_equal_to(False)
        assert_that(reports_comment.json().get('message')).is_equal_to("Unauthorized")

    def test_report_post_empty_token(self):
        param = {
            'forum_id': '10',
            'forum_report_kategori_id': '1',
            'content': 'parah cuk'
        }
        reports_comment = requests.post(settings.url_reports_post_forum_customer,
                                        headers=settings.header_without_token_customer, data=param)

        assert reports_comment.status_code == 401
        assert_that(reports_comment.json().get('success')).is_equal_to(False)
        assert_that(reports_comment.json().get('message')).is_equal_to("Unauthorized")

    def test_report_post_post_id_empty(self):
        param = {
            'forum_id': '',
            'forum_report_kategori_id': '1',
            'content': 'parah cuk'
        }
        reports_comment = requests.post(settings.url_reports_post_forum_customer,
                                        headers=settings.header_with_token_customer, data=param)

        assert reports_comment.status_code == 422
        assert_that(reports_comment.json().get('success')).is_equal_to(False)
        assert "Forum tidak boleh kosong." in reports_comment.json().get('message')['forum_id']

    def test_report_post_post_id_wrong(self):
        param = {
            'forum_id': '9988776655443322',
            'forum_report_kategori_id': '1',
            'content': 'parah cuk'
        }
        reports_comment = requests.post(settings.url_reports_post_forum_customer,
                                        headers=settings.header_with_token_customer, data=param)

        assert reports_comment.status_code == 500
        assert_that(reports_comment.json().get('success')).is_equal_to(False)

    def test_report_post_post_id_no_param(self):
        param = {
            # 'forum_id': '',
            'forum_report_kategori_id': '1',
            'content': 'parah cuk'
        }
        reports_comment = requests.post(settings.url_reports_post_forum_customer,
                                        headers=settings.header_with_token_customer, data=param)

        assert reports_comment.status_code == 422
        assert_that(reports_comment.json().get('success')).is_equal_to(False)
        assert "Forum tidak boleh kosong." in reports_comment.json().get('message')['forum_id']

    def test_report_post_post_id_string(self):
        param = {
            'forum_id': 'a',
            'forum_report_kategori_id': '1',
            'content': 'parah cuk'
        }
        reports_comment = requests.post(settings.url_reports_post_forum_customer,
                                        headers=settings.header_with_token_customer, data=param)

        assert reports_comment.status_code == 422
        assert_that(reports_comment.json().get('success')).is_equal_to(False)
        assert "Forum harus berupa angka." in reports_comment.json().get('message')['forum_id']

    def test_report_post_report_type_empty(self):
        param = {
            'forum_id': '10',
            'forum_report_kategori_id': '',
            'content': 'parah cuk'
        }
        reports_comment = requests.post(settings.url_reports_post_forum_customer,
                                        headers=settings.header_with_token_customer, data=param)

        assert reports_comment.status_code == 422
        assert_that(reports_comment.json().get('success')).is_equal_to(False)

    def test_report_post_report_type_wrong(self):
        param = {
            'forum_id': '10',
            'forum_report_kategori_id': '99',
            'content': 'parah cuk'
        }
        reports_comment = requests.post(settings.url_reports_post_forum_customer,
                                        headers=settings.header_with_token_customer, data=param)

        assert reports_comment.status_code == 500
        assert_that(reports_comment.json().get('success')).is_equal_to(False)
        assert "Aduh!" in reports_comment.json().get('message')

    def test_report_post_report_type_string(self):
        param = {
            'forum_id': '10',
            'forum_report_kategori_id': 'a',
            'content': 'parah cuk'
        }
        reports_comment = requests.post(settings.url_reports_post_forum_customer,
                                        headers=settings.header_with_token_customer, data=param)

        assert reports_comment.status_code == 422
        assert_that(reports_comment.json().get('success')).is_equal_to(False)
        assert "Kategori Laporan Forum harus berupa angka." in reports_comment.json().get('message')['forum_report_kategori_id']
