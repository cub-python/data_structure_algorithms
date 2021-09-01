# 1. Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
# Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.

import timeit

from random import random

A = 50
S = 20
q = []

for i in range(S):      # O(n)
    b = []
    for j in range(A):          # O(n)
        n = int(random() * 200)
        b.append(n)
        print('%4d' % n, end='')
    q.append(b)
    print()                # O(n2)

mx = -1
for j in range(A):          # O(n)
    mn = 80
    for i in range(S):       # O(n)
        if q[i][j] < mn:     # O(n)
            mn = q[i][j]
    if mn > mx:              # O(n)
        mx = mn                      # O(2n2)


print("Максимальный среди минимальных: ", mx)
print(timeit.timeit())

# сложность алгоритма : O(2n2) + O(n2)  = O(3n2), квадратичная сложность
# скорость алгоритма состовляет: 0.006723699999999999
# 0.007014199999999998, это скорость при увелич параметров