# Lists or array
arr = [1, 2, 3, 4, 5, 6, 7, 8]

# Index array
arr2 = arr[0]  # or arr[-1] = [8]
# Memotong array
arr3 = arr[0:3]  # or arr[:4] = [1,2,3,4]

arr4 = [9, 10, 11, 12, 13, 14, 15]

# Merubah isi
arr4[0] = 100

# Menambah isi array (push)
arr5 = arr + arr4

# Copy isi array ( [:] )
arr6 = arr[:]

# Merubah isi array menggunakan metoda slicing
arr[0:2] = [200, 300]

# Menambahkan array didalam array ( Multi dimensi array )
arr7 = [arr, arr4]

# Method array
# Append = untuk menambahkan nilai baru keakhir array
arr.append(1)

# Functions
lenArr = len(arr)
print(lenArr)
