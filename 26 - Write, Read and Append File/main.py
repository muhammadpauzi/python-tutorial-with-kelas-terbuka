"""
Mode :
w = write mode / mode menulis dan menghapus file lama, jika 
    file tidak ada maka akan dibuatkan
r = read only / hanya membaca
a = appending mode / menambahkan text diakhir file
r+ = write and read mode
"""
path = '26 - Write, Read and Append File/file.txt'

# Open file
file = open(path, mode='w')
file.write("Baris Pertama")
file.write("\nBaris Kedua")
file.write("\nBaris Kedua")
file.close()


file2 = open(path, mode='r')
print(file2.read())
# print(file2.readline())
# print(file2.readline())
# print(file2.readline())

file2.close()

file3 = open(path, 'a')
file3.write("\nBaris ini ditambah menggunakan mode append")
file3.close()
