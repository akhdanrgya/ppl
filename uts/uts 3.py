nama_0069 = input("masukkan nama anda kak : ")
nim_0069 = int(input("masukkan nim anda : "))
nomor_rekening_0069 = 102042330069
saldo_0069 = 100000
pin_0069 = 102042


pin_input_0069 = int(input("masukkan pin anda(6 digit) :"))
if pin_input_0069 == pin_0069:
    print("nama : ", nama_0069)
    print("nim anda :", nim_0069)
    print("nomor rekening anda : ", nomor_rekening_0069)
    print("""
            ======================
            1. cek saldo kekayaan
            2. tarik kekayaan
            3. setor kekayaan
            4. cancel
            ======================
    """)

    pilih_cek_saldo_0069 = int(input("mau ngapain kak? "))
    if pilih_cek_saldo_0069 == 1:
        print("Nama : ", nama_0069)
        print("NIM : ", nim_0069)
        print("rekening anda : ", nomor_rekening_0069)
        print("kekayaan anda : ", saldo_0069)

    if pilih_cek_saldo_0069 == 2:
        print("mau ambil berapa kak dari", saldo_0069)
        tarik_kekayaan_0069 = int(
            input("Jumlah kekayaan yang ingin ditarik : "))
        if tarik_kekayaan_0069 <= saldo_0069:
            saldo_0069 -= tarik_kekayaan_0069
            print("Nama : ", nama_0069)
            print("NIM : ", nim_0069)
            print("rekening anda : ", nomor_rekening_0069)
            print("Sisa kekayaan anda:", saldo_0069)
        else:
            print(" ===Saldo anda tidak mencukupi kak huhu=== ")

    if pilih_cek_saldo_0069 == "3":
        print("mau setor kekayaan berapa kak ? ")
        setor_kekayaan_0069 = int(
            input("Jumlah kekayaan yang ingin disetor : "))
        saldo_0069 += setor_kekayaan_0069
        print("Anda telah menyetor kekayaan sebesar", setor_kekayaan_0069)
        print("Nama : ", nama_0069)
        print("NIM : ", nim_0069)
        print("rekening anda : ", nomor_rekening_0069)
        print("Saldo kekayaan sekarang : ", saldo_0069)
    else:
        print("Maaf tidak tersedia")
else:
    print("pin salah")
