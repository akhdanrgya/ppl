#Nim : 102042300045
#Nama : Aabid Ahmad Zubaid
# Daftar makanan dan harganya
menu_makanan_0045 = {
    "BAKSO MIE SPESIAL": 25000,
    "BAKMI PANGSIT": 20000,
    "SATE AYAM PADANG": 15000,
    "Nasi Goreng": 15000,
    "Mie Goreng": 1000,
}

# Daftar minuman dan harganya
menu_minuman_0045 = {
    "Blue Sea Soda": 20000,
    "Cappucina Latte": 15000,
    "Ice Grape Soda": 20000,
    "Sparkling Breeze Soda": 15000,
    "Milk Shake": 10000,
}

# Inisialisasi variabel Nama dan Harga
nama_0045 = ""
harga_0045 = 0

# Customer memilih kategori
print (""" 
       ==----------------------==
       SELAMAT DATANG DI RESTAURANT PAKCIK & MAKCIK! 
       1. Makanan
       2. Minuman
       ==----------------------==
 """)
pilih_0045 = int(input("Masukkkan Pilihan"))

if pilih_0045 == 1 :
    print("""
          -------------------------------------
          SILAHKAN PILIH MENU HIDANGAN MAKANAN NYA TUAN
          1. BAKSO MIE SPESIAL       Rp.25000
          2. BAKMI PANGSIT           Rp.20000
          3. SATE AYAM PADANG        Rp.15000
          4. SOTO AYAM               Rp.15000
          5. KWETIUAW AYAM           Rp.10000
          -------------------------------------
          """)
    pilihmenu_0045 = int(input("Masukkan Pilihan :"))
    if pilihmenu_0045 == 1:
        nama_0045 += "BAKSO MIE SPESIAL"
        harga_0045 += 25000
    elif pilihmenu_0045 == 2:
        nama_0045 += "BAKMI PANGSIT"
        harga_0045 += 20000
    elif pilihmenu_0045 == 3:
        nama_0045 += "SATE AYAM PADANG"
        harga_0045 += 150000
    elif pilihmenu_0045 == 4:
        nama_0045 += "SOTO AYAMM"
        harga_0045 += 150000
    elif pilihmenu_0045 == 5:
        nama_0045 += "KWETIAUW AYAM"
        harga_0045 += 10000
    else :
        print("Maaf Tidak Ada Lagi Pilihan Menu")
        exit()

elif pilih_0045 == 2 :
      harga_0045 = 0
      nama_0045 = ''
      print("""
            -------------------------------------
            SILAHKAN PILIH MENU HIDANGAN MINUMAN NYA TUAN! 
            1. Blue Sea Soda           Rp.20000
            2. Cappucina Latte         Rp.15000
            3. Ice Grape Soda          Rp.20000
            4. Sparkling Breeze Soda   Rp.15000
            5. Milk Shake              Rp.10000
            -------------------------------------
            """)
      pilihmenu_0045 = int(input("Masukkan Pilihan :"))
      if pilihmenu_0045 == 1:
            nama_0045 += "Blue Sea Soda"
            harga_0045 += 20000
      elif pilihmenu_0045 == 2:
            nama_0045 += "Cappucino Latte"
            harga_0045 += 15000
      elif pilihmenu_0045 == 3:
            nama_0045 += "Ice Grape Soda"
            harga_0045 += 20000
      elif pilihmenu_0045 == 4:
            nama_0045 += "Sparkling Breeze Soda"
            harga_0045 += 15000
      elif pilihmenu_0045 == 5:
            nama_0045 += "Milk Shake"
            harga_0045 += 10000
      else :
            print("Maaf Tuan Tidak Ada Lagi Pilihan Menu")

else :
      print ("Maaf Pembayaran Anda Gagal!")
      exit()

# Customer memasukkan jumlah banyaknya item yang dipilih
jumlah_0045 = int(input(f"Masukkan jumlah {nama_0045} yang akan dibeli: "))

# Tampilkan hasil pesanan
print(f"Anda telah memesan {nama_0045} sebanyak {jumlah_0045} dengan total harga Rp. {harga_0045 * jumlah_0045}")

# Hitung total harga
total_harga_0045 = harga_0045 * jumlah_0045

# Hitung diskon jika berlaku
diskon_0045 = 0
if total_harga_0045 > 500000:
    diskon_0045 = 0.25 * total_harga_0045
elif total_harga_0045 > 250000:
    diskon_0045 = 0.15 * total_harga_0045
elif total_harga_0045 > 100000:
    diskon_0045 = 0.10 * total_harga_0045

# Hitung total akhir yang harus dibayar
total_akhir_0045 = total_harga_0045 - diskon_0045



# Masukkan NIM dan Nama saat proses pembayaran
nim_0045 = input("Masukkan NIM: ")
nama_pelanggan_0045 = input("Masukkan Nama: ")

# Masukkan nominal pembayaran
nominal_pembayaran_0045 = float(input("Masukkan nominal pembayaran: "))

# Hitung kembalian
kembalian_0045 = nominal_pembayaran_0045 - total_akhir_0045

# Tampilkan total akhir dan kembalian
print(f"Total Harga: Rp. {total_harga_0045}")
print(f"Anda Mendapat Diskon sebesar: Rp. {diskon_0045}")
print(f"Total Akhir: Rp. {total_akhir_0045}")
print(f"Kembalian: Rp. {kembalian_0045}")