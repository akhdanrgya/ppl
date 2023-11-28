from datetime import datetime

data = []

while True:
    print("""
          Selamat datang di parkir anjay
          1. Masuk
          2. Keluar
          3. Admin
          """)

    pilih = input("Pilih mana bang? ")

    if pilih == "1":
        plat = input("Masukan plat anda: ")
        waktu_masuk = datetime.now()
        data.append(
            {"plat": plat, "waktu masuk": waktu_masuk}
        )
    elif pilih == "2":
        keluar = input("Masukan plat anda: ")
        waktu_keluar = datetime.now()
    elif pilih == "3":
        print(data)
