from timeit import timeit
from sys import getsizeof

users = (
    ("1", "Muhammad Pauzi", "muhammadpauzi@gmail.com"),
    ("2", "Muhammad Sukri", "muhammadsukri@gmail.com"),
    ("3", "Muhammad Ilham", "muhammadilham@gmail.com"),
)

print(50*"=")

i = 1
for user in users:
    print("No:", i)
    print("  ID:", user[0])
    print("  Name:", user[1])
    print("  Email:", user[2])
    i += 1

print(50*"=")

print("Time:", timeit(str(users)))
print("Size:", getsizeof(users))

print(50*"=")
