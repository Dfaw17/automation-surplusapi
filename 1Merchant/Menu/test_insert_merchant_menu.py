import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestInserMerchantMenu:

    def test_insert_menu_kat_sayur_normal(self):
        param = {
            "nama_menu_makanan": settings.nama_makanan,
            "merchant_kategori_makanan_id": settings.merchant_kategori_sayur,
            "deskripsi": settings.deskripsi,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": "0",
            "weight": settings.weight
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_insert_menu_merchant, data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")
        validate_data = data.get("data")
        validate_nama = data.get("data")['nama_menu_makanan']
        validate_kategori = data.get("data")['merchant_kategori_makanan_id']
        validate_deskripsi = data.get("data")['deskripsi']
        validate_harga_asli = data.get("data")['harga_asli']
        validate_harga_jual = data.get("data")['harga_jual']
        validate_weight = data.get("data")['weight']

        assert response.status_code == 201
        assert validate_status == bool(True)
        assert f"Data menu {settings.nama_makanan} berhasil ditambahkan." in validate_message
        assert_that(validate_weight).is_equal_to(settings.weight)
        assert_that(validate_harga_jual).is_equal_to(settings.harga_jual)
        assert_that(validate_harga_asli).is_equal_to(settings.harga_asli)
        assert_that(validate_deskripsi).is_equal_to(settings.deskripsi)
        assert_that(validate_kategori).is_equal_to(settings.merchant_kategori_sayur)
        assert_that(validate_nama).is_equal_to(settings.nama_makanan)
        assert_that(validate_data).contains('id', 'merchant_id', 'nama_menu_makanan', 'merchant_kategori_makanan_id',
                                            'merchant_kategori_makanan_id', 'deskripsi', 'waktu_mulai_penjemputan',
                                            'waktu_akhir_penjemputan', 'harga_asli', 'harga_jual', 'stock',
                                            'is_non_halal', 'total_terjual', 'is_missed', 'is_active', 'weight',
                                            'weight_string', 'waktu_missed', 'image_thumbnail', 'created_at',
                                            'updated_at', 'is_tomorrow')

    def test_insert_menu_kat_non_sayur_normal(self):
        param = {
            "nama_menu_makanan": settings.nama_makanan,
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": settings.deskripsi,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": "0",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_insert_menu_merchant, data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")
        validate_data = data.get("data")
        validate_nama = data.get("data")['nama_menu_makanan']
        validate_kategori = data.get("data")['merchant_kategori_makanan_id']
        validate_deskripsi = data.get("data")['deskripsi']
        validate_harga_asli = data.get("data")['harga_asli']
        validate_harga_jual = data.get("data")['harga_jual']
        validate_weight_string = data.get("data")['weight_string']

        assert response.status_code == 201
        assert validate_status == bool(True)
        assert f"Data menu {settings.nama_makanan} berhasil ditambahkan." in validate_message
        assert_that(validate_weight_string).is_equal_to(settings.weight_string)
        assert_that(validate_harga_jual).is_equal_to(settings.harga_jual)
        assert_that(validate_harga_asli).is_equal_to(settings.harga_asli)
        assert_that(validate_deskripsi).is_equal_to(settings.deskripsi)
        assert_that(validate_kategori).is_equal_to(settings.merchant_kategori_non_sayur)
        assert_that(validate_nama).is_equal_to(settings.nama_makanan)
        assert_that(validate_data).contains('id', 'merchant_id', 'nama_menu_makanan', 'merchant_kategori_makanan_id',
                                            'merchant_kategori_makanan_id', 'deskripsi', 'waktu_mulai_penjemputan',
                                            'waktu_akhir_penjemputan', 'harga_asli', 'harga_jual', 'stock',
                                            'is_non_halal', 'total_terjual', 'is_missed', 'is_active', 'weight',
                                            'weight_string', 'waktu_missed', 'image_thumbnail', 'created_at',
                                            'updated_at', 'is_tomorrow')

    def test_insert_menu_empty_token(self):
        param = {
            "nama_menu_makanan": settings.nama_makanan,
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": settings.deskripsi,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": "0",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_insert_menu_merchant, data=param,
                                 headers=settings.header_without_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message

    def test_insert_menu_wrong_token(self):
        param = {
            "nama_menu_makanan": settings.nama_makanan,
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": settings.deskripsi,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": "0",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_insert_menu_merchant, data=param,
                                 headers=settings.header_wrong_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message

    def test_insert_menu_empty_nama_menu_value(self):
        param = {
            "nama_menu_makanan": '',
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": settings.deskripsi,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": "0",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_insert_menu_merchant, data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")['nama_menu_makanan']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Nama menu tidak boleh kosong." in validate_message

    def test_insert_menu_without_param_nama_menu(self):
        param = {
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": settings.deskripsi,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": "0",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_insert_menu_merchant, data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")['nama_menu_makanan']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Nama menu tidak boleh kosong." in validate_message

    def test_insert_menu_kategori_makanan_id_wrong_value(self):
        param = {
            "nama_menu_makanan": settings.nama_makanan,
            "merchant_kategori_makanan_id": 500,
            "deskripsi": settings.deskripsi,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": "0",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_insert_menu_merchant, data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 404
        assert validate_status == bool(False)
        assert "Data gagal dibuat." in validate_message

    def test_insert_menu_kategori_makanan_id_empty(self):
        param = {
            "merchant_kategori_makanan_id": "",
            "nama_menu_makanan": settings.nama_makanan,
            "deskripsi": settings.deskripsi,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": "0",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_insert_menu_merchant, data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")['merchant_kategori_makanan_id']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Kategori menu tidak boleh kosong." in validate_message

    def test_insert_menu_without_param_kategori_makanan_id(self):
        param = {
            "nama_menu_makanan": settings.nama_makanan,
            "deskripsi": settings.deskripsi,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": "0",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_insert_menu_merchant, data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")['merchant_kategori_makanan_id']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Kategori menu tidak boleh kosong." in validate_message

    def test_insert_menu_deskripsi_empty(self):
        param = {
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "nama_menu_makanan": settings.nama_makanan,
            "deskripsi": '',
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": "0",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_insert_menu_merchant, data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")['deskripsi']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "deskripsi tidak boleh kosong." in validate_message

    def test_insert_menu_without_param_deskripsi(self):
        param = {
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "nama_menu_makanan": settings.nama_makanan,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": "0",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_insert_menu_merchant, data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")['deskripsi']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "deskripsi tidak boleh kosong." in validate_message

    def test_insert_menu_harga_asli_empty(self):
        param = {
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": settings.deskripsi,
            "nama_menu_makanan": settings.nama_makanan,
            "harga_asli": '',
            "harga_jual": settings.harga_jual,
            "is_non_halal": "0",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_insert_menu_merchant, data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")['harga_asli']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Harga asli tidak boleh kosong." in validate_message

    def test_insert_menu_without_param_harga_asli(self):
        param = {
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": settings.deskripsi,
            "nama_menu_makanan": settings.nama_makanan,
            "harga_jual": settings.harga_jual,
            "is_non_halal": "0",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_insert_menu_merchant, data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")['harga_asli']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Harga asli tidak boleh kosong." in validate_message

    def test_insert_menu_harga_asli_string_value(self):
        param = {
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": settings.deskripsi,
            "nama_menu_makanan": settings.nama_makanan,
            "harga_jual": settings.harga_jual,
            "harga_asli": 'aaa',
            "is_non_halal": "0",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_insert_menu_merchant, data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")['harga_asli']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "format harga asli yang diinputkan salah" in validate_message

    def test_insert_menu_harga_jual_empty(self):
        param = {
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": settings.deskripsi,
            "nama_menu_makanan": settings.nama_makanan,
            "harga_jual": '',
            "harga_asli": settings.harga_asli,
            "is_non_halal": "0",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_insert_menu_merchant, data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")['harga_jual']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Harga jual tidak boleh kosong." in validate_message

    def test_insert_menu_harga_jual_string_value(self):
        param = {
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": settings.deskripsi,
            "nama_menu_makanan": settings.nama_makanan,
            "harga_jual": 'a',
            "harga_asli": settings.harga_asli,
            "is_non_halal": "0",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_insert_menu_merchant, data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")['harga_jual']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "format harga jual yang diinputkan salah" in validate_message

    def test_insert_menu_without_param_harga_jual(self):
        param = {
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": settings.deskripsi,
            "nama_menu_makanan": settings.nama_makanan,
            "harga_asli": settings.harga_asli,
            "is_non_halal": "0",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_insert_menu_merchant, data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")['harga_jual']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Harga jual tidak boleh kosong." in validate_message

    def test_insert_menu_is_non_halal_empty(self):
        param = {
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": settings.deskripsi,
            "nama_menu_makanan": settings.nama_makanan,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": "",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_insert_menu_merchant, data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")['is_non_halal']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Menu tidak halal tidak boleh kosong." in validate_message

    def test_insert_menu_is_non_halal_wrong_value(self):
        param = {
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": settings.deskripsi,
            "nama_menu_makanan": settings.nama_makanan,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": "5",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_insert_menu_merchant, data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")['is_non_halal']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Menu tidak halal harus bernilai true atau false." in validate_message

    def test_insert_menu_without_param_is_non_halal(self):
        param = {
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": settings.deskripsi,
            "nama_menu_makanan": settings.nama_makanan,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_insert_menu_merchant, data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")['is_non_halal']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Menu tidak halal tidak boleh kosong." in validate_message

    def test_insert_menu_sayur_without_param_weight(self):
        param = {
            "merchant_kategori_makanan_id": settings.merchant_kategori_sayur,
            "deskripsi": settings.deskripsi,
            "nama_menu_makanan": settings.nama_makanan,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": settings.status_halal,
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_insert_menu_merchant, data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")['weight']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "weight tidak boleh kosong ketika Kategori menu adalah 5." in validate_message

    def test_insert_menu_sayur_wight_empty_value(self):
        param = {
            "merchant_kategori_makanan_id": settings.merchant_kategori_sayur,
            "deskripsi": settings.deskripsi,
            "nama_menu_makanan": settings.nama_makanan,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": settings.status_halal,
            "weight": ''
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_insert_menu_merchant, data=param,
                                 headers=settings.header_with_token_merchant, files=file)

        data = response.json()
        validate_status = data.get("success")
        validate_message = data.get("message")['weight']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "weight tidak boleh kosong ketika Kategori menu adalah 5." in validate_message

    def test_insert_menu_sayur_weight_string_value(self):
        param = {
            "merchant_kategori_makanan_id": settings.merchant_kategori_sayur,
            "deskripsi": settings.deskripsi,
            "nama_menu_makanan": settings.nama_makanan,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": settings.status_halal,
            "weight": "aaa"
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_insert_menu_merchant, data=param,
                                 headers=settings.header_with_token_merchant, files=file)

        data = response.json()
        validate_status = data.get("success")
        validate_message = data.get("message")['weight']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "weight harus berupa angka." in validate_message

    def test_insert_menu_non_sayur_without_param_weight_string(self):
        param = {
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": settings.deskripsi,
            "nama_menu_makanan": settings.nama_makanan,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": settings.status_halal,
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_insert_menu_merchant, data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")['weight_string']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'weight string tidak boleh kosong kecuali Kategori menu ada dalam 5.' in validate_message

    def test_insert_menu_non_sayur_wight_empty_value(self):
        param = {
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": settings.deskripsi,
            "nama_menu_makanan": settings.nama_makanan,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": settings.status_halal,
            "weight_string": ''
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_insert_menu_merchant, data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")['weight_string']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert 'weight string tidak boleh kosong kecuali Kategori menu ada dalam 5.' in validate_message

    def test_insert_menu_non_sayur_weight_int_value(self):
        param = {
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": settings.deskripsi,
            "nama_menu_makanan": settings.nama_makanan,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": settings.status_halal,
            "weight_string": 200
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
            'images[2]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_insert_menu_merchant, data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")

        assert response.status_code == 201
        assert validate_status == bool(True)
