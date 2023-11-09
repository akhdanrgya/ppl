# tipe data

nama = "Akhdan Anargya"
print(nama)
print(type(nama))

umur = 19
print(umur)
print(type(umur))

bb = 55.6
print(bb)
print(type(bb))

tinggi = False
print(tinggi)
print(type(tinggi))



#Aritmatika

num1 = 5
num2 = 8

hasilPenjumlahan = num1 + num2
print("hasil penjumlahan : ", hasilPenjumlahan)

hasilPengurangan = num1 - num2
print("hasil pengurangan :", hasilPengurangan)

hasilPembagian = num1/num2
print(f"hasil pembagian adalah {hasilPembagian}")

hasilPembagianBulat = num1//num2
print(f"hasil pembagian adalah {hasilPembagianBulat}")

hasilKuadrat = num1**num2
print(f"hasil kuadrat adalah : {hasilKuadrat}")

hasilModulus = num1%num2
print(f"hasil modulus adalah : {hasilModulus}")

print("=" * 3, "Tolong masukan biodata anda", "=" *3, "\n" )
nama = input("nama :")
umur = int(input("umur :"))
jenisKelamin = input("Jenis Kelamin :")
tinggiBadan = float(input("Tinggi Badan :"))
noHP = int(input("masukan No NIM :"))

print("=" * 3, "Hasil Biodata", "=" *3,  "\n")
print(f"nama: {nama}")
print(f"umur: {umur}")
print(f"Jenis Kelamin: {jenisKelamin}")
print(f"Tinggi Badan: {tinggiBadan}")
print(f"No. HP: {tinggiBadan}")


print("=" * 3, "Tipe Biodata", "=" *3, "\n" )
print(type(nama))
print(type(umur))
print(type(jenisKelamin))
print(type(tinggiBadan))
print(type(noHP))

