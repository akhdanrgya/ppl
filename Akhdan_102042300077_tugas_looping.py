while True:
    print("""
    🍚 ==========MENU NASI==========
    1. Nasi Goreng     - Rp. 10000
    2. Nasi Udang      - Rp. 10000
    3. Nasi Kambing    - Rp. 10000
    4. Keluar
    =============================
    """)
    pilih = int(input("Masukan Pilihan: "))
    
    menu_dict = {
        1: {"nama": "Nasi pecel", "harga": 10000},
        2: {"nama": "Nasi bakar", "harga": 10000},
        3: {"nama": "Nasi uduk", "harga": 10000}
    }
    
    if pilih in menu_dict:
        pesanan = menu_dict[pilih]
        jumlah_pesanan = int(input("Masukkan jumlah pesanan yang ingin dibeli: "))
        
        harga_total = pesanan["harga"] * jumlah_pesanan
        
        print("🍛 Kamu membeli", pesanan["nama"], "sebanyak", jumlah_pesanan,
              "dengan total harga: Rp.", harga_total)
              
        nominal_pembayaran = int(input("Masukkan nominal pembayaran: "))
        kembalian = nominal_pembayaran - harga_total
        
        print("Total Harga: Rp. ", harga_total)
        print("Kembalian: Rp. ", kembalian)
        
        print("Makasih ya! 😊")
    elif pilih == 4:
        print("Terima Kasih, yaa!")
        break
    else:
        print("Pilihan Tidak Valid, bro. Coba lagi ya!")

