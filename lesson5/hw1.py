# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего


import collections

company = collections.name_tuple('company', ['name', 'p1', 'p2', 'p3', 'p4', 'y'])
companys = []
p = int(input("Введити кол-во компаний: "))
total = 0
for i in range(q):
    name = input(f"Название {i + 1}-ого предприятия: ")
    q1 = int(input("Прибыль за 1 квартал: "))
    q2 = int(input("Прибыль за 2 квартал: "))
    q3 = int(input("Прибыль за 3 квартал: "))
    q4 = int(input("Прибыль за 4 квартал: "))
    y = p1 + p2 + p3 + p4
    total += y
    companys.append(company(name = name, p1 = p1, p2 = p2, p3 = p3, p4 = p4, y = y))
total_avg = total / p
print(f"Предприятия с прибылью выше средней {total_avg}: ")
for company in companys:
    if company.y >= total_avg:
        print(company.name)
print(f"Предприятия с прибылью неже средней {total_avg}: ")
for company in companys:
    if company.y < total_avg:
        print(company.name)
