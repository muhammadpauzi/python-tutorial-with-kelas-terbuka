import sys  # Untuk memeriksa ukuran dari data
import timeit  # Untuk memerika waktu proses
# List
ganjil = [1, 3, 5, 7, 9]

# Tuple ()
# Tuple adalah tipe data yang mirip dengan list namun tidak bisa dimanipulasi sperti dihapus, ditambah dll.
genap = (2, 4, 6, 8, 10)

# Indexing tuple sama dengan list
print(genap[1])

# genap.append() # Tidak bisa

# dir untuk memeriksa method yang bisa digunakan tipe data dari varibale
# print(dir(genap))

# Tuple ukurannya lebih kecil dan lebih cepat
print("Ukuran List:", sys.getsizeof(ganjil))
print("Ukuran Tuple:", sys.getsizeof(genap))
# Tuples lebih cepat
print("Waktu List:", timeit.timeit('[1,2,3,4,5,6,7]', number=1000000))
print("Waktu Tuple:", timeit.timeit('(1,2,3,4,5,6,7)', number=1000000))

# Tuple cocok untuk hanya menampilakan data
