print("===OPERATOR BITWISE===")

# Operator Bitwise adalah operator yang digunakan untuk melakukan. operasi berdasarkan bit / biner
# Angka bit adalah 0 atau 1 dengan basis bilangan adalah 8 angka, dengan index pada tiap barisnya adalah 2^(index)
# 0 = false, 1 = true

a = 9
b = 5

# Operator Bitwise OR (|)
c = a | b
print("\n===OR===")
print("Nilai :", a, ", binary :", format(a, "08b"))
print("Nilai :", b, ", binary :", format(b, "08b"))
print("------------------------------- (|)")
print("Nilai :", c, ", binary :", format(c, "08b"))

# Operator Bitwise AND (&)
c = a & b
print("\n===AND===")
print("Nilai :", a, ", binary :", format(a, "08b"))
print("Nilai :", b, ", binary :", format(b, "08b"))
print("------------------------------- (&)")
print("Nilai :", c, ", binary :", format(c, "08b"))

# Operator Bitwise XOR (^)
c = a ^ b
print("\n===XOR===")
print("Nilai :", a, ", binary :", format(a, "08b"))
print("Nilai :", b, ", binary :", format(b, "08b"))
print("------------------------------- (^)")
print("Nilai :", c, ", binary :", format(c, "08b"))

# Operator Bitwise NOT (~)
c = ~a
print("\n===NOT===")
print("Nilai :", a, ", binary :", format(a, "08b"))
print("------------------------------- (~)")
print("Nilai :", c, ", binary :", format(c, "08b"))
print(
    "------------------------------- (^)"
)  # Kalau mau bener2 nge-flip nilainya, pakai XOR
d = 0b0000001001
e = 0b1111111111
print("Nilai :", e ^ d, ", binary :", format(e ^ d, "08b"))

# Operator Bitwise Shift Left (<<)
c = a << 2
print("\n===SHIFT LEFT===")
print("Nilai :", a, ", binary :", format(a, "08b"))
print("------------------------------- (<<)")
print("Nilai :", c, ", binary :", format(c, "08b"))

# Operator Bitwise Shift Right (>>)
c = a >> 2
print("\n===SHIFT RIGHT===")
print("Nilai :", a, ", binary :", format(a, "08b"))
print("------------------------------- (>>)")
print("Nilai :", c, ", binary :", format(c, "08b"))
