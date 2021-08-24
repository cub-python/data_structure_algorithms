# 6. В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import random
N = 10
a = [0]*N
for i in range(N):
    a[i] = int(random()*50)
    print('%3d' % a[i], end='')
print()
min_id = 0
max_id = 0                  #запоминаем в переменных не сами значения элементов, а их индексы.
for i in range(1,N):        # находим min и max элементы массива в цикле массива
    if a[i] < a[min_id]:
        min_id = i
    elif a[i] > a[max_id]:
        max_id = i
print(a[min_id], a[max_id])
if min_id > max_id:
    min_id, max_id = max_id, min_id
summa = 0                        # До подсчета суммы элементов, находящихся между мин и макс, переменной sum присвоим 0.
for i in range(min_id+1, max_id): # перебираем в цикле for массив от след за min элемента до элемента предшеств max.
    summa += a[i]          # В теле цикла к значению sum добавляем значение текущего элемента массива
print(summa)