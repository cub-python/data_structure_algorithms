# 4. Определить, какое число в массиве встречается чаще всего.
# Будем по-очереди (в цикле) брать элементы массива с первого до предпоследнего и сравнивать его с элементами,
# стоящими после него. С элементами, стоящими впереди, сравнивать не надо, т.к. если там есть равный ему,
# то текущий элемент уже был учтен, и количество раз, какое он встречается в массиве, уже находилось.
# Последний элемент не с чем сравнивать, поэтому цикл идет до предпоследнего элемента


from random import random

N = 15
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 20)
print(arr)

num = arr[0]            # будем записывать в переменную num найденный самый встречаемый элемент
max_f = 1                #  переменную max_frq – количество раз, которое он встречается.
for i in range(N - 1):
    f = 1
    for k in range(i + 1, N):
        if arr[i] == arr[k]:
            f += 1
    if f > max_f:
        max_f = f
        num = arr[i]

if max_f > 1:
    print(max_f, 'раз(а) встречается число', num)
