# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# class Matrix1: #только создает матрицу через ввод (решение задачи дальше)
#
#     def __init__(self, x):
#         self.x = x
#         m = []
#         i = input('Введите числа через пробел ').split() # сделали из строки список строк
#         sp_1 = [int(el) for el in i] # преобразовали элементы списка в числа
#
#         n = 0
#         y = 0
#         while n < (len(sp_1) // self.x):
#             n += 1
#             s = [sp_1[i] for i in range(y, y + self.x)]
#             m.append(s)
#             print(f'{s[0]} {s[1]} {s[2]}')
#             y += self.x
#         if len(sp_1) % self.x > 0:
#             str_last = [sp_1[i] for i in range(y, len(sp_1))]
#             m.append(str_last)
#             str_last = ' '.join(map(str, str_last)) #преобразовали последний список в строку
#             print(str_last)
#         self.m = m



        # str_1 = [sp_1[i] for i in range(0, self.x)] #1я строка матрицы
        # str_2 = [sp_1[i] for i in range(self.x, self.x * 2)] #2я строка матрицы
        #
        # m.append(str_1)
        # m.append(str_2)
        # for el in m:
        #     print(f'{el[0]} {el[1]} {el[2]} ')
        #


# m_1 = Matrix1(3)

# class Matrix2: #способ номер 2, когда при формировании объекта класса сразу задаются данные(список списков)
#     m = []
#
#     def __init__(self, m):
#         self.m = m
#
#     def __str__(self):
#         s = ''
#         for el in self.m:
#             s_2 = ' '.join(map(str, el))
#             s = s + s_2 + '\n'
#         return s
#
#     def __add__(self, other): #1й способ
#         new = []
#         for i in range(0, len(self.m)):
#             new.insert(i, [])
#             for j in range(0, len(self.m[i])):
#                 new[i].insert(j, (self.m[i][j] + other.m[i][j]))
#         return Matrix2(new)
#
#
# m_2 = Matrix2([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(m_2)
# m_3 = Matrix2([[1, 1, 1], [3, 1, 2], [1, 0, 1]])
# print(m_3)
#
# m_su = m_2 + m_3
# print(m_su)

# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
# from abc import ABC, abstractmethod
#
# class Clothes(ABC):
#     size = int
#     def __init__(self, lab, size):
#         self.lab = lab
#         self.size = size
#
#     @abstractmethod
#     def size(self):
#         return self.__size
#
#     @abstractmethod
#     def size(self, size):
#         pass
#
#     @abstractmethod
#     def tag(self):
#         print(f'Название: , Бренд: {self.lab}, Размер: {self.__size}')
#
#     @abstractmethod
#     def cloth(self):
#         pass
#
# class Coats(Clothes):
#
#     @property
#     def size(self):
#         return self.__size
#
#     @size.setter
#     def size(self, size):
#         if size < 40 or size > 60:
#             print(f'Бренд {self.lab} не шьет пальто {self.__size}-го размера')
#         else:
#             self.__size = size
#
#     def tag(self):
#         print(f'Название: Пальто, Бренд: {self.lab}, Размер: {self.__size}')
#
#     def cloth(self):
#         cl = round(self.__size / 6.5 + 0.5, 1)
#         print(f'На пальто {self.__size}-го размера требуется {cl} метров ткани')
#
# class Costum(Clothes):
#
#     @property
#     def size(self):
#         return self.__size
#     @size.setter
#     def size(self, size):
#         if size < 160 or size > 180:
#             print(f'Фабрика {self.lab} не шьет костюмы на рост {self.__size} см . Выберите рост в диапазоне от 160 до 180 см')
#         else:
#             self.__size = size
#
#
#     def tag(self):
#         print(f'Название: Костюм , Бренд: {self.lab}, Размер: {self.__size}')
#
#     def cloth(self):
#         cl = round((2 * self.__size) / 100 + 0.3, 1)
#         print(f'На костюм {self.__size}-го размера требуется {cl} метров ткани')
#
# coa_1 = Coats('Zara', 30)
# coa_1.cloth()
# cost = Costum('Next', 170)
# cost.cloth()

# 3.

class Cell:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        s = self.x + other.x
        return Cell(s)

    def __sub__(self, other):
        d = self.x - other.x
        if d > 0:
            return Cell(d)
        else:
            return f'Вычитание невозможно'

    def __mul__(self, other):
        m = self.x * other.x
        return Cell(m)

    def make_order(self, y):
        self.y = y
        sp = [el for el in range(0, self.x)]
        print(sp)
        for i in range(0, len(sp), self.y):
            yield sp[i : i + self.y]
        return sp




c_1 = Cell(10)
# c_2 = Cell(2)
# c_3 = c_1 + c_2
# c_4 = c_1 - c_2
# print(type(c_4))
# print(c_3)
print(c_1.make_order(2))







