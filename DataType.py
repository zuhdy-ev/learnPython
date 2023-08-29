print("===DATA TYPE===")

# --- Tipe data umum ---
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

# --- Tipe data khusus ---
# Contoh 1: bilangan kompleks
data_complex = complex(5, 6)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

# --- Tipe data dari bahasa C ---
# Contoh: import tipe data c_double yang ada di bahasa C melalui ctypes
from ctypes import c_double

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))
