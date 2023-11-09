# IF ELSE BERSARANG

print(""" 
       =============================
       Menu Konter HP
       1. Isi Pulsa
       2. Top-Up
       3. Bayar Tagihan
       =============================
       """)

pilih = int(input("Masukan Pilihan: "))

if pilih == 1:
    nama = ""
    harga = 0
    print("""
       =============================
       Menu Konter HP
       1. Telkom
       2. Eksel
       3. Teri
       =============================
             """)
    pilihProvider = int(input("Masukan Pilihan: "))
    if pilihProvider == 1:
        nama += "Telkoms"
        harga += 50000
    elif pilihProvider == 2:
        nama += "Eksel"
        harga += 35000
    elif pilihProvider == 3:
        nama += "Teri"
        harga += 25000
    else:
        print("Gak Ada Cuy")


elif pilih == 2:
    nama = ""
    harga = 0
    print("""
       =============================
       Menu Konter HP
       1. EpEp
       2. Roblox
       3. Cs
       =============================
             """)
    pilihTopUp = int(input("Masukan Pilihan: "))
    if pilihTopUp == 1:
        nama += "EpEp"
        harga += 52322
    elif pilihTopUp == 2:
        nama += "Roblox"
        harga += 39000
    elif pilihTopUp == 3:
        nama += "Cs"
        harga += 70000
    else:
        print("Gak Ada Cuy")
elif pilih == 3:
    nama = ""
    harga = 0
    print("""
       =============================
       Menu Konter HP
       1. Listrik
       2. BRI
       3. BCA
       =============================
             """)
    pilihTagihan = int(input("Masukan Pilihan: "))
    if pilihTagihan == 1:
        nama += "Listrik"
        harga += 102030
    elif pilihTagihan == 2:
        nama += "BRI"
        harga += 99223
    elif pilihTagihan == 3:
        nama += "BCA"
        harga += 99221
    else:
        print("Gak Ada Cuy")

transaksi = input("Apakah sudah sesuai? (y/n)")
if transaksi == "y" or transaksi == 'ya':
    print("Transaksi Berhasil")
    print(f"Nama Profider : {nama}")
    print(f"Harga : {harga}")
else:
    print('Transaksi Gagal')
