from datetime import datetime

data_parkir = {}  # pake dictionary buat menyimpan informasi parkir
PIN = "111"

while True:
    print("1. msk")
    print("2. kluar")
    print("3. admin")

    pilih = int(input("plh : "))
    if pilih == 1:
        plat = input("plt : ")
        if plat in data_parkir:
            print("msk lg?")
        else:
            waktu_masuk = datetime.now()
            data_parkir[plat] = {"masuk": waktu_masuk, "keluar": None}
            print("dah masuk", plat, "dengan waktu", waktu_masuk)

    elif pilih == 2:
        plat_keluar = input("plt : ")
        if plat_keluar in data_parkir:
            waktu_keluar = datetime.now()
            data_parkir[plat_keluar]["keluar"] = waktu_keluar
            waktu_total = waktu_keluar - data_parkir[plat_keluar]["masuk"]
            print("keluar dgn plat : ", plat_keluar, "dgn waktu selama", waktu_total)
        else:
            print("ga ada")

    elif pilih == 3:
        pin_admin = input("masukkan pin : ")
        if pin_admin == PIN:
            for plat, info in data_parkir.items():
                waktu_masuk = info["masuk"]
                waktu_keluar = info["keluar"]
                print("Plat:", plat, "Waktu Masuk:", waktu_masuk, "Waktu Keluar:", waktu_keluar)
        else:
            print("slh pin")

    else:
        print("byebye")
        break
