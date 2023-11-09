# 102042300077
# Akhdan Anargya Arisadi


# data dictionary mahasiswa yang nantinya akan di gunakan key nya untuk mendapankan value dari masing masing key
data_mahasiswa_0077 = {
    "102042300077": {
        "nama": "Akhdan Anargya",
        "no_rekening": "102042300077",
        "pin": "123456",
        "saldo": 100000000.0
    },
    "102042300075": {
        "nama": "Enrico",
        "no_rekening": "102042300075",
        "pin": "112233",
        "saldo": 400000.0
    }
}


# fungsi login untuk memvalidasi atau authentifikasi apakah nim dan pin yang di masukan sesuai dengan data
def login():
    nim_0077 = input("Masukkan NIM: ")
    pin_0077 = input("Masukkan PIN (6 digit dari NIM): ")

    if nim_0077 in data_mahasiswa_0077 and data_mahasiswa_0077[nim_0077]["pin"] == pin_0077:
        return nim_0077
    else:
        print("PIN yang dimasukkan salah.")
        return None

# fungsi cek saldo untuk mengecek saldo yang ada di dalam data


def cek_saldo(nim_0077):
    mahasiswa_0077 = data_mahasiswa_0077[nim_0077]
    print("NIM:", nim_0077)
    print("Nama:", mahasiswa_0077["nama"])
    print("No. Rekening:", mahasiswa_0077["no_rekening"])
    print("Saldo:", mahasiswa_0077["saldo"])

# fungsi tarik uang untuk menarik atau menguraing jumlah uang yang ada di dalam data


def tarik_uang(nim_0077):
    mahasiswa_0077 = data_mahasiswa_0077[nim_0077]
    print("NIM:", nim_0077)
    print("Nama:", mahasiswa_0077["nama"])
    print("No. Rekening:", mahasiswa_0077["no_rekening"])
    saldo_0077 = mahasiswa_0077["saldo"]
    nominal_0077 = float(input("Masukkan nominal yang akan ditarik: "))

    if nominal_0077 <= saldo_0077:
        mahasiswa_0077["saldo"] -= nominal_0077
        print("Penarikan sukses. Saldo tersisa:", mahasiswa_0077["saldo"])
    else:
        print("Saldo tidak mencukupi.")

# fungsi setor uang untuk menambah uang yang ada di dalam data


def setor_uang(nim_0077):
    mahasiswa_0077 = data_mahasiswa_0077[nim_0077]
    print("NIM:", nim_0077)
    print("Nama:", mahasiswa_0077["nama"])
    print("No. Rekening:", mahasiswa_0077["no_rekening"])
    saldo_0077 = mahasiswa_0077["saldo"]
    nominal_0077 = float(input("Masukkan nominal yang akan anda setorkan: "))

    if nominal_0077 <= saldo_0077:
        mahasiswa_0077["saldo"] += nominal_0077
        print("Setor uang sukses. Saldo anda:", mahasiswa_0077["saldo"])
    else:
        print("Setor uang gagal.")


# ini adalah looping menggunakan while true untuk menjalankan fungsi fungsi yang sudah saya buat di atas
while True:
    print("\nMenu Utama:")
    print("1. Login")
    print("2. Keluar")
    choice_0077 = input("Pilih menu: ")

    if choice_0077 == "1":
        nim_0077 = login()
        if nim_0077:
            while True:
                print("\nMenu Utama:")
                print("1. Cek Saldo")
                print("2. Tarik Uang")
                print("3. Setor Uang")
                print("4. Keluar")
                menu_choice_0077 = input("Pilih menu: ")

                if menu_choice_0077 == "1":
                    cek_saldo(nim_0077)
                elif menu_choice_0077 == "2":
                    tarik_uang(nim_0077)
                elif menu_choice_0077 == "3":
                    setor_uang(nim_0077)
                elif menu_choice_0077 == "4":
                    break
                else:
                    print("Menu tidak valid.")
    elif choice_0077 == "2":
        print("Terima kasih. Sampai jumpa!")
        break
    else:
        print("Menu tidak valid.")
