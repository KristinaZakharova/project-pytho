# 1. Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.
print('Exercise 1')

n = int(input('n ='))
print('n = ', n)
n = int(n)
print('n * 4 =', n * 4)
print(type(n))
c = float(input('c ='))
res = n + c
print(type(res))
print('n + c = ', res)
#2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
print('Exercise 2')
#
time = input('time, sec =')
time = int(time)

hours = int(time // 60 ** 2)
minutes = int((time - hours * 60 ** 2) // 60)
seconds = int((time - hours * 60 ** 2) % 60)


if hours < 10:
    hours = str(hours)
    hours = '0' + hours

if minutes < 10:
    minutes = str(minutes)
    minutes = '0' + minutes

if seconds < 10:
    seconds = str(seconds)
    seconds = '0' + seconds


print(f'Time {hours}:{minutes}:{seconds}')

# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

print('Exercise 3')

n = int(input('Input number '))
n = str(n)
nn = n + n
nnn = n + n + n
n = int(n)
nn = int(nn)
nnn = int(nnn)

s = n + nn + nnn
print(f'If n={n}, then n + nn + nnn = {s}')

# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

print('Exercise 4')
n = int(input('input positive integer '))
if n <= 0:
    print('the insert integer not positive')
else:
    max = 0
    while n > 0:
        a = n % 10
        if a > max:
            max = a
        n = n // 10
    print ('max number = ', max)

# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.

print('Exercise 5-6')
rev = float(input('Input your revenue (введите выручку) '))
costs = float(input('Input your costs (введите издержжки) '))

if rev > costs:
    print('you are in profit (прибыль)')
    profit = rev - costs
    empl = int(input('Print number of your employees '))
    prperempl = profit / empl
    print('Profit per employee = ', prperempl)
elif rev == costs:
    print('you are in zero profit (нулевая прибыль)')
elif rev < costs:
    print('you are at loss (убыток)')

print('Exercise 7')
a = float(input("push sportsman's result on the first day in km  "))
b = float(input("push result 'b' "))

n = 1
print(f'{n} day: {a} ')
while a < b:
    a = a * 1.1
    n = n + 1
    print(f'{n} day: {a}')
print(f'Answer: on the {n} day sportsman has been having results - at least {b} km')

