print("===LOGIC OPERATION (BOOLEAN)===")

# not, or, and, xor

print("===NOT===")
a = True
c = not a

print("a mengandung nilai =", a)
print("c mengandung nilai =", c)

print("===OR===")
# Jika salah satu nilainya True, maka hasilnya True
a = False
b = False
c = a or b
print(a, "OR", b, "=", c)
a = False
b = True
c = a or b
print(a, "OR", b, "=", c)
a = True
b = False
c = a or b
print(a, "OR", b, "=", c)
a = True
b = True
c = a or b
print(a, "OR", b, "=", c)

print("===AND===")
# Jika salah satu nilainya False, maka hasilnya False
a = False
b = False
c = a and b
print(a, "AND", b, "=", c)
a = False
b = True
c = a and b
print(a, "AND", b, "=", c)
a = True
b = False
c = a and b
print(a, "AND", b, "=", c)
a = True
b = True
c = a and b
print(a, "AND", b, "=", c)

print("===XOR===")
# Akan bernilai True HANYA JIKA ada 1 nilai True, kalau kurang atau lebih dari 1, maka hasilnya False
a = False
b = False
c = a ^ b
print(a, "XOR", b, "=", c)
a = False
b = True
c = a ^ b
print(a, "XOR", b, "=", c)
a = True
b = False
c = a ^ b
print(a, "XOR", b, "=", c)
a = True
b = True
c = a ^ b
print(a, "XOR", b, "=", c)
