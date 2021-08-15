# Di python tidak ada ternary yang ada if ..
# .. dan else dalam satu baris

# 1. nilai yang dikembalikan jika kondisi true if kondisi else nilai yang dikembalikan jika kondisi false

# 2. kondisi true if kondisi else kondisi false

nilai = input("Masukan nilai: ")

print("Anda Lulus" if int(nilai) >= 75 else "Anda Tidak Lulus")


# Atau ada cara lain menggunakan tuples
# 1. (Nilai yang akan dikembalikan jika kondisi true, Nilai yang akan dikembalikan jika kondisi false)[kondisi]
# 2. (true, false)[kondisi]

jomblo = True  # Kondisi
status = ("Menikah", "Single")[jomblo]
print(status)
