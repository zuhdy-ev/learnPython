print("=== EXCERCISE PART 1 ===")
print("Program Konversi Satuan Temperatur\n")

print("Celcius ke satuan lain")
celcius = float(input("Masukkan nilai suhu: "))
print("- Suhu dalam Celcius adalah", celcius, "derajat")

# Reamur (4/5 Celcius)
reamur = (4 / 5) * celcius
print("- Suhu dalam Reamur adalah", reamur, "derajat")

# Fahrenheit ((9/5) Celcius + 32)
fahrenheit = ((9 / 5) * celcius) + 32
print("- Suhu dalam Fahrenheit adalah", fahrenheit, "derajat")

# Kelvin (Celcius + 273)
kelvin = celcius + 273
print("- Suhu dalam Kelvin adalah", kelvin, "derajat")

print(
    "\n---\nTugas: \n1. Buat fungsi konverter dari Fahrenheit ke Kelvin\n2. Buat fungsi dari Kelvin ke Fahrenheit"
)

# No. 1
print("\n1. Fahrenheit ke Kelvin")
fahrenheitToKelvin = (fahrenheit - 32) * (5 / 9) + 273
print("- Suhu dalam Kelvin adalah", fahrenheitToKelvin, "derajat")

# No. 2
print("\n2. Kelvin ke Fahrenheit")
kelvinToFahrenheit = (kelvin - 273) * (9 / 5) + 32
print("- Suhu dalam Fahrenheit adalah", kelvinToFahrenheit, "derajat")
