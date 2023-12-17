from datetime import datetime, timedelta

data = []

while True:
    print("""
          1. masuk
          2. keluar
          3. view
          """)

    pilih = int(input("Pilih: "))

    if pilih == 1:
        masuk = datetime.now()
        data.append({"masuk": masuk, "keluar": None})
        print("masuk")

    elif pilih == 2:
        keluar = datetime.now()
        for entry in data:
            if entry["keluar"] is None:
                entry["keluar"] = keluar
                print("Keluar")
            else:
                print("Belum keluar")

    elif pilih == 3:
        for entry in data:
            masuk = entry['masuk']
            keluar = entry['keluar']
            selisih = keluar - masuk

            # Mendapatkan komponen jam, menit, dan detik dari timedelta
            hours, remainder = divmod(selisih.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            formatted_time = "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))
            
            print(f"masuk: {masuk}, keluar: {keluar}, selisih: {formatted_time}")

