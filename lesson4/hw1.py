# 1. Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.

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
    mn = 200
    for i in range(S):       # O(n)
        if q[i][j] < mn:
            mn = q[i][j]
    if mn > mx:
        mx = mn                      # O(n2)


print("Максимальный среди минимальных: ", mx)
print(timeit.timeit())

# сложность алгоритма : O(n2) + O(n2)  = O(2n2), квадратичная сложность
# скорость алгоритма состовляет: 0.006723699999999999
# 0.007798299999999994, это скорость при увелич параметров