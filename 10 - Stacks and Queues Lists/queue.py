# Queue adalah teknik menambahkan element dari akhir element dan menghapus element pertama dari array/list

# Import function deque dari collections
# Jika menggunakan deque akan ada method tambahan seperti : appendleft(), popleft() dll.
from collections import deque

queue = deque([1, 2, 3, 4, 5, 6])
print(type(queue))
print(queue)

queue.append(7)
print(queue)
queue.append(8)
print(queue)
# popleft() untuk menghapus element pertama dari list atau deque
queue.popleft()
print(queue)
queue.popleft()
print(queue)
