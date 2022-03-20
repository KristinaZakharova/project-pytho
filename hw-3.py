# # 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# # Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
# print('Exercise 1')
# x = int(input('x '))
# y = int(input('y '))
#
# def div_x(x, y):
#     if y != 0:
#         return x / y
#     else:
#         return 'error'
#
# print(div_x(x, y))
#
# # 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# # имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
# # как именованные аргументы. Осуществить вывод данных о пользователе одной строкой
# print('Exercise 2')
#
# def user(**kwargs):
#     try:
#         name = input('name ')
#         year = int(input('year of birth '))
#         em = input('email ')
#         phone = int(input('Phone '))
#         print(f'name -  {name}, year of birth - {year}, email - {em}, phone - {phone}')
#     except ValueError:
#         print('Process stopped - ValueError')
#
# user()
#
# # version 2.2
# print('exercise 2.2')
# def user2_2(name, year, em, phone):
#
#     # try:
#     #     name = input('name ')
#     #     year = int(input('year of birth '))
#     #     em = input('email ')
#     #     phone = int(input('Phone '))
#     # except ValueError:
#     #     return "ValueError"
#     print(f'name - {name}, year of birth - {year}, email - {em}, phone - {phone}')
#
#
# user2_2(year=1991, em='kris@mail', name='kjjfj', phone=321354)
#
# # 3. Реализовать функцию my_func(),
# # которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
# print('Exercise 3')
#
# def my_func(a, b, c):
#     if a >= b:
#         if b >= c:
#             s = a + b
#         else:
#             s = a + c
#     elif a < b:
#         if a >= c:
#             s = a + b
#         else:
#             s = b + c
#     return s
#
# print(my_func(5, 6, 9))
#
# # 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# # Выполните возведение числа x в степень y.
# # Задание реализуйте в виде функции my_func(x, y).
# # При решении задания нужно обойтись без встроенной функции возведения числа в степень.
#
# print('Exercise 4')
#
# def my_func2(x, y):
#     if x > 0  and y < 0:
#         res = 1
#         for el in range(-1, y - 1, -1):
#             res = res / x
#         return res
#     else:
#         print('Error')
#
# x = int(input('x'))
# y = int(input('y'))
#
# print(my_func2(x, y))
# print('check = ', x ** y)
#
# def my_func3(x, y):
#     if x > 0 and y < 0:
#         res = 1 / x ** abs(y)
#         return res
#     else:
#         print('Error')
#
# x = int(input('x'))
# y = int(input('y'))
#
# print(my_func3(x, y))
# print('check = ', x ** y)


# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.



def func_sum():
    s = 0
    while True:
        li = input('Введите числа, разделенные пробелом, для выхода введите stop: ')
        li = li.split()
        try:
            for el in li:
                if el == 'stop':
                    return 'end'
                else:
                    s += int(el)
            print(s)
        except (ValueError, TypeError):
            print('Try again')
        continue

func_sum()


func_sum()
        











