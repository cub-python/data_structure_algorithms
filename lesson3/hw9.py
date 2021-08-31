# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.


from random import random

A = 10
S = 5
q = []
for i in range(S):
    b = []
    for j in range(A):
        n = int(random() * 80)
        b.append(n)
        print('%4d' % n, end='')
    q.append(b)
    print()

mx = -1
for j in range(A):
    mn = 80
    for i in range(S):
        if q[i][j] < mn:
            mn = q[i][j]
    if mn > mx:
        mx = mn
print("Максимальный среди минимальных: ", mx)
