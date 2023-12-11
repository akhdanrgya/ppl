from datetime import datetime

HARGA = 10000
ACCOUNT = [
    {
        "username": "admin1",
        "password" :"123"
    },
    {
        "username": "admin2",
        "password" :"456"
    }
]
data = [] #data list yang nanti bakal di isi dengan data dictionary

def pembayaran(waktu_keluar, waktu_masuk, plat):
    selisih_waktu = waktu_keluar - waktu_masuk
    waktu_detik = 380
    
    denda = 0
    total_harga = 0
    
    if waktu_detik <= 60: # 1 menit
        total_harga = HARGA
        
    elif waktu_detik > 60 and waktu_detik <= 120: # lebih dari 1 menit kurang dari 2 menit
        total_harga = HARGA * 2
    
    elif waktu_detik > 120 and waktu_detik <= 180 : # lebih dari 2 menit kurang dari 3 menit
        total_harga = HARGA * 3
    
    elif waktu_detik > 180 and waktu_detik <= 240 : # lebih dari 3 menit
        total_harga = HARGA * 4
        
    elif waktu_detik > 240 and waktu_detik <= 360 :
        denda = 0.1
        total_harga = HARGA * 4
        hitung_denda = total_harga * denda

        total_harga = total_harga + hitung_denda

    elif waktu_detik > 360:
        denda = 0.25
        total_harga = HARGA * 4
        hitung_denda = total_harga * denda
        
        total_harga = total_harga + hitung_denda
    

    


def total(platNo, total):
    for list in data:
        if platNo == list["plat"] and list["harga"] == None:
            list["harga"] = total
            
            for i, list in enumerate(data):
                    # print(f"No {i + 1} Plat kendaraan {list['plat']} waktu masuk {list['waktu_masuk']} waktu keluar {list['waktu_keluar']} harga {list['harga']}")
                return(list["harga"])


def menu_admin():
    username = input("Masukan username: ")
    password = input("Masukan password: ")

    for acc in ACCOUNT:
        if username == acc["username"] and password == acc["password"]:
            print("""
                  1. Histori Parkir
                  2. Total Pemasukan
                  3. Exit
                  """)
            
            pilih = input("Pilih bwang: ")

            if pilih == "1":
                print(total())



def utama():
    while True:
        print("""
              1. Masuk kendaraan
              2. Keluar Kendaraan
              3. Admin
              """)
        
        pilih = input("pilih mana bwang: ")

        if pilih == "1":
            waktu_masuk = datetime.now()
            plat = input("Masukan plat nomor: ")
            data.append({"plat": plat ,"waktu_masuk": waktu_masuk, "waktu_keluar": "belum", "harga": None})
            
            print("silahkan masuk")

        elif pilih == "2":
            if not data:
                print("data kosong")
            else:
                plat_keluar = input("Masukan plat nomor: ")
                waktu_keluar = datetime.now()
                
                for list in data:
                    if plat_keluar == list["plat"] and list["waktu_keluar"] == "belum" and list["harga"] == None:
                        list["waktu_keluar"] = waktu_keluar
                        print(f"Plat kendaraan {list['plat']} waktu masuk {list['waktu_masuk']} waktu keluar {list['waktu_keluar']}")

                        pembayaran(list["waktu_keluar"], list["waktu_masuk"], plat_keluar)
                        
                    else:
                        print("plat nomor tidak di temukan")
        
        elif pilih == "3":
            menu_admin()


utama()