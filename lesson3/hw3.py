# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

# Поиск минимума и максимума (а лучше их индексов).
# Обмен минимального и максимального элемента местами.


from random import random

N = 15
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 100)
    print(arr[i], end=' ')
print()

mn = 0
mx = 0
for i in range(N):
    if arr[i] < arr[mn]:
        mn = i
    elif arr[i] > arr[mx]:
        mx = i
print('arr[%d]=%d arr[%d]=%d' % (mn + 1, arr[mn], mx + 1, arr[mx]))
b = arr[mn]
arr[mn] = arr[mx]
arr[mx] = b
for i in range(15):
    print(arr[i],end=' ')
print()