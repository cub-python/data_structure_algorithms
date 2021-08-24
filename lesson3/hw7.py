# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from random import randint

array = [randint(0, 25)
         for i in range(10)]
print(array)
min1 = min(array)
array.remove(min1)
min2 = min(array)
print(min1)
print(min2)
