# 5. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
from random import randint
let1 = input("Введите первую букву : ")
let2 = input("Введите вторую букву : ")

alph = ['0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

let1_ind = alph.index(let1)
let2_ind = alph.index(let2)

rand_let = alph[randint(let1_ind, let2_ind)]

print(f'Выбранные вами буквы имеют порядковые номера: '
      f'{let1} = {let1_ind}, {let2} = {let2_ind},'
      f' и между ними находятся {let2_ind - let1_ind - 1} букв')