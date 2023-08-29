print("====CASTING====")

# Casting: merubah tipe data, dari suatu tipe data ke tipe data yang lain

print("====Casting 1: INTEGER====")
data_int = 9
print("data = ", data_int, ", type = ", type(data_int))

data_float = float(data_int)
print("data = ", data_float, ", type = ", type(data_float))
data_str = str(data_int)
print("data = ", data_str, ", type = ", type(data_str))
data_bool = bool(data_int)  # akan false jika nilai int = 0
print("data = ", data_bool, ", type = ", type(data_bool))

print("====Casting 2: FLOAT====")
data_float = 9.5
print("data = ", data_float, ", type = ", type(data_float))

data_int = int(data_float)  # akan dibulatkan ke bawah
print("data = ", data_int, ", type = ", type(data_int))
data_str = str(data_float)
print("data = ", data_str, ", type = ", type(data_str))
data_bool = bool(data_float)
print("data = ", data_bool, ", type = ", type(data_bool))

print("====Casting 3: BOOLEAN====")
data_bool = True
print("data = ", data_bool, ", type = ", type(data_bool))

data_int = int(data_bool)
print("data = ", data_int, ", type = ", type(data_int))
data_str = str(data_bool)
print("data = ", data_str, ", type = ", type(data_str))
data_float = float(data_bool)
print("data = ", data_float, ", type = ", type(data_float))

print("====Casting 4: STRING====")
data_str = "0"
print("data = ", data_str, ", type = ", type(data_str))

data_int = int(data_str) # string harus berupa angka dan/atau string tidak boleh kosong agar tidak error
print("data = ", data_int, ", type = ", type(data_int))
data_float = float(data_str) # string harus berupa angka dan/atau string tidak boleh kosong agar tidak error
print("data = ", data_float, ", type = ", type(data_float))
data_bool = bool(data_str) # bernilai false jika string kosong
print("data = ", data_bool, ", type = ", type(data_bool))
