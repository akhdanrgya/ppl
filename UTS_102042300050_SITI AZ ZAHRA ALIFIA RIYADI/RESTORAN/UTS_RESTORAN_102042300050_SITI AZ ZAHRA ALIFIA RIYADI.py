# NIM : 102042300050
# NIM : Siti Az Zahra Alifia Riyadi

print("""
        ***************************
      
        Welcome to Shusiseu Izakaya !   
        
        Mau pesan apa hari ini????
        1. Japanese food
        2. Japanese Drinks
      
        Have A Nice Day!
      
        ***************************
        


        """)

menu_0050 = input("Silahkan Pesan Menu Yang Kamu Suka: ")
harga_total_0050 = 0


if menu_0050 == '1':
    print("""
          Mau Japanese Food Apa? :
          1. Spicy Miso Kara Ramen       Rp. 45.000
          2. Gyoza Platter               Rp. 20.000
          3. Beef Curry                  Rp. 30.000
          4. Gyu Yaki Don                Rp. 35.000
          5. Chicken Katsun Don          Rp. 50.000
        
        """)
elif menu_0050 == '2':
    print("""
          Mau Pilih Japanese Drinks Apa :
          1. Royal Milk Tea             Rp. 30.000
          2. Greentea                   Rp. 35.000
          3. Aloe Drinks                Rp. 45.000
          4. Melon Soda                 Rp. 30.000
          5. Soy Milk                   Rp. 25.000
        
        """)
else:
   print("Sorry, Menu Tidak Tertera Silahkan Pilih Japanese Food or Drinks!.")

pilih_menu_0050 =input("Mau Pesan Apa: ")

total_pesan_0050 = int(input("Masukkan Jumlah: "))

nama_menu_0050 = ""

if menu_0050 == '1':
    if pilih_menu_0050 == '1':
        harga_0050 = 45000
        nama_menu_0050 = "Spicy Miso Kara Ramen"
    elif pilih_menu_0050 == '2':
        harga_0050 = 20000
        nama_menu_0050 = "Gyoza Platter"
    elif pilih_menu_0050 == '3':
        harga_0050 = 30000
        nama_menu_0050 = "Beef Curry"
    elif pilih_menu_0050 == '4':
        harga_0050 = 35000
        nama_menu_0050 = "Gyu Yaki Don"
    elif pilih_menu_0050 == '5':
        harga_0050 = 50000
        nama_menu_0050 = "Chicken Katsu Don"
    else:
        print("Japanese Food Yang Anda Pilih Tidak Tersedia. Silakan Pilih Menu Yang Tersedia :)")
        harga_0050 = 0

elif menu_0050 == '2':
    if pilih_menu_0050 == '1':
        harga_0050 = 30000
        nama_menu_0050 = "Royal Milk Tea"
    elif pilih_menu_0050 == '2':
        harga_0050 = 35000
        nama_menu_0050 = "Greentea"
    elif pilih_menu_0050 == '3':
        harga_0050 = 45000
        nama_menu_0050 = "Aloe Drinks"
    elif pilih_menu_0050 == '4':
        harga_0050 = 30000
        nama_menu_0050 = "Melon Soda"
    elif pilih_menu_0050 == '5':
        harga_0050 = 25000
        nama_menu_0050 = "Soy Milk"
    else:
        print("Japanese Drink Yang Anda Pilih Tidak Tersedia. Silakan Pilih Menu Yang Tersedia :)")
        harga_0050 = 0
else:
    harga_0050 = 0

if harga_0050 > 0:
    print("Anda telah memilih:")
    if menu_0050 == '1':
        print("Makanan", nama_menu_0050)
    else:
        print("Minuman", nama_menu_0050)
    
    print("Item: " + pilih_menu_0050)
    print("Jumlah: " + str(total_pesan_0050))
    print("Harga: Rp. " + str(harga_0050 * total_pesan_0050))

    harga_total_0050 = harga_0050 * total_pesan_0050

    if harga_total_0050 > 500000:
        disc_0050 = 0.25 
    elif harga_total_0050 >250000:
        disc_0050 = 0.15 
    elif harga_total_0050 >100000:
        disc_0050 = 0.10 
    else:
        disc_0050 = 0
    
    print("\n")
    print("=============================================")
    print("SHUSISEU'S IZAKAYA INVOICE")
    print("=============================================")
    total_harga_diskon_0050 = harga_total_0050 - \
        (harga_total_0050 * disc_0050)
    print("Total Harga Setelah Diskon: Rp. " +
          str(total_harga_diskon_0050))
    
    nim_0050 = input("Masukkan NIM: ")
    nama_0050 = input("Masukkan Nama: ")


    pembayaran_0050 = int(input("Masukkan nominal pembayaran: "))
   

    kembalian_0050 = pembayaran_0050 - total_harga_diskon_0050
    if kembalian_0050 > pembayaran_0050:
        print("Maaf uang anda kurang untuk melakukan proses pembayaran")
    else:
        print("Kembalian: Rp. " + str(kembalian_0050))
        print("=============================================")
        print("THANK YOU FOR VISIT US <3")
        print("=============================================")
else:
    exit()