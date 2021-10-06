import sys
import requests
import settings
from assertpy import assert_that

sys.path.append('.../IntegrationTest')


class TestUpdateMerchantMenu:

    def test_update_menu_kat_sayur_normal(self):
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
        }
        response = requests.post(settings.url_update_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + '?_method=PUT', data=param,
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

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert f"Data menu {settings.nama_makanan} berhasil diperbarui." in validate_message
        assert_that(validate_weight).is_equal_to(settings.weight)
        assert_that(validate_harga_jual).is_equal_to(settings.harga_jual)
        assert_that(validate_harga_asli).is_equal_to(settings.harga_asli)
        assert_that(validate_deskripsi).is_equal_to(settings.deskripsi)
        assert_that(validate_kategori).is_equal_to(settings.merchant_kategori_sayur)
        assert_that(validate_nama).is_equal_to(settings.nama_makanan)
        assert_that(validate_data).contains('id', 'merchant_id', 'nama_menu_makanan', 'merchant_kategori_makanan_id',
                                            'is_exclusive', 'deskripsi', 'waktu_mulai_penjemputan',
                                            'waktu_akhir_penjemputan', 'harga_asli', 'harga_jual', 'stock',
                                            'is_non_halal', 'total_terjual', 'is_missed', 'is_active', 'weight',
                                            'weight_string', 'waktu_missed', 'image_thumbnail', 'created_at',
                                            'updated_at', 'is_tomorrow', 'image', 'menu_images')

    def test_update_menu_kat_non_sayur_normal(self):
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
        }
        response = requests.post(settings.url_update_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + '?_method=PUT', data=param,
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
        validate_weight_sting = data.get("data")['weight_string']

        assert response.status_code == 200
        assert validate_status == bool(True)
        assert f"Data menu {settings.nama_makanan} berhasil diperbarui." in validate_message
        assert_that(validate_weight_sting).is_equal_to(settings.weight_string)
        assert_that(validate_harga_jual).is_equal_to(settings.harga_jual)
        assert_that(validate_harga_asli).is_equal_to(settings.harga_asli)
        assert_that(validate_deskripsi).is_equal_to(settings.deskripsi)
        assert_that(validate_kategori).is_equal_to(settings.merchant_kategori_non_sayur)
        assert_that(validate_nama).is_equal_to(settings.nama_makanan)
        assert_that(validate_data).contains('id', 'merchant_id', 'nama_menu_makanan', 'merchant_kategori_makanan_id',
                                            'is_exclusive', 'deskripsi', 'waktu_mulai_penjemputan',
                                            'waktu_akhir_penjemputan', 'harga_asli', 'harga_jual', 'stock',
                                            'is_non_halal', 'total_terjual', 'is_missed', 'is_active', 'weight',
                                            'weight_string', 'waktu_missed', 'image_thumbnail', 'created_at',
                                            'updated_at', 'is_tomorrow', 'image', 'menu_images')

    def test_update_menu_wrong_token(self):
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
        }
        response = requests.post(settings.url_update_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + '?_method=PUT', data=param,
                                 headers=settings.header_wrong_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message

    def test_update_menu_token_empty(self):
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
        }
        response = requests.post(settings.url_update_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + '?_method=PUT', data=param,
                                 headers=settings.header_without_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 401
        assert validate_status == bool(False)
        assert "Unauthorized" in validate_message

    def test_update_menu_nama_makanan_empty(self):
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
        }
        response = requests.post(settings.url_update_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + '?_method=PUT', data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")["nama_menu_makanan"]

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Nama menu tidak boleh kosong." in validate_message

    def test_update_menu_without_param_nama_menu_makanan(self):
        param = {
            # "nama_menu_makanan": settings.nama_makanan,
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
        }
        response = requests.post(settings.url_update_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + '?_method=PUT', data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")["nama_menu_makanan"]

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Nama menu tidak boleh kosong." in validate_message

    def test_update_menu_kategori_makanan_id_wrong_value(self):
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
        }
        response = requests.post(settings.url_update_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + '?_method=PUT', data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")

        assert response.status_code == 404
        assert validate_status == bool(False)
        assert "Data gagal dibuat." in validate_message

    def test_update_menu_kategori_makanan_id_empty(self):
        param = {
            "nama_menu_makanan": settings.nama_makanan,
            "merchant_kategori_makanan_id": '',
            "deskripsi": settings.deskripsi,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": "0",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_update_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + '?_method=PUT', data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")["merchant_kategori_makanan_id"]

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Kategori menu tidak boleh kosong." in validate_message

    def test_update_menu_without_param_kategori_makanan_id(self):
        param = {
            "nama_menu_makanan": settings.nama_makanan,
            # "merchant_kategori_makanan_id": '',
            "deskripsi": settings.deskripsi,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": "0",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_update_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + '?_method=PUT', data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")["merchant_kategori_makanan_id"]

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Kategori menu tidak boleh kosong." in validate_message

    def test_update_menu_deskripsi_empty(self):
        param = {
            "nama_menu_makanan": settings.nama_makanan,
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": '',
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": "0",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_update_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + '?_method=PUT', data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")["deskripsi"]

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "deskripsi tidak boleh kosong." in validate_message

    def test_update_menu_without_param_deskripsi(self):
        param = {
            "nama_menu_makanan": settings.nama_makanan,
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            # "deskripsi": '',
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": "0",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_update_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + '?_method=PUT', data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")["deskripsi"]

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "deskripsi tidak boleh kosong." in validate_message

    def test_update_menu_harga_asli_empty(self):
        param = {
            "nama_menu_makanan": settings.nama_makanan,
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": settings.deskripsi,
            "harga_asli": '',
            "harga_jual": settings.harga_jual,
            "is_non_halal": "0",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_update_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + '?_method=PUT', data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")["harga_asli"]

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Harga asli tidak boleh kosong." in validate_message

    def test_update_menu_without_param_harga_asli(self):
        param = {
            "nama_menu_makanan": settings.nama_makanan,
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": settings.deskripsi,
            # "harga_asli": '',
            "harga_jual": settings.harga_jual,
            "is_non_halal": "0",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_update_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + '?_method=PUT', data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")["harga_asli"]

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Harga asli tidak boleh kosong." in validate_message

    def test_update_menu_harga_asli_string_value(self):
        param = {
            "nama_menu_makanan": settings.nama_makanan,
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": settings.deskripsi,
            "harga_asli": 'aaa',
            "harga_jual": settings.harga_jual,
            "is_non_halal": "0",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_update_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + '?_method=PUT', data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")["harga_asli"]

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "format harga asli yang diinputkan salah" in validate_message

    def test_update_menu_harga_jual_empty(self):
        param = {
            "nama_menu_makanan": settings.nama_makanan,
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": settings.deskripsi,
            "harga_asli": settings.harga_asli,
            "harga_jual": '',
            "is_non_halal": "0",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_update_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + '?_method=PUT', data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")["harga_jual"]

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Harga jual tidak boleh kosong." in validate_message

    def test_update_menu_without_param_harga_jual(self):
        param = {
            "nama_menu_makanan": settings.nama_makanan,
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": settings.deskripsi,
            "harga_asli": settings.harga_asli,
            # "harga_jual": '',
            "is_non_halal": "0",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_update_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + '?_method=PUT', data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")["harga_jual"]

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Harga jual tidak boleh kosong." in validate_message

    def test_update_menu_harga_jual_string_value(self):
        param = {
            "nama_menu_makanan": settings.nama_makanan,
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": settings.deskripsi,
            "harga_asli": settings.harga_asli,
            "harga_jual": 'aaa',
            "is_non_halal": "0",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_update_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + '?_method=PUT', data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")["harga_jual"]

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "format harga jual yang diinputkan salah" in validate_message

    def test_update_menu_is_non_halal_empty(self):
        param = {
            "nama_menu_makanan": settings.nama_makanan,
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": settings.deskripsi,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": "",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_update_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + '?_method=PUT', data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")["is_non_halal"]

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Menu tidak halal tidak boleh kosong." in validate_message

    def test_update_menu_without_param_is_non_halal(self):
        param = {
            "nama_menu_makanan": settings.nama_makanan,
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": settings.deskripsi,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            # "is_non_halal": "",
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_update_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + '?_method=PUT', data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")["is_non_halal"]

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Menu tidak halal tidak boleh kosong." in validate_message

    def test_update_menu_is_non_halal_wrong_value(self):
        param = {
            "nama_menu_makanan": settings.nama_makanan,
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": settings.deskripsi,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": 'aaaa',
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_update_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + '?_method=PUT', data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")["is_non_halal"]

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "Menu tidak halal harus bernilai true atau false." in validate_message

    def test_update_menu_sayur_without_param_weight(self):
        param = {
            "nama_menu_makanan": settings.nama_makanan,
            "merchant_kategori_makanan_id": settings.merchant_kategori_sayur,
            "deskripsi": settings.deskripsi,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": settings.status_halal,
            "weight_string": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_update_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + '?_method=PUT', data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")['weight']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "weight tidak boleh kosong ketika Kategori menu adalah 5." in validate_message

    def test_update_menu_sayur_weight_string_value(self):
        param = {
            "nama_menu_makanan": settings.nama_makanan,
            "merchant_kategori_makanan_id": settings.merchant_kategori_sayur,
            "deskripsi": settings.deskripsi,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": settings.status_halal,
            "weight": settings.weight_string
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_update_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + '?_method=PUT', data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")['weight']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "weight harus berupa angka." in validate_message

    def test_update_menu_sayur_wight_empty_value(self):
        param = {
            "nama_menu_makanan": settings.nama_makanan,
            "merchant_kategori_makanan_id": settings.merchant_kategori_sayur,
            "deskripsi": settings.deskripsi,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": settings.status_halal,
            "weight": ''
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_update_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + '?_method=PUT', data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")['weight']

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "weight tidak boleh kosong ketika Kategori menu adalah 5." in validate_message

    def test_update_menu_non_sayur_without_param_weight_string(self):
        param = {
            "nama_menu_makanan": settings.nama_makanan,
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": settings.deskripsi,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": settings.status_halal,
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_update_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + '?_method=PUT', data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")["weight_string"]

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "weight string tidak boleh kosong kecuali Kategori menu ada dalam 5." in validate_message

    def test_update_menu_non_sayur_weight_string_number_value(self):
        param = {
            "nama_menu_makanan": settings.nama_makanan,
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": settings.deskripsi,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": settings.status_halal,
            "weight_string" : 200
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_update_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + '?_method=PUT', data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")

        assert response.status_code == 200
        assert validate_status == bool(True)

    def test_update_menu_non_sayur_wight_string_empty_value(self):
        param = {
            "nama_menu_makanan": settings.nama_makanan,
            "merchant_kategori_makanan_id": settings.merchant_kategori_non_sayur,
            "deskripsi": settings.deskripsi,
            "harga_asli": settings.harga_asli,
            "harga_jual": settings.harga_jual,
            "is_non_halal": settings.status_halal,
            "weight_string" : ''
        }
        file = {
            'images[0]': open("img/mie.jpg", 'rb'),
            'images[1]': open("img/mie.jpg", 'rb'),
        }
        response = requests.post(settings.url_update_menu_merchant + str(
            settings.var_list_menu_merchant().json().get('data')[0]['id']) + '?_method=PUT', data=param,
                                 headers=settings.header_with_token_merchant, files=file)
        data = response.json()

        validate_status = data.get("success")
        validate_message = data.get("message")["weight_string"]

        assert response.status_code == 422
        assert validate_status == bool(False)
        assert "weight string tidak boleh kosong kecuali Kategori menu ada dalam 5." in validate_message
