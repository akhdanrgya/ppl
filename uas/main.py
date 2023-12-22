from datetime import datetime

PIN_ADMIN = "123"
HARGA_PER_MENIT = 10000

data_parkir = []  # list yang nantinya akan di isi data dictionary


def hitung_harga_parkir(waktu_masuk, waktu_keluar, plat, jenis, waktu_parkir):
    try:
        selisih_waktu = waktu_keluar - waktu_masuk
        waktu_parkir_detik = selisih_waktu.total_seconds()
        # waktu_parkir_detik = 370

        # Pembulatan waktu parkir
        if waktu_parkir_detik <= 60:  # Parkir dibulatkan ke 60 detik
            harga_parkir = HARGA_PER_MENIT
        elif waktu_parkir_detik <= 120:
            # Parkir dibulatkan ke 120 detik lebih dari 1 menit
            harga_parkir = HARGA_PER_MENIT * 2
        elif waktu_parkir_detik <= 180:
            # Parkir dibulatkan ke 180 detik atau lebih dari sama dengan 3 menit
            harga_parkir = HARGA_PER_MENIT * 3
        elif waktu_parkir_detik <= 240:
            # Maksimal waktu parkir adalah 240 detik atau 4 menit
            harga_parkir = HARGA_PER_MENIT * 4
        elif waktu_parkir_detik > 240:
            harga_parkir = HARGA_PER_MENIT * 4

        # Perhitungan denda parkir
        denda = 0
        if waktu_parkir_detik > 240 and waktu_parkir_detik < 360:
            denda = harga_parkir * 0.1  # Denda 10% dari total biaya parkir
            harga_parkir += denda
        elif waktu_parkir_detik > 360:
            denda = harga_parkir * 0.25  # Denda 25% dari total biaya parkir
            harga_parkir += denda

        total = harga_parkir
        print(f"Total harga yang harus anda bayar : Rp.{total:,.0f}")

        bayar = 0
        while True:
            try:
                bayar = int(input("Masukkan nominal pembayaran: "))
                if bayar < total:
                    print("Uang anda kurang. Mohon masukkan nominal yang cukup.")
                else:
                    break
            except ValueError:
                print("Masukkan angka bulat positif.")

        total_harga = bayar - total
        print(
            f"Anda membayar Rp.{bayar:,.0f} dari total harga parkir Rp.{total:,.0f}, kembalian : Rp.{total_harga:,.0f}")

        print(f"""
              ========== PARKIR APP ==========
              Kendaraan     : {jenis}
              Plat          : {plat}
              Waktu Masuk   : {waktu_masuk.strftime("%Y-%m-%d %H:%M:%S")}
              Waktu Keluar  : {waktu_keluar.strftime("%Y-%m-%d %H:%M:%S")}
              Waktu Parkir  : {waktu_parkir}

              Harga         : Rp.{harga_parkir - denda:,.0f}
              Denda         : Rp.{denda:,.0f}
              Total         : Rp.{total:,.0f}

              Pembayaran    : Rp.{bayar:,.0f}
              Kembalian     : Rp.{total_harga:,.0f}
              """)
        return harga_parkir, denda
    except Exception as error:
        print(f"Terjadi kesalahan dalam menghitung harga parkir: {error}")


def menu_admin():
    try:
        pin_input = input("Masukkan PIN Admin: ")
        isauth = False

        if pin_input == PIN_ADMIN:
            isauth = True

        while True:
            if isauth:
                print("""
                    Menu Admin - Kelola Data Parkir
                    
                    1. Riwayat Data Parkir
                    2. Hapus Data Parkir
                    3. Kembali 
                    """)

                pilih = input("Pilih menu admin (1/2/3): ")

                if pilih == "1":
                    print(f"=" * 52, "Data Parkir", "=" * 52, "\n")
                    total = sum(item['harga_parkir'] for item in data_parkir)

                    for i, entry in enumerate(data_parkir):
                        waktu_masuk = entry['waktu_masuk']
                        waktu_keluar = entry['waktu_keluar']
                        waktu_parkir = entry['waktu_parkir']
                        jenis = entry['jenis_kendaraan']

                        print(f"""
                            ({i + 1})   
                            Jenis Kendaraan : {jenis}
                            Plat Kendaraan  : {entry['plat']}
                            Waktu Masuk     : {waktu_masuk}
                            Waktu Keluar    : {waktu_keluar}
                            Waktu Parkir    : {waktu_parkir}
                            
                            Harga Parkir    : {entry['harga_parkir']}
                            Denda Parkir    : {entry['denda']}
                              """)

                    print(f"\n Total Pemasukan: {total}")

                elif pilih == "2":
                    print("\nMenu Admin - Hapus Data Parkir")
                    plat_nomor_hapus = input(
                        "Masukkan plat nomor yang akan dihapus ( q untuk kembali ): ").upper()

                    if plat_nomor_hapus == 'q':
                        menu_admin()

                    for i, entry in enumerate(data_parkir):
                        if entry["plat"] == plat_nomor_hapus:
                            data_parkir.pop(i)  # hapus data list sesuai index
                            print(
                                f"Data parkir dengan plat {plat_nomor_hapus} berhasil dihapus.")
                            break
                    else:
                        print("Data parkir tidak ditemukan :(")

                elif pilih == "3":
                    break
            else:
                print("PIN salah. Akses ditolak!!")
                break
    except Exception as error:
        print(f"Terjadi kesalahan menu admin : {error}")


def main():
    try:
        print("Selamat datang di Aplikasi Parkir!")

        while True:
            print(f"""
                  ===== Parkir APP =====
                  
                  1. Masuk Kendaraan
                  2. Keluar Kendaraan
                  3. Admin
                  4. Keluar Aplikasi
                  """)

            pilihan_menu = input("Pilih menu (1/2/3/4): ")

            if pilihan_menu == "1":
                jenis = input("Masukan jenis kendaraan: ")
                plat_nomor = input("Masukkan plat nomor kendaraan: ").upper()
                waktu_masuk = datetime.now()
                print(
                    f"Kendaraan {jenis} dengan plat {plat_nomor} masuk pada {waktu_masuk.strftime('%Y-%m-%d %H:%M:%S')}.")
                print("==== Gerbang terbuka ====")
                print(f"Silahkan masuk plat {plat_nomor}")

                data_parkir.append({
                    "jenis_kendaraan": jenis,
                    "plat": plat_nomor,
                    "waktu_masuk": waktu_masuk,
                    "waktu_keluar": "Belum",
                    "waktu_parkir": "belum",
                    "harga_parkir": 0.0,
                    "denda": 0.0
                })  # Menambah data dictionary ke data list

            elif pilihan_menu == "2":
                waktu_keluar = datetime.now()
                plat_nomor = input("Masukkan plat nomor kendaraan: ").upper()
                for entry in data_parkir:

                    waktu_masuk = entry['waktu_masuk']

                    # Menghitung total waktu parkir
                    selisih_waktu = waktu_keluar - waktu_masuk
                    hours, remainder = divmod(selisih_waktu.seconds, 3600)
                    minutes, seconds = divmod(remainder, 60)

                    formatted_time = "{:02}:{:02}:{:02}".format(
                        int(hours), int(minutes), int(seconds))

                    if entry["plat"] == plat_nomor and entry["waktu_keluar"] == "Belum":
                        entry["waktu_keluar"] = waktu_keluar
                        entry["waktu_parkir"] = formatted_time

                        harga_parkir, denda = hitung_harga_parkir(
                            entry["waktu_masuk"],
                            entry["waktu_keluar"],
                            plat_nomor,
                            entry['jenis_kendaraan'],
                            entry['waktu_parkir']
                        )
                        entry["harga_parkir"] = harga_parkir
                        entry["denda"] = denda

                        print(
                            f"\nTotal harga parkir: {harga_parkir} (Termasuk denda {denda})")
                        break

                else:
                    print("Data parkir tidak ditemukan :(")
            elif pilihan_menu == "3":
                menu_admin()
            elif pilihan_menu == "4":
                print("Terima kasih telah menggunakan Aplikasi Parkir!")
                exit()
            else:
                print("Pilihan tidak tersedia :(")
    except Exception as error:
        print(f"Terjadi kesalahan fungsi main : {error}")


main()
