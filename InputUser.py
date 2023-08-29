print("===INPUT USER===")

# Note: input() akan menganggap semua data yang diinput adalah string

# Membuat variable dan membuat form input
nama = input("Masukkan nama: ")
# Print nama
print("nama = ", nama, ", type = ", type(nama))

# Jika ingin mengambil data yang bertipe selain string, maka perlu dilakukan casting
# Contoh:
umur = int(input("Masukkan umur: "))
print("umur = ", umur, ", type = ", type(umur))

# Casting data lain, khususnya untuk boolean. Untuk boolean, jika inputan tidak kosong, maka akan selalu bernilai True. Jika kosong, maka akan bernilai False. Nah, bagaimana jika kita ingin mengisi nilai True/False dengan data biner (0/1)? Maka, kita perlu mengubahnya menjadi integer terlebih dahulu, baru kemudian diubah menjadi boolean.
# Contoh:
biner = bool(int(input("Apakah Anda suka Indomie? 0 untuk Tidak atau 1 untuk Iya): ")))
print("Suka mie?", biner, ", type = ", type(biner))
