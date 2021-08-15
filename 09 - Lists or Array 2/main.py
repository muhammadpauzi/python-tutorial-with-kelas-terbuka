kota = ['medan', 'jakarta', 'bandung']

# Method untuk menambahkan element baru diakhir array
kota.append('palembang')
print(kota)

# Method untuk menambahkan string yang dipecah keladama array
kota.extend('aceh')
print(kota)

# Method untuk menambahkan element baru menurut index yang diberikan
kota.insert(0, 'makassar')
print(kota)

# Method untuk menghapus element dengan isi element yang ada didalam array
kota.remove('jakarta')
print(kota)

# Method untuk merubah urutan array dari akhir ke awal
kota.reverse()
print(kota)

# Method untuk merubah urutan dari nilai terbesar atau huruf dari string huruf pertama
kota.sort()
print(kota)

# Method untuk meng copy array
newArr = kota.copy()

newArr.append('stabat')
print(kota)
print(newArr)
