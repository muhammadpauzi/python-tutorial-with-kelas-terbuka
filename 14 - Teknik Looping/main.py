members = [
    'Muhammad Pauzi', "Muhammad Sukri", "Muhammad Ilham"
]

email = [
    "muhammadpauzi@gmail.com", "muhammadsukri@gmail.com", "muhammadilham@gmail.com"
]

# Enumerate for iteration
# i = 1
for i, member in enumerate(members, 1):
    print(i, member)
    # i += 1
print("\n")

# Zip / Menggabungkan list
for member, email in zip(members, email):
    print("Nama:", (len(member) - 4)*" ", "Email:")
    print(member, " ", email, "\n")

# Set / Himpunan
kota = {"Medan", "jakarta", "Bandung", "Surabaya"}
for k in sorted(kota):
    print(k)
print("\n")

# Dictianory
negara = {
    "Indonesia": "Jakarta",
    "Malaysia": "Kuala Lumpur",
    "Singapura": "Singapura",
    "Thailand": "Bangkok"
}

for n in negara.items():
    print("Negara", n[0], "ibukotanya adalah", n[1])
