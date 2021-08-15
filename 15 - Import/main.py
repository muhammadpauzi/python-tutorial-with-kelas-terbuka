# Import semua yang ada di file tersebut
import module

# Alias / as
# import module as m

# Import hanya satu atau lebih variable atau function atau yang lain
# from module import nama, umur
# from module import nama as n, umur as u
# from module import *


print("Nama dari modul:", module.nama)
print("Umur dari modul:", module.umur)
module.ubahNama("Nama Baru")
print("Nama baru dari modul:", module.nama)
