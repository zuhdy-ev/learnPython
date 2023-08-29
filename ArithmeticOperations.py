print("===ARITHMETIC OPERAIONS")

a = 10
b = 3

# Penjumlahan (+)
hasil = a + b
print(a, "+", b, "=", hasil)

# Pengurangan (-)
hasil = a - b
print(a, "-", b, "=", hasil)

# Perkalian (*)
hasil = a * b
print(a, "*", b, "=", hasil)

# Pembagian (/)
hasil = a / b
print(a, "/", b, "=", hasil)

# Pembagian dengan pembulatan ke bawah ~floor division (//)
hasil = a // b
print(a, "//", b, "=", hasil)

# Modulus (sisa pembagian) (%)
hasil = a % b
print(a, "%", b, "=", hasil)

# Pangkat (**)
hasil = a**b
print(a, "**", b, "=", hasil)

""" Prioritas operasi sama seperti matematika biasa (Operational precedence):
1. ()
2. exponen **
3. perkalian dan teman-teman * / ** % //
4. penjumlahan dan pengurangan + -
"""
# Contoh:
x = 3
y = 2
z = 4

hasil = x**y * z + x / y - y % z // x
print(x, "**", y, "*", z, "+", x, "/", y, "-", y, "%", z, "//", x, "=", hasil)

# Kurung akan mengambil prioritas yang lebih tinggi
hasil = x ** (y * z + x) / y - y % z // x
print(x, "**", "(", y, "*", z, "+", x, ")", "/", y, "-", y, "%", z, "//", x, "=", hasil)
