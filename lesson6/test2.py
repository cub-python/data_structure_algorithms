import sys
import timeit

from collections import defaultdict
from collections import deque
t1 = timeit.timeit()
a = [2]
n = 10000
for i in range(3, n + 1):  # O(n)
    k = 0
    for j in a:  # O(n)
        if i % j == 0:  # O(n)
            k = 1
    if k == 0:  # O(n)
        a.append(i)

# print(len(a))  # O(2n3)
print(t1)

memory_size = 0
memory_size += sys.getsizeof(a)
memory_size += sys.getsizeof(i)
memory_size += sys.getsizeof(j)
memory_size += sys.getsizeof(n)
print('Переменные занимают', memory_size)

# Используя алгоритм «Решето Эратосфена»

t2 = timeit.timeit()
a = []
for i in range(n + 1):  # O(n)
    a.append(i)
a[1] = 0
i = 2
while i <= n:  # O(n)
    if a[i] != 0:
        j = i + i
        while j <= n:  # O(n)
            a[j] = 0
            j = j + i
    i += 1
# a = set(a)
# a.remove(0)
print(t2)

memory_size = 0
memory_size += sys.getsizeof(a)
memory_size += sys.getsizeof(i)
memory_size += sys.getsizeof(j)

print('Переменные занимают', memory_size)

# в 1-ом варианте Переменные занимают 10092 байт, меньше памяти
# # во 2-ом варианте Переменные занимают 131344 байт
