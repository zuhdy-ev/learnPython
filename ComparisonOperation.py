print("===OPERASI KOMPARASI===")

# Setiap hasil dari operasi komparasi adalah "boolean"
# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

# Lebih dari (>)
print("🚀 Lebih dari (>):")
hasil = a > 3
print(a, ">", 3, "=", hasil)
hasil = b > 3
print(b, ">", 3, "=", hasil)
hasil = b > 2
print(b, ">", 2, "=", hasil)

# Kurang dari (<)
print("🚀 Kurang dari (<):")
hasil = a < 3
print(a, "<", 3, "=", hasil)
hasil = b < 3
print(b, "<", 3, "=", hasil)
hasil = b < 2
print(b, "<", 2, "=", hasil)

# Lebih dari sama dengan (>=)
print("🚀 Lebih dari sama dengan (>=):")
hasil = a >= 3
print(a, ">=", 3, "=", hasil)
hasil = b >= 3
print(b, ">=", 3, "=", hasil)
hasil = b >= 2
print(b, ">=", 2, "=", hasil)

# Kurang dari sama dengan (<=)
print("🚀 Kurang dari sama dengan (<=):")
hasil = a <= 3
print(a, "<=", 3, "=", hasil)
hasil = b <= 3
print(b, "<=", 3, "=", hasil)
hasil = b <= 2
print(b, "<=", 2, "=", hasil)

# Sama dengan (==).
# NOTE! Kalau tandanya cuman satu (=) itu artinya assignment, tapi kalau dua (==) itu artinya komparasi.
print("🚀 Sama dengan (==):")
hasil = a == 3
print(a, "==", 3, "=", hasil)
hasil = b == 3
print(b, "==", 3, "=", hasil)
hasil = b == 2
print(b, "==", 2, "=", hasil)

# Tidak sama dengan (!=)
print("🚀 Tidak sama dengan (!=):")
hasil = a != 3
print(a, "!=", 3, "=", hasil)
hasil = b != 3
print(b, "!=", 3, "=", hasil)
hasil = b != 2
print(b, "!=", 2, "=", hasil)

# 'is' dan 'is not' sebagai komparasi object identity. Jadi, 'is' itu untuk membandingkan apakah dua buah object itu sama atau tidak. Misal: a = 5, b = 5, a is b, maka hasilnya True. Adapun 'is not' itu kebalikannya. Misal: a = 5, b = 5, a is not b, maka hasilnya False.
# Cara mengetahui object identity: id(object) atau hex(id(object)).
print("🚀 'is' sebagai komparasi object identity:")
print("- Contoh 1:")
x = 5  # ini adalah assignment membuat object
y = 5
print("nilai x =", x, ", id =", hex(id(x)))
print("nilai y =", y, ", id =", hex(id(y)))
hasil = x is y
print("x is y =", hasil)

print("- Contoh 2:")
x = 5  # ini adalah assignment membuat object
y = 8
print("nilai x =", x, ", id =", hex(id(x)))
print("nilai y =", y, ", id =", hex(id(y)))
hasil = x is y
print("x is y =", hasil)

print("🚀 'is not' sebagai komparasi object identity:")
print("- Contoh 1:")
x = 5  # ini adalah assignment membuat object
y = 5
print("nilai x =", x, ", id =", hex(id(x)))
print("nilai y =", y, ", id =", hex(id(y)))
hasil = x is not y
print("x is not y =", hasil)

print("- Contoh 2:")
x = 5  # ini adalah assignment membuat object
y = 8
print("nilai x =", x, ", id =", hex(id(x)))
print("nilai y =", y, ", id =", hex(id(y)))
hasil = x is not y
print("x is not y =", hasil)
