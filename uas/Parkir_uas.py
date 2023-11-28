from datetime import datetime

PIN_ADMIN = "123"
HARGA_PER_MENIT = 10000
DETTIK_BULAT_ATAS = 30

data_parkir = []


def hitung_harga_parkir(waktu_masuk, waktu_keluar, plat):
    try:
        selisih_waktu = waktu_keluar - waktu_masuk
        harga_parkir = round(
            selisih_waktu.total_seconds() / 60) * HARGA_PER_MENIT

        if selisih_waktu.total_seconds() > 240:
            denda = harga_parkir * 0.1
            harga_parkir += denda
        elif selisih_waktu.total_seconds() > 360:
            denda = harga_parkir * 0.25
            harga_parkir += denda
        else:
            denda = 0
            harga_parkir = HARGA_PER_MENIT

        total = harga_parkir + denda
        print(f"Total harga yang harus anda bayar : {total}")

        bayar = int(input("Masukan nominal pembayaran: "))

        if bayar >= harga_parkir:
            total_harga = bayar - total
            print(
                f"Anda membayar {bayar} dari total harga parkir {total}, kembalian : {total_harga}")

        else:
            print("Maaf uang anda kurang")

        print(f"""
              ==== Struk Pembayaran ====
              Plat          : {plat}
              Waktu Masuk   : {waktu_masuk}
              Waktu Keluar  : {waktu_keluar}


              Harga         : {total}
              Pembayaran    : {bayar}
              Kembalian     : {total_harga}
              Denda         : {denda}
              """)
        return harga_parkir, denda
    except Exception as error:
        print(f"Terjadi kesalahan dalam menghitung harga parkir: {error}")


def menu_admin():
    try:
        pin_input = input("Masukkan PIN Admin: ")

        if pin_input == PIN_ADMIN:
            print("Menu Admin - Kelola Data Parkir")
            print("Data Parkir:")
            for entry in data_parkir:
                print(
                    f"Plat: {entry['plat']}, Waktu Masuk: {entry['waktu_masuk']}, Waktu Keluar: {entry['waktu_keluar']}")

            print("\nMenu Admin - Hapus Data Parkir")
            plat_nomor_hapus = input(
                "Masukkan plat nomor yang akan dihapus ( q untuk kembali ): ")

            if plat_nomor_hapus == 'q':
                main()

            for i, entry in enumerate(data_parkir):
                if entry["plat"] == plat_nomor_hapus:
                    data_parkir.pop(i)
                    print(
                        f"Data parkir dengan plat {plat_nomor_hapus} berhasil dihapus.")
                    break
            else:
                print("Data parkir tidak ditemukan.")
        else:
            print("PIN salah. Akses ditolak.")
    except Exception as error:
        print(f"Terjadi kesalahan : {error}")


def main():
    try:
        print("Selamat datang di Aplikasi Parkir!")

        while True:
            print("""
                  ===== Parkir APP =====
                  
                  1. Masuk Kendaraan
                  2. Keluar Kendaraan
                  3. Admin
                  4. Keluar Aplikasi
                  """)

            pilihan_menu = input("Pilih menu (1/2/3/4): ")

            if pilihan_menu == "1":
                plat_nomor = input("Masukkan plat nomor kendaraan: ")
                waktu_masuk = datetime.now()
                print(
                    f"Kendaraan dengan plat {plat_nomor} masuk pada {waktu_masuk}.")

                data_parkir.append(
                    {"plat": plat_nomor, "waktu_masuk": waktu_masuk, "waktu_keluar": None})
            elif pilihan_menu == "2":
                plat_nomor = input("Masukkan plat nomor kendaraan: ")
                waktu_keluar = datetime.now()
                print(
                    f"Kendaraan dengan plat {plat_nomor} keluar pada {waktu_keluar}.")

                for entry in data_parkir:
                    if entry["plat"] == plat_nomor and entry["waktu_keluar"] is None:
                        entry["waktu_keluar"] = waktu_keluar

                        harga_parkir, denda = hitung_harga_parkir(
                            entry["waktu_masuk"], entry["waktu_keluar"], plat_nomor)
                        entry["harga_parkir"] = harga_parkir
                        entry["denda"] = denda

                        print(
                            f"\nTotal harga parkir: {harga_parkir} (Termasuk denda {denda})")
                        break
                else:
                    print("Data parkir tidak ditemukan.")
            elif pilihan_menu == "3":
                menu_admin()
            elif pilihan_menu == "4":
                print("Terima kasih telah menggunakan Aplikasi Parkir!")
                exit()
            else:
                print("Pilihan tidak tersedia :(")
    except Exception as error:
        print(f"Terjadi error : {error}")


main()
