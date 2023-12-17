
data = []

def utama():
    try:
        while True:
            print("""
                  1. Add
                  2. Remove
                  3. View
                  """)
            
            pilih = int(input("Pilih menu: "))

            if pilih == 1:
                angka = input("Angka: ")
                huruf = input("Huruf: ")

                data.append({"angka": angka, "huruf": huruf})
                
                if not angka and not huruf:
                    print("Tolong masukan angka dan huruf")
                
            elif pilih == 2:
                print("Remove")
            elif pilih == 3:
                
                print("Data:")
                
                for list in data:
                    print(f"Angka: {list['angka']} Huruf: {list['huruf']}")
            else:
                print("Pilih lagi")
                
    except Exception as err:
        print(f"Error utama function: {err}")
        
utama()