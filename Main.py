print("Yuu gaskaann!")

print("Tab 1 di atas tidak akan error, karena tab 1 dianggap sebagai string")
print(
    "Di Python juga tidak perlu tanda ; di akhir baris, karena Python akan menganggap bahwa setiap baris adalah statement"
)

# ini comment
""" ini juga comment """

print(
    "Python itu bahasa pemrograman yang interpreted. Jadi, tidak perlu compile. Cukup run aja. Tapi kelemahannya adalah lebih lambat dari bahasa pemrograman yang compiled."
)

print(
    "cara menjadikan source code Python menjadi byte code (file yang executable) adalah dengan menggunakan pyinstaller. Caranya: python -m py_compile Main.py"
)

print(
    "File Python yang sudah di-compile akan lebih cepat dijalankan daripada file Python yang belum di-compile, ini akan sangat terasa ketika program yang dibuat sudah sangat panjang dan kompleks. Tapi, file Python yang sudah di-compile tidak bisa diedit lagi."
)

# --- VARIABLE ---
# Variable adalah tempat menyimpan data

# Contoh menaruh atau menng-assigment nilai ke dalam variable
a = 10
x = 5
p = 20
panjang = 1000

# Pemanggilan pertama
print("Nilai a = ", a)
print("Nilai x = ", x)
print("Nilai panjang = ", panjang)

# Penamaan
nilai_y = 15  # dengan menggunakan underscore
juta10 = 10000000  # ini boleh
nilaiZ = 17.5  # ini boleh

# Pemanggilan kedua
print("Nilai a = ", a)
a = 7
print("Nilai a = ", a)

# Assignment indirect
b = a
print("Nilai b = ", b)

# --- DATA TYPE ---

# Tipe data umum
# Tipe data angka satuan yang tidak ada komanya = integer
data_integer = 1
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

# Tipe data angka dengan koma = float
data_float = 1.5
print("data : ", data_float)
print("- bertipe : ", type(data_float))

# Tipe data kumpulan karakter = string
data_string = "ucup"
print("data : ", data_string)
print("- bertipe : ", type(data_string))

# Tipe data biner true/false = boolean
data_bool = True
print("data : ", data_bool)
print("- bertipe : ", type(data_bool))

# Tipe data khusus
# Contoh 1: bilangan kompleks
data_complex = complex(5, 6)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

# Tipe data dari bahasa C
# Contoh: import tipe data c_double yang ada di bahasa C melalui ctypes
from ctypes import c_double

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))
