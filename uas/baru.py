from datetime import datetime

HARGA = 10000
data = []  # data list yang nanti bakal di isi dengan data dictionary
PIN = "123"


def pembayaran(waktu_keluar, waktu_masuk, plat):
    selisih_waktu = waktu_keluar - waktu_masuk
    waktu_detik = selisih_waktu.total_seconds()

    denda = 0
    total_harga = 0

    if waktu_detik <= 60:  # 1 menit
        total_harga = HARGA

    elif waktu_detik > 60 and waktu_detik <= 120:  # lebih dari 1 menit kurang dari 2 menit
        total_harga = HARGA * 2

    elif waktu_detik > 120 and waktu_detik <= 180:  # lebih dari 2 menit kurang dari 3 menit
        total_harga = HARGA * 3

    elif waktu_detik > 180 and waktu_detik <= 240:  # lebih dari 3 menit
        total_harga = HARGA * 4

    elif waktu_detik > 240 and waktu_detik <= 360:
        denda = 0.1
        total_harga = HARGA * 4
        hitung_denda = total_harga * denda

        total_harga = total_harga + hitung_denda

    elif waktu_detik > 360:
        denda = 0.25
        total_harga = HARGA * 4
        hitung_denda = total_harga * denda

        total_harga = total_harga + hitung_denda

    print("harga parkir adalah ", total_harga)

    for list in data:
        if plat == list['plat']:
            list['harga'] = total_harga


def admin():
    total = 0.0
    pin = input("Masukan pin: ")

    if pin == PIN:
        print("""
            1. Lihat data
            2. Hapus data
            3. Exit
            """)

        pilih = input("Pilih mana bwang: ")

        if pilih == "1":
            for list in data:
                print(
                    f"plat {list['plat']} waktu masuk {list['waktu_masuk']} waktu keluar {list['waktu_keluar']} total harga {list['harga']}")
                total += list['harga']
            print(f'\nTotal pemasukan {total}')

        elif pilih == "2":
            hapus = input("Masukan plat yang ingin di hapus: ")

            for i, list in enumerate(data):
                if hapus == list["plat"]:
                    data.pop(i)

            print("data sudah berhasil di hapus")

        elif pilih == "3":
            utama()

    else:
        print("pin salah brooo")


def utama():
    while True:
        print("""
              1. Masuk kendaraan
              2. Keluar Kendaraan
              3. Admin
              4. Keluar Aplikasi
              """)

        pilih = input("pilih mana bwang: ")

        if pilih == "1":
            waktu_masuk = datetime.now()
            plat = input("Masukan plat nomor: ")
            data.append({"plat": plat, "waktu_masuk": waktu_masuk,
                        "waktu_keluar": "belum", "harga": None})

            print("silahkan masuk")

        elif pilih == "2":
            plat_keluar = input("Masukan plat nomor: ")
            waktu_keluar = datetime.now()

            if not data:
                print("data kosong")

            for list in data:
                if plat_keluar == list["plat"] and list["waktu_keluar"] == "belum":
                    list["waktu_keluar"] = waktu_keluar
                    pembayaran(list["waktu_keluar"],
                               list["waktu_masuk"], plat_keluar)

                    print(f"Plat nomor {plat_keluar} berhasil keluar")
            else:
                print("plat nomor tidak di temukan")

        elif pilih == "3":
            admin()

        elif pilih == "4":
            print("Terimakasih telah menggunakan aplikasi parkir")
            exit()


utama()
