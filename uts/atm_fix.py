# 102042300077
# Akhdan Anargya Arisadi

nim_0077 = int(input("Masukan nim anda: "))
nama_0077 = input("Masukan nama anda: ")
norek_0077 = input("Masukan nomor rekening anda: ")
inp_pin_0077 = int(input("Masukan pin anda (6 digit pin): "))

pin_0077 = 102042
saldo_0077 = 2000

if inp_pin_0077 == pin_0077:
    print("""
           Menu ATM
           1. Cek Saldo
           2. Setor Tunai
           3. Tarik Tunai
           4. Exit
           """)
    pilih_menu_0077 = int(input("Pilih menu (1-4) : "))

    if pilih_menu_0077 == 1:
        print(f"""
              Nama          : {nama_0077}
              NIM           : {nim_0077}
              No Rekening   : {norek_0077}
              Saldo         : {saldo_0077}
              """)
    elif pilih_menu_0077 == 2:
        print(f"""
              Nama          : {nama_0077}
              NIM           : {nim_0077}
              No Rekening   : {norek_0077}
              Saldo         : {saldo_0077}
              """)

        setor_tunai_0077 = int(
            input("Masukan jumlah yang ingin anda setor : "))

        saldo_0077 = saldo_0077 + setor_tunai_0077

        print(f"""
              === Setor Tunai Berhasil ==
              Nama          : {nama_0077}
              NIM           : {nim_0077}
              No Rekening   : {norek_0077}
              Saldo         : {saldo_0077}
              """)

    elif pilih_menu_0077 == 3:

        print(f"""
              Nama          : {nama_0077}
              NIM           : {nim_0077}
              No Rekening   : {norek_0077}
              Saldo         : {saldo_0077}
              """)
        tarik_tunai_0077 = int(
            input("Masukan jumlah yang ingin anda tarik : "))

        if saldo_0077 >= tarik_tunai_0077:
            saldo_0077 = saldo_0077 - tarik_tunai_0077
            print(f"""
              === Tarik Tunai Berhasil ==
              Nama          : {nama_0077}
              NIM           : {nim_0077}
              No Rekening   : {norek_0077}
              Saldo         : {saldo_0077}
              """)

        else:
            print("Maaf saldo anda tidak cukup")
    elif pilih_menu_0077 == 4:
        print("Terimakasih dan sampai jumpa")
        exit()
    else:
        print("Maaf pilihan tidak tersedia")

else:
    print("Maaf pin anda salah")
