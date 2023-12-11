data = []

while True:
    print("""
          1. add
          2. view
          """)
    
    pilih = input("Pilih bwang: ")

    if pilih == "1":
        angka = float(input("Masukan angka: "))
        data.append({"angka": angka})
    
    if pilih == "2":
        total = sum(item['angka'] for item in data)
        
        for item in data:
            print(f"Data: {item['angka']}")
            
        print(f"\nTotal: {total}")
