# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

import random

lst = [random.randint(-100, 100) for i in range(10)]
print(f'Исходный целочисленный список :\n{lst}')


def bleb_sort(lst):
    n = 1

    while n < len(lst):
        sorted = True
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                sorted = False

        if sorted == True:
            break

        n += 1

        print(f'Отсортированный список по убыванию:\n {lst}')


bleb_sort(lst)
