# 102042300077
# Akhdan Anargya Arisadi

print("PROGRAM PEMBELIAN")
print("1. Makanan")
print("2. Minuman")

kategori_0077 = input("Pilih kategori (1/2): ")

total_harga_0077 = 0

if kategori_0077 == '1':
    print("Sub Menu Makanan:")
    print("1. Nasi Goreng - Rp. 25,000")
    print("2. Mie Ayam - Rp. 20,000")
    print("3. Sate Ayam - Rp. 30,000")
    print("4. Ayam Bakar - Rp. 35,000")
    print("5. Rendang - Rp. 40,000")

elif kategori_0077 == '2':
    print("Sub Menu Minuman:")
    print("1. Teh Manis - Rp. 5,000")
    print("2. Kopi - Rp. 10,000")
    print("3. Jus Jeruk - Rp. 15,000")
    print("4. Es Teh Tawar - Rp. 5,000")
    print("5. Es Cendol - Rp. 20,000")
else:
    print("Kategori tidak valid. Silakan pilih 1 atau 2.")


item_0077 = input("Pilih item (1-5): ")

jumlah_0077 = int(input("Masukkan jumlah: "))

if kategori_0077 == '1':
    if item_0077 == '1':
        harga_0077 = 25000
    elif item_0077 == '2':
        harga_0077 = 20000
    elif item_0077 == '3':
        harga_0077 = 30000
    elif item_0077 == '4':
        harga_0077 = 35000
    elif item_0077 == '5':
        harga_0077 = 40000
    else:
        print("Item tidak valid. Silakan pilih 1-5.")
        harga_0077 = 0
elif kategori_0077 == '2':
    if item_0077 == '1':
        harga_0077 = 5000
    elif item_0077 == '2':
        harga_0077 = 10000
    elif item_0077 == '3':
        harga_0077 = 15000
    elif item_0077 == '4':
        harga_0077 = 5000
    elif item_0077 == '5':
        harga_0077 = 20000
    else:
        print("Item tidak valid. Silakan pilih 1-5.")
        harga_0077 = 0
else:
    harga_0077 = 0


if harga_0077 > 0:
    print("Anda telah memilih:")
    if kategori_0077 == '1':
        print("Makanan")
    else:
        print("Minuman")
    print("Item: " + item_0077)
    print("Jumlah: " + str(jumlah_0077))
    print("Harga: Rp. " + str(harga_0077 * jumlah_0077))

    total_harga_0077 = harga_0077 * jumlah_0077

    if total_harga_0077 > 500000:
        diskon_0077 = 0.25
    elif total_harga_0077 > 250000:
        diskon_0077 = 0.15
    elif total_harga_0077 > 100000:
        diskon_0077 = 0.10
    else:
        diskon_0077 = 0

    total_harga_setelah_diskon_0077 = total_harga_0077 - \
        (total_harga_0077 * diskon_0077)
    print("Total Harga Setelah Diskon: Rp. " +
          str(total_harga_setelah_diskon_0077))

    nim_0077 = input("Masukkan NIM: ")
    nama_0077 = input("Masukkan Nama: ")

    pembayaran_0077 = int(input("Masukkan nominal pembayaran: "))

    kembalian_0077 = pembayaran_0077 - total_harga_setelah_diskon_0077
    print("Kembalian: Rp. " + str(kembalian_0077))
else:
    print("Terjadi kesalahan dalam pemilihan item.")
