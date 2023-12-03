from datetime import datetime
from termcolor import colored

PIN_ADMIN = "123"
HARGA_PER_MENIT = 10000

data_parkir = []  # list yang nantinya akan di isi data dictionary


def hitung_harga_parkir(waktu_masuk, waktu_keluar, plat):
    try:
        selisih_waktu = waktu_keluar - waktu_masuk
        waktu_parkir_detik = selisih_waktu.total_seconds()

        # Pembulatan waktu parkir
        if waktu_parkir_detik < 60:
            harga_parkir = HARGA_PER_MENIT
        elif waktu_parkir_detik <= 75:
            harga_parkir = HARGA_PER_MENIT * 2  # Parkir dibulatkan ke 120 detik
        elif waktu_parkir_detik <= 240:
            harga_parkir = HARGA_PER_MENIT * 4  # Maksimal waktu parkir adalah 240 detik
        elif waktu_parkir_detik > 240:
            harga_parkir = HARGA_PER_MENIT * 4

        # Perhitungan denda parkir
        denda = 0
        if waktu_parkir_detik > 240:
            denda = harga_parkir * 0.1  # Denda 10% dari total biaya parkir
            harga_parkir += denda
        elif waktu_parkir_detik > 360:
            denda = harga_parkir * 0.25  # Denda 25% dari total biaya parkir
            harga_parkir += denda

        total = harga_parkir + denda
        print(colored(f"Total harga yang harus anda bayar : Rp.{total:,.0f}", 'green'))

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
        print(colored(f"Anda membayar Rp.{bayar:,.0f} dari total harga parkir Rp.{total:,.0f}, kembalian : Rp.{total_harga:,.0f}", 'yellow'))

        print(colored(f"""
              ========== PARKIR APP ==========
              Plat          : {plat}
              Waktu Masuk   : {waktu_masuk.strftime("%Y-%m-%d %H:%M:%S")}
              Waktu Keluar  : {waktu_keluar.strftime("%Y-%m-%d %H:%M:%S")}

              Harga         : Rp.{harga_parkir - denda:,.0f}
              Denda         : Rp.{denda:,.0f}
              Total         : Rp.{total:,.0f}

              Pembayaran    : Rp.{bayar:,.0f}
              Kembalian     : Rp.{total_harga:,.0f}
              """, 'cyan'))
        return harga_parkir, denda
    except Exception as error:
        print(colored(f"Terjadi kesalahan dalam menghitung harga parkir: {error}", 'red'))


def menu_admin():
    try:
        pin_input = input("Masukkan PIN Admin: ")

        if pin_input == PIN_ADMIN:
            print(colored("Menu Admin - Kelola Data Parkir", 'blue'))
            print("Data Parkir:")
            for entry in data_parkir:
                print(
                    f"Plat: {entry['plat']}, Waktu Masuk: {entry['waktu_masuk']}, Waktu Keluar: {entry['waktu_keluar']}")

            print(colored("\nMenu Admin - Hapus Data Parkir", 'blue'))
            plat_nomor_hapus = input(
                "Masukkan plat nomor yang akan dihapus ( q untuk kembali ): ")

            if plat_nomor_hapus == 'q':
                main()

            for i, entry in enumerate(data_parkir):
                if entry["plat"] == plat_nomor_hapus:
                    data_parkir.pop(i)  # hapus data list sesuai index
                    print(
                        colored(f"Data parkir dengan plat {plat_nomor_hapus} berhasil dihapus.", 'green'))
                    break
            else:
                print(colored("Data parkir tidak ditemukan :(", 'red'))
        else:
            print(colored("PIN salah. Akses ditolak!!", 'red'))
    except Exception as error:
        print(colored(f"Terjadi kesalahan menu admin : {error}", 'red'))


def main():
    try:
        print(colored("Selamat datang di Aplikasi Parkir!", 'green'))

        while True:
            print(colored(f"""
                  ===== Parkir APP =====
                  
                  1. Masuk Kendaraan
                  2. Keluar Kendaraan
                  3. Admin
                  4. Keluar Aplikasi
                  """, 'cyan'))

            pilihan_menu = input("Pilih menu (1/2/3/4): ")

            if pilihan_menu == "1":
                plat_nomor = input("Masukkan plat nomor kendaraan: ")
                waktu_masuk = datetime.now()
                print(
                    colored(f"Kendaraan dengan plat {plat_nomor} masuk pada {waktu_masuk.strftime('%Y-%m-%d %H:%M:%S')}.", 'green'))
                print(colored("Silahkan masuk :)", 'green'))

                data_parkir.append(
                    {"plat": plat_nomor, "waktu_masuk": waktu_masuk, "waktu_keluar": "Belum"})  # Menambah data dictionary ke data list

            elif pilihan_menu == "2":
                waktu_keluar = datetime.now()
                plat_nomor = input("Masukkan plat nomor kendaraan: ")
                for entry in data_parkir:
                    if entry["plat"] == plat_nomor and entry["waktu_keluar"] == "Belum":
                        entry["waktu_keluar"] = waktu_keluar

                        harga_parkir, denda = hitung_harga_parkir(
                            entry["waktu_masuk"], entry["waktu_keluar"], plat_nomor)
                        entry["harga_parkir"] = harga_parkir
                        entry["denda"] = denda

                        print(
                            colored(f"\nTotal harga parkir: {harga_parkir} (Termasuk denda {denda})", 'cyan'))
                        break
                else:
                    print(colored("Data parkir tidak ditemukan :(", 'red'))
            elif pilihan_menu == "3":
                menu_admin()
            elif pilihan_menu == "4":
                print(colored("Terima kasih telah menggunakan Aplikasi Parkir!", 'green'))
                exit()
            else:
                print(colored("Pilihan tidak tersedia :(", 'red'))
    except Exception as error:
        print(colored(f"Terjadi kesalahan fungsi main : {error}", 'red'))


main()
