# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

import hashlib

string = input('Введите строку, состоящая только из маленьких латинских букв: ')
some_string = set()

for i in range(len(string)):
    for j in range(len(string), i, -1):
        h = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
        some_string.add(h)

print(f'Количество различных подстрок в строке: {len(some_string) -1} ')
