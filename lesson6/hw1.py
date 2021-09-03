# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду.
# Также укажите в комментариях версию Python и разрядность вашей ОС.

import sys
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


memory_size = 0
memory_size += sys.getsizeof(A)
memory_size += sys.getsizeof(S)
memory_size += sys.getsizeof(q)
memory_size += sys.getsizeof(i)
memory_size += sys.getsizeof(j)
memory_size += sys.getsizeof(n)



print('Переменные занимают', memory_size)


# в варианте «Решето Эратосфена» скорость быстрее и чем n больше,разница увеличивается
# 2-й вариант по сложности > чем 1-й вар
