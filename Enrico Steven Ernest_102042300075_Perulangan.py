angka = 5
for i in range(0, angka):
    print(1)
    
for j in range(5):
    print(j)

nama = ["Tristan", "Cicak", "Nebin", "Alip", "Grace"]
for i in nama:
    print(i)

angka = 0
while(angka < 5):
    angka += 2
    print(angka)

while True:
    print("Menu")
    print("1. A")
    print("2, B")
    print("3, Exit")
    pilih = int(input("Masukan Angka Yang Ingin Dipilih"))
    
    if pilih == 1:
        print("A")
    elif pilih == 2:
        print("B")
    else:
        print("tidak ada pilihan")
        break
    

# while True:
#     print("""
#     ==========MENU NASI==========
#     1. Nasi pecel     - Rp. 10000
#     2. Nasi bakar     - Rp. 10000
#     3. Nasi uduk      - Rp. 10000
#     4. Keluar
#     =============================
#     """)
#     pilih = int(input("Masukan Pilihan : "))
#     if pilih == 1:
#         nama = "Nasi pecel"
#         harga = 10000
#     elif pilih == 2:
#         nama = "Nasi bakar"
#         harga = 10000
#     elif pilih == 3:
#         nama = "Nasi uduk"
#         harga = 10000        
#     else:
#         print("Pilihan Makanan Tidak Valid!")
#         break
#     jumlah_pesanan = int(input(f"Anda membeli {nama} ,masukan jumlah yang ingin dibeli: "))
#     harga_total = harga * jumlah_pesanan
#     print("Anda membeli", nama, "sebanyak", jumlah_pesanan, "dengan total harga: Rp.", harga_total)
#     harga_total = harga * jumlah_pesanan


#     nominal_pembayaran = int(input("Masukkan nominal pembayaran: "))
#     kembalian = nominal_pembayaran - harga_total
#     print("Total Harga: Rp. ", harga_total)
#     print("Kembalian: Rp. ", kembalian)
    