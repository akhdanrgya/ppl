# 102042300077
# Akhdan Anargya Arisadi

# ini adalah daftar menu makanan yang di masukan ke dalam tipe data dictionary
menu_makanan_0077 = {
    "Nasi Goreng": 25000,
    "Mie Goreng": 20000,
    "Ayam Goreng": 30000,
    "Sate Ayam": 35000,
    "Nasi Rendang": 40000
}

# ini adalah daftar menu minuman yang di masukan ke dalam tipe data dictionary
menu_minuman_0077 = {
    "Es Teh Manis": 5000,
    "Es Jeruk": 7000,
    "Es Campur": 10000,
    "Es Cincau": 8000,
    "Es Kelapa Muda": 12000
}

# ini adalah fungsi untuk menampilkan menu dan di dalamnya ada beberapa kondisi menggunakan if else


def tampilkan_menu(kategori_0077):
    print(f"Daftar Menu {kategori_0077}:")
    menu_0077 = menu_makanan_0077 if kategori_0077 == "1" else menu_minuman_0077
    for i, (item_0077, harga_0077) in enumerate(menu_0077.items(), start=1):
        print(f"{i}. {item_0077}\tRp.{harga_0077}")


total_harga_0077 = 0
pesanan_0077 = {}

print("PROGRAM PEMBELIAN")
print("""
      Pilih Kategori
      1. Makanan
      2. Minuman
      """)
kategori_0077 = input("Masukan Pilihan (1 atau 2) : ")

if kategori_0077 not in ["1", "2"]:
    print("Kategori tidak valid.")
else:
    tampilkan_menu(kategori_0077)
# ini adalah input dan kalkulasi dari menu menggunakan metode looping while True yang akan berhenti ketika kita break
    while True:
        item_0077 = input("Pilih menu (q untuk selesai): ")
        if item_0077 == 'q':
            break
        menu_0077 = menu_makanan_0077 if kategori_0077 == "1" else menu_minuman_0077
        if item_0077.isdigit() and 1 <= int(item_0077) <= len(menu_0077):
            # untuk mengambil data dict berdasarkan index nya
            item_idx_0077 = int(item_0077) - 1
            item_name_0077 = list(menu_0077.keys())[
                item_idx_0077]  # mengambil data dict
            qty_0077 = int(input("Jumlah: "))
            harga_0077 = menu_0077[item_name_0077]
            subtotal_0077 = harga_0077 * qty_0077
            total_harga_0077 += subtotal_0077
            pesanan_0077[item_name_0077] = {
                'Jumlah': qty_0077, 'Harga': harga_0077, 'Subtotal': subtotal_0077}
        else:
            print("Menu tidak valid.")

    print("\nPesanan Anda:")
    for item_name_0077, detail in pesanan_0077.items():
        print(
            f"{item_name_0077} x {detail['Jumlah']} = Rp.{detail['Subtotal']}")
    print(f"Total Harga: Rp.{total_harga_0077}")

    diskon_0077 = 0  # variable diskon kosong yang nantinya akan di tambahkan di dalam validasi di bawah
    if total_harga_0077 > 500000:
        diskon_0077 = 0.25
    elif total_harga_0077 > 250000:
        diskon_0077 = 0.15
    elif total_harga_0077 > 100000:
        diskon_0077 = 0.10

    total_akhir_0077 = total_harga_0077 * (1 - diskon_0077)

    nim_0077 = input("Masukkan NIM: ")
    nama_0077 = input("Masukkan Nama: ")
    nominal_pembayaran_0077 = float(input("Masukkan nominal pembayaran: "))

    kembalian_0077 = nominal_pembayaran_0077 - total_akhir_0077

    print("\n--- Struk Pembayaran ---")
    print(f"NIM: {nim_0077}")
    print(f"Nama: {nama_0077}")
    print(f"Total Harga: Rp.{total_harga_0077}")
    print(f"Diskon: {int(diskon_0077 * 100)}%")
    print(f"Total Akhir: Rp.{total_akhir_0077}")
    print(f"Nominal Pembayaran: Rp.{nominal_pembayaran_0077}")
    print(f"Kembalian: Rp.{kembalian_0077}")

    print("Terima kasih telah melakukan pembelian!")
