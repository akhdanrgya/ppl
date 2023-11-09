# 102042300077
# Akhdan Anargya Arisadi

menu_0077 = {
    "Nasi Goreng": 25000,
    "Mie Goreng": 20000,
    "Ayam Goreng": 30000,
    "Sate Ayam": 35000,
    "Nasi Rendang": 40000,
    "Es Teh Manis": 5000,
    "Es Jeruk": 7000,
    "Es Campur": 10000,
    "Es Cincau": 8000,
    "Es Kelapa Muda": 12000
}


total_harga_0077 = 0


print("Selamat datang di restoran")
kategori_0077 = input("Apakah anda mau pesan sesuatu? ")

if kategori_0077 == 'iya' or kategori_0077 == "ya" or kategori_0077 == "y":
    print("Daftar Menu Makanan:")
    print("""
          
            ==========================
                    Makanan
          
          1. Nasi Goreng        Rp.25000
          2. Mie Goreng         Rp.20000
          3. Ayam Goreng        Rp.30000
          4. Sate Ayam          Rp.35000
          5. Nasi Rendang       Rp.40000
          
            ===========================
                    Minuman
                    
          1. Es Teh Manis       Rp.25000
          2. Es Jeruk           Rp.20000
          3. Es Campur          Rp.30000
          4. Es Cincau          Rp.35000
          5. Es Kelapa Muda     Rp.40000
          """)
    menu_0077 = menu_0077
else:
    print("Pilihan tidak valid")
    exit()


pesanan_0077 = {}
while True:
    item_0077 = input("Pilih menu (q untuk selesai): ")
    if item_0077 == 'q':
        break
    if item_0077 in menu_0077:
        qty_0077 = int(input("Jumlah: "))
        harga_0077 = menu_0077[item_0077]
        subtotal_0077 = harga_0077 * qty_0077
        total_harga_0077 += subtotal_0077
        pesanan_0077[item_0077] = {'Jumlah': qty_0077, 'Harga': harga_0077, 'Subtotal': subtotal_0077}
    else:
        print("Menu tidak valid")


print("\nPesanan Anda:")
for item_0077, detail in pesanan_0077.items():
    print(f"{item_0077} x {detail['Jumlah']} = {detail['Subtotal']}")
print(f"total yang harus anda bayar: {total_harga_0077}")


diskon_0077 = 0
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
print(f"Total Harga: Rp. {total_harga_0077}")
print(f"Diskon: {int(diskon_0077 * 100)}%")
print(f"Total Akhir: Rp. {total_akhir_0077}")
print(f"Nominal Pembayaran: Rp. {nominal_pembayaran_0077}")
print(f"Kembalian: Rp. {kembalian_0077}")

print("Terima kasih telah makan di restoran !")

