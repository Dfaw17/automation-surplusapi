import sys
import requests
import settings
import time
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestCustomerReportCommentForum:

    def test_report_comment_forum_normal(self):
        param = {
            'forum_id': '360',
            'forum_komentar_id': '386',
            'forum_report_kategori_id': '1',
            'content': 'parah cuk'
        }
        reports_comment = requests.post(settings.url_reports_comment_forum_customer,
                                        headers=settings.header_with_token_customer, data=param)

        assert reports_comment.status_code == 200
        assert_that(reports_comment.json().get('success')).is_equal_to(True)
        assert_that(reports_comment.json().get('message')).is_equal_to("Komentar berhasil dilaporkan")

    def test_report_comment_forum_without_token(self):
        param = {
            'forum_id': '10',
            'forum_komentar_id': '197',
            'forum_report_kategori_id': '1',
            'content': 'parah cuk'
        }
        reports_comment = requests.post(settings.url_reports_comment_forum_customer,
                                        headers=settings.header_without_token_customer, data=param)

        assert reports_comment.status_code == 401
        assert_that(reports_comment.json().get('success')).is_equal_to(False)
        assert_that(reports_comment.json().get('message')).is_equal_to("Unauthorized")

    def test_report_comment_forum_wrong_token(self):
        param = {
            'forum_id': '10',
            'forum_komentar_id': '197',
            'forum_report_kategori_id': '1',
            'content': 'parah cuk'
        }
        reports_comment = requests.post(settings.url_reports_comment_forum_customer,
                                        headers=settings.header_wrong_token_customer, data=param)

        assert reports_comment.status_code == 401
        assert_that(reports_comment.json().get('success')).is_equal_to(False)
        assert_that(reports_comment.json().get('message')).is_equal_to("Unauthorized")

    def test_report_comment_forum_forum_id_empty(self):
        param = {
            'forum_id': '',
            'forum_komentar_id': '197',
            'forum_report_kategori_id': '1',
            'content': 'parah cuk'
        }
        reports_comment = requests.post(settings.url_reports_comment_forum_customer,
                                        headers=settings.header_with_token_customer, data=param)

        assert reports_comment.status_code == 422
        assert_that(reports_comment.json().get('success')).is_equal_to(False)

    def test_report_comment_forum_forum_id_string(self):
        param = {
            'forum_id': 'aaa',
            'forum_komentar_id': '197',
            'forum_report_kategori_id': '1',
            'content': 'parah cuk'
        }
        reports_comment = requests.post(settings.url_reports_comment_forum_customer,
                                        headers=settings.header_with_token_customer, data=param)

        assert reports_comment.status_code == 422
        assert_that(reports_comment.json().get('success')).is_equal_to(False)

    def test_report_comment_forum_forum_id_wrong(self):
        param = {
            'forum_id': '9988776655443322',
            'forum_komentar_id': '197',
            'forum_report_kategori_id': '1',
            'content': 'parah cuk'
        }
        reports_comment = requests.post(settings.url_reports_comment_forum_customer,
                                        headers=settings.header_with_token_customer, data=param)

        assert reports_comment.status_code == 500
        assert_that(reports_comment.json().get('success')).is_equal_to(False)
        assert "Aduh!" in reports_comment.json().get('message')

    def test_report_comment_forum_komentar_id_empty(self):
        param = {
            'forum_id': '10',
            'forum_komentar_id': '',
            'forum_report_kategori_id': '1',
            'content': 'parah cuk'
        }
        reports_comment = requests.post(settings.url_reports_comment_forum_customer,
                                        headers=settings.header_with_token_customer, data=param)

        assert reports_comment.status_code == 422
        assert_that(reports_comment.json().get('success')).is_equal_to(False)
        assert "Kategori forum tidak boleh kosong." in reports_comment.json().get('message')['forum_komentar_id']

    def test_report_comment_forum_komentar_id_string(self):
        param = {
            'forum_id': '10',
            'forum_komentar_id': '',
            'forum_report_kategori_id': '1',
            'content': 'parah cuk'
        }
        reports_comment = requests.post(settings.url_reports_comment_forum_customer,
                                        headers=settings.header_with_token_customer, data=param)

        assert reports_comment.status_code == 422
        assert_that(reports_comment.json().get('success')).is_equal_to(False)
        assert "Kategori forum tidak boleh kosong." in reports_comment.json().get('message')['forum_komentar_id']

    def test_report_comment_forum_komentar_id_wrong(self):
        param = {
            'forum_id': '10',
            'forum_komentar_id': '9988776655443322',
            'forum_report_kategori_id': '1',
            'content': 'parah cuk'
        }
        reports_comment = requests.post(settings.url_reports_comment_forum_customer,
                                        headers=settings.header_with_token_customer, data=param)

        assert reports_comment.status_code == 500
        assert_that(reports_comment.json().get('success')).is_equal_to(False)

    def test_report_comment_forum_kategori_id_empty(self):
        param = {
            'forum_id': '10',
            'forum_komentar_id': '197',
            'forum_report_kategori_id': '',
            'content': 'parah cuk'
        }
        reports_comment = requests.post(settings.url_reports_comment_forum_customer,
                                        headers=settings.header_with_token_customer, data=param)

        assert reports_comment.status_code == 422
        assert_that(reports_comment.json().get('success')).is_equal_to(False)
        assert "Kategori Laporan Forum tidak boleh kosong." in reports_comment.json().get('message')['forum_report_kategori_id']

    def test_report_comment_forum_kategori_id_string(self):
        param = {
            'forum_id': '10',
            'forum_komentar_id': '197',
            'forum_report_kategori_id': '',
            'content': 'parah cuk'
        }
        reports_comment = requests.post(settings.url_reports_comment_forum_customer,
                                        headers=settings.header_with_token_customer, data=param)

        assert reports_comment.status_code == 422
        assert_that(reports_comment.json().get('success')).is_equal_to(False)
        assert "Kategori Laporan Forum tidak boleh kosong." in reports_comment.json().get('message')['forum_report_kategori_id']

    def test_report_comment_forum_kategori_id_wrong(self):
        param = {
            'forum_id': '10',
            'forum_komentar_id': '197',
            'forum_report_kategori_id': '9988776655443322',
            'content': 'parah cuk'
        }
        reports_comment = requests.post(settings.url_reports_comment_forum_customer,
                                        headers=settings.header_with_token_customer, data=param)

        assert reports_comment.status_code == 500
        assert_that(reports_comment.json().get('success')).is_equal_to(False)