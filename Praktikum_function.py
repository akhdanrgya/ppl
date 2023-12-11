# fungsi tanpa argumen

# def salampagi():
#     print("halo")
#     print("Selamat Pagi!")

# salampagi()

# fungsi dengan argumen

# def salampagi(nama):
#     print('Halo')
#     print('Selamat pagi', nama)

# salampagi("adan")

# fungsi dengan lebih dari satu argumen

# def hitungBMI(berat, tinggi):
#     print("BMI : ", berat / (tinggi**2))

# hitungBMI(65, 1.65)

# fungsi dengan keyword


# def hitungBMI(berat, tinggi):
#     print("BMI : ", berat / (tinggi**2))

# hitungBMI(berat= 70, tinggi= 1.65)
# hitungBMI(tinggi= 1.65, berat= 70)

# fungsi dengan default value

# def salampagi(nama="Sobat pagi"):
#     print("Halo!")
#     print("Selamat Pagi", nama)

# salampagi("Cipeng")
# salampagi()

# fungsi dengan jumlah argumen yang tidak diatur

# def salampagi(*VarArgs):
#     print("Halo!")
#     print("Selamat Pagi", end = ' ')

#     for Arg in VarArgs:
#         print(Arg, end = ' ')

# salampagi("akhdan", "anargya", "arisadi")

# fungsi dengan return

# def hitungBMI(berat, tinggi):
#     return berat / (tinggi**2)

# print("BMI: ", hitungBMI(70, 1.65))

# fungsi dengan menggunakan variable

# angka = 4

# def menggunakanVariable():
#     angka = 17
#     print("Angka dalam fungsi = ", angka)

# menggunakanVariable()
# print("a = ", angka)

# menghitung faktorial

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# hasil = 5
# res = factorial(hasil)
# print(res)

# menghitung kubus

# def kubus(s):
#     luas = "Hasil luas: ", 6 * s**2
#     volume = "Hasil volume", s**3

#     return luas, volume

# sisi = int(input("sisi: "))

# print(kubus(sisi)) 