def main():
    print("""
    === Toko sedia berbagi  ===
    1. Makanan
    2. Minuman
    3. Exit
    """)

    pilihan_kategori = int(input("Masukkan Pilihan Kategori Anda: "))
    if pilihan_kategori == 1:
        print("""
        === Toko sedia berbagi  ===
        1. Nasi pecel          - Rp. 10000
        2. Nasi bakar          - Rp. 10000
        3. Nasi uduk           - Rp. 10000
        4. Nasi kuning         - Rp. 12000
        5. Nasi goreng         - Rp. 15000
        6. Exit
        """)

        pilihan_makanan = input("Masukkan Pilihan Paket Anda: ")
        harga_barang = 0

        if pilihan_makanan == "1":
            harga_barang = 10000
        elif pilihan_makanan == "2":
            harga_barang = 10000
        elif pilihan_makanan == "3":
            harga_barang = 10000
        elif pilihan_makanan == "4":
            harga_barang = 12000
        elif pilihan_makanan == "5":
            harga_barang = 15000
        else:
            print("Pilihan Paket Tidak Valid!")
            return

        jumlah_pembelian = int(input("Jumlah Pembelian: "))

        pesan_ulang = input("Ingin pesan lagi gak? (ya/tidak) ")
        if pesan_ulang == "ya":
            main()
        else:
            nimpembeli = input("Masukkan nama anda: ")
            email = input("Masukkan email: ")

            print("Masukkan Cara Pembayaran")
            print("1. OVO")
            print("2. Gopay")
            print("3. Dana")
            pilihan_pembayaran = int(input("Masukan pilihan: "))

            if pilihan_pembayaran == 1:
                print("anda memilih OVO")
                sandiovo = int(input("Masukkan Kode Sandi: "))
            elif pilihan_pembayaran == 2:
                print("anda memilih Gopay")
                sandigopay = int(input("Masukkan Kode Sandi: "))
            elif pilihan_pembayaran == 3:
                print("anda memilih Dana")
                sandidana = int(input("Masukkan Kode Sandi: "))
            else:
                print("Pilihan pembayaran tidak tersedia")

    elif pilihan_kategori == 2:
        print("""
        1. Air Putih           - Rp. 5000       
        2. Teh Manis           - Rp. 7000
        3. Kopi                - Rp. 5000
        4. Es Jeruk            - Rp. 8000
        5. Jahe                - Rp. 7000
        6. Exit
        """)

        pilihan_minuman = input("Masukkan Pilihan Paket Anda: ")
        harga_barang = 0

        if pilihan_minuman == "1":
            harga_barang = 5000
        elif pilihan_minuman == "2":
            harga_barang = 7000
        elif pilihan_minuman == "3":
            harga_barang = 5000
        elif pilihan_minuman == "4":
            harga_barang = 8000
        elif pilihan_minuman == "5":
            harga_barang = 7000
        else:
            print("Pilihan Paket Tidak Valid!")
            return

        jumlah_pembelian = int(input("Jumlah Pembelian: "))

        pesan_ulang = input("Ingin pesan lagi gak? (ya/tidak) ")
        if pesan_ulang == "ya":
            main()
        else:
            nimpembeli = input("Masukkan nama anda: ")
            email = input("Masukkan email: ")

            print("Masukkan Cara Pembayaran")
            print("1. OVO")
            print("2. Gopay")
            print("3. Dana")
            pilihan_pembayaran = int(input("Masukan pilihan: "))

            if pilihan_pembayaran == 1:
                print("anda memilih OVO")
                sandiovo = int(input("Masukkan Kode Sandi: "))
            elif pilihan_pembayaran == 2:
                print("anda memilih Gopay")
                sandigopay = int(input("Masukkan Kode Sandi: "))
            elif pilihan_pembayaran == 3:
                print("anda memilih Dana")
                sandidana = int(input("Masukkan Kode Sandi: "))
            else:
                print("Pilihan pembayaran tidak tersedia")
                
    total_harga = harga_barang * jumlah_pembelian
    if total_harga >= 100000:
        diskon = total_harga * 0.1
        total_harga -= diskon
        print("Selamat Anda Mendapatkan Diskon 10%")
    elif total_harga >= 250000:
        diskon = total_harga * 0.15
        total_harga -= diskon
        print("Selamat Anda Mendapatkan Diskon 15%")
    elif total_harga >= 500000:
        diskon = total_harga * 0.25
        total_harga -= diskon
        print("Selamat Anda Mendapatkan Diskon 25%")

    print(f"""
    ===== Nota Pembelian =====
    Nama  : {nimpembeli}
    Email : {email}
    diskon : {diskon}
    Jumlah Pembelian : {jumlah_pembelian}
    Total Harga : {total_harga}
    """)
    print("Lunas")



if __name__ == "__main__":
    main()
