# Latihan Logika dan Komparasi: Membuat Gabungan Area Rentang dari Angka

# Contoh 1: x < 3 atau x > 10
print("=====Contoh 1=====")

# User input
inputUser = float(
    input("Masukkan angka yang bernilai kurang dari 3 atau lebih besar dari 10: ")
)

# Memeriksa angka (x) kurang dari 3 [komparasi]
isKurangDari = inputUser < 3
print("Kurang dari 3 =", isKurangDari)

# Memeriksa angka (x) lebih dari 10 [komparasi]
isLebihDari = inputUser > 10
print("Lebih dari 10 =", isLebihDari)

# Gabungan dengan OR [logika]
isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukkan:", isCorrect)

# Contoh 2: 3 < x < 10
print("=====Contoh 2=====")

# User input
inputUser = float(
    input("Masukkan angka yang bernilai lebih dari 3 dan kurang dari 10:")
)

# Memeriksa angka (x) lebih dari 3 [komparasi]
isLebihDari = inputUser > 3
print("Lebih dari 3 =", isLebihDari)

# Memeriksa angka (x) kurang dari 10 [komparasi]
isKurangDari = inputUser < 10
print("Kurang dari 10 =", isKurangDari)

# Gabungan dengan AND [logika]
isCorrect = isKurangDari and isLebihDari
print("Angka yang anda masukkan:", isCorrect)

# Contoh 3: 0 < x < 5 atau 8 < x < 11
print("=====Contoh 3=====")

# User input
inputUser = float(input("Masukkan angka yang bernilai 0-5 atau 8-11: "))

# Memeriksa angka (x) lebih dari 0 [komparasi]
isLebihDari0 = inputUser > 0
print("Lebih dari 0 =", isLebihDari0)

# Memeriksa angka (x) kurang dari 5 [komparasi]
isKurangDari5 = inputUser < 5
print("Kurang dari 5 =", isKurangDari5)

# Memeriksa angka (x) lebih dari 8 [komparasi]
isLebihDari8 = inputUser > 8
print("Lebih dari 8 =", isLebihDari8)

# Memeriksa angka (x) kurang dari 11 [komparasi]
isKurangDari11 = inputUser < 11
print("Lebih dari 11 =", isKurangDari11)

# Gabungan dengan OR [logika]
isCorrect = (isLebihDari0 and isKurangDari5) or (isLebihDari8 and isKurangDari11)
print("Angka yang anda masukkan:", isCorrect)

# Contoh 4: x < 0 atau 5 < x < 8 atau x > 11
print("=====Contoh 4=====")

# User input
inputUser = float(
    input("Masukkan angka yang bernilai kurang dari 0 atau 5-8 atau lebih dari 11: ")
)

# Memeriksa angka (x) kurang dari 0 [komparasi]
isKurangDari0 = inputUser < 0
print("Kurang dari 0 =", isKurangDari0)

# Memeriksa angka (x) lebih dari 5 [komparasi]
isLebihDari5 = inputUser > 5
print("Lebih dari 5 =", isLebihDari5)

# Memeriksa angka (x) kurang dari 8 [komparasi]
isKurangDari8 = inputUser < 8
print("Kurang dari 8 =", isKurangDari8)

# Memeriksa angka (x) lebih dari 11 [komparasi]
isLebihDari11 = inputUser > 11
print("Lebih dari 11 =", isLebihDari11)

# Gabungan dengan OR [logika]
isCorrect = isKurangDari0 or (isLebihDari5 and isKurangDari8) or isLebihDari11
print("Angka yang anda masukkan:", isCorrect)
