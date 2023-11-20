#SITI AZ ZAHRA ALIFIA RIYADI
#102042300050

print("Selamat Datang Di ATM BECA!")
print("============================")

nim_0050         = int(input("Masukan NIM anda : "))
nama_0050        = input("Masukan Nama Anda : ")
no_rekening_0050 = 102042300050
saldo_0050   = 50000000
pin_0050     = 300050

input_pin_0050 = int(input("Masukan pin anda : "))
if input_pin_0050 == pin_0050:
    print("""
      
         Selamat datang di ATM BECA
             1. Cek Saldo
             2. Tarik Uang
             3. Setor Uang
             4. Keluar
      
      """)
    menu_0050 = int(input("Silahkan Pilih Menu : "))
    if menu_0050 == 1:
        print("NIM : ", nim_0050)
        print("Nama : ", nama_0050)
        print("No rekening anda : ", no_rekening_0050)
        print("Saldo Anda : ", saldo_0050)
    
    elif menu_0050 == 2:
        tarik_0050 = int(input("Masukan Nominal : "))
        print("NIM : ", nim_0050)
        print("Nama : ", nama_0050)
        print("No rekening anda : ", no_rekening_0050)
        print("Saldo atm anda : ", saldo_0050 - tarik_0050)
    
    elif menu_0050 == 3:
        setor_0050 = int(input("Masukan Nominal Setor : "))
        print("NIM : ", nim_0050)
        print("Nama : ", nama_0050)
        print("No rekening anda : ", no_rekening_0050)
        print("Saldo atm anda : ", saldo_0050 + setor_0050)
    else:
        print("Menu tidak tersedia")
        
else:
    print("PIN YANG ANDA MASUKAN SALAH")
