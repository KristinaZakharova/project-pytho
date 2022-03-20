# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.


# f = open(r'text_1.txt', 'w+', encoding='utf-8')
# t = []
# while True:
#     str = input('введите строку ')
#     if str == '':
#         break
#     else:
#         t.append(f'{str}\n')
#
# f.writelines(t)
#
# f.seek(0)
# r = f.read()
# print(r)
#
# f.close()

# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
#
# f = open(r'text_22.txt', 'r', encoding='utf-8')
#
# r = f.read()
# print(r)
#
# str = r.split('\n')
# print('Число строк = ', len(str))
# print(str)
# def wordnumber():
#     n = 0
#     for el in str:
#         n += 1
#         w = el.split()
#         wn = len(w)
#         print(f'{n}-я cтрока: {wn} словo(a)')
#     return
#
# wordnumber()
# f.close()

# 3. Cоздать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов ( не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

# f = open(r'text_3.txt', 'r', encoding='utf-8')
#
# r = f.read()
# print(r)
#
# str = r.split('\n') # разбили на список построчно
#
#
# spisok = {} # создали пустой словарь
# for el in str:  # элемент с индексом 0 из каждой строки это ключ, 1 - значение
#     el = el.split()
#     fam = el[0]
#     zp = el[1]
#     spisok[fam] = zp
#
# all_zp = list(spisok.values()) # создали список со значениями зп
#
#
# all_zp = [int(el) for el in all_zp] # преобразовали в числа
#
#
# sr_zp = round(sum(all_zp)/len(all_zp)) # вычислили среднее
# print(f'средняя зарплата по отделу = {sr_zp} рублей')
#
# spisok_int = {}
# for k, v in spisok.items(): # перевели значения из строки в число
#     spisok_int[k] = int(v)
# print('Оклад меньше 20000 рублей: ')
# for k, v in spisok_int.items(): # если зп меньше 20 000, печатаем фамилию
#     if v < 20000:
#         print(k)
#
#
# f.close()
#
# 4. Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

# f = open(r'text_4.txt', 'r', encoding='utf-8')
# new = open(r'text_4_new.txt', 'a', encoding='utf-8')
# rus = ['Один', 'Два', 'Три', 'Четыре']
# n = 0
# for line in f:
#     line = line.split()
#     line[0] = rus[n]
#     n +=1
#     line.append('\n')
#     str = ' '.join(line)
#     print(str)
#     new.write(str)
#
# new.close()
# f.close()

# 5.Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

# f = open(r'text_5.txt', 'a+', encoding='utf-8')
#
# str = input('введите числа, разделенные пробелом ') # ввели строку чисел
#
# f.write(f'{str}\n') # дописали строку в файл
# f.seek(0) # перевели курсор в начало
# t = []
# for line in f: # построчно прочитали файл и выполнили действие для каждой стркои
#     line = [int(el) for el in line.split()] # разделили строку, преобразовали каждый элемент списка в число
#     t.append(sum(line)) # вычислили сумму строки
# print('Сумма чисел в файле = ', sum(t))
#
# f.close()

# 6. Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.

# f = open(r'text_6.txt', 'r', encoding='utf-8')
# spisok = {}
#
# list = []
# for line in f:
#     chasy = []
#     line = line.replace('(', ' ')
#     line = line.replace(')', ' ')
#     line = line.replace(':', ' ')
#     line = line.replace('  - ', ' ')
#     line_i = line.split()
#     for el in line_i:
#         try:
#             i = int(el)
#             chasy.append(i)
#         except (TypeError, ValueError, IndentationError):
#             continue
#     s = sum(chasy)
#     spisok[line_i[0]] = s
#
# print(spisok)
# f.close()


# 7.Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.

f = open(r'text_7.txt', 'r', encoding='utf-8')

sr_pr = []
n = 0
dict_pr = {}
dict_ub = {}
dict_sr = {}
e = []

for line in f:
    li = line.split()

    delta = int(li[2]) - int(li[3])
    if delta > 0:
        sr_pr.append(delta)
        n += 1
        print('Прибыль составила: ', delta)
        dict_pr[li[0]] = delta
    else:
        print('Убыток составил: ', delta)
        dict_ub[li[0]] = delta

sr_pr = sum(sr_pr) / n
print(f'Средняя прибыль компаний с положительной рейнтабельностью составляет: {sr_pr}')
dict_sr['Средняя прибыль:'] = sr_pr

e = [dict_pr, dict_ub, dict_sr]
print(e)

import json


with open('text_7_json.txt', 'w', encoding='utf-8') as write_f:
    json.dump(e, write_f)

f.close
