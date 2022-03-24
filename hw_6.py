# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.
# import time
# class TrafficLight:
#     __colors = ['Красный', 'Желтый', 'Зеленый']
#
#     def __init__(self, color):
#         self.color = color
#
#     def start(self, i):
#         for i in range(i):
#             print(self.__colors[self.color])
#             time.sleep(7)
#             print(self.__colors[(self.color + 1) % 3])
#             time.sleep(3)
#             print(self.__colors[(self.color + 2) % 3])
#             time.sleep(1)
#
#
# tl_1 = TrafficLight(2)
# tl_1.start(2)

# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.
#
# class Road:
#     _lengt = int
#     _width = int
#     def __init__(self, lengt, width):
#         self._lengt = lengt
#         self._width = width
#
#     def asphalt_metod(self):
#         asphalt = self._lengt * self._width * 25 * 5 / 1000
#         print(f'Масса асфальта, необходимая для покрытия дороги длиной {self._lengt}м, шириной {self._width}м, толщиной 5см: {asphalt}тонн')
#
# m_1 = Road(20, 5000)
# m_1.asphalt_metod()

#
# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.
# import self as self
#
#
# class Worker:
#     name = ''
#     surname = ''
#     position = ''
#     wage = int
#     bonus = int
#     _income =int
#
#     def __init__(self):
#         self.name = input('Имя ')
#         self.surname = input('Фамилия ')
#         self.position = input('Должность ')
#         self.wage = int(input('wage '))
#         self.bonus = int(input('bonus '))
#         zp = {'wage': self.wage, 'bonus': self.bonus}
#         self._income = print('income = ', zp)
#
# class Position(Worker):
#     def get_full_name(self):
#         print(self.name + ' ' + self.surname)
#
#     def get_total_income(self):
#         self.total_income = self.wage + self.bonus
#         print('Total income = ', self.total_income)
#
#
# w_1 = Position()
# w_1.get_full_name()
# w_1.get_total_income()


# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

# class Car:
#     speed = int
#     color = ''
#     name = ''
#     is_police = bool
#
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = bool(is_police)
#
#     def go(self):
#         print('Car is going')
#
#     def stop(self):
#         print('Car stopped')
#
#     def turn(self, direction):
#         self.direction = direction
#         print(f'Car turned to the {direction}')
#
#     def show_speed(self):
#         print(f'speed now = {self.speed}')
#
#
# class Towncar(Car):
#     def show_speed(self):
#         if self.speed > 60:
#             print('Speeding')
#
#
# class Sportcar(Car):
#     def sport(self):
#         print("It's a sport car")
#
# class WorkCar(Car):
#     def work(self):
#         print("It's a work car")
#     def show_speed(self):
#         if self.speed > 40:
#             print('Speeding')
#
#
# class Police_Car(Car):
#
#     def police(self):
#         print("It's a police")
#
#
# car_1 = WorkCar(80, 'white', 'garbage truck', 0)
# car_1.show_speed()
# print(car_1.color)
# print(car_1.is_police)
#
# car_2 = Sportcar(120, 'red', 'Ferari', 0)
# car_2.show_speed()
# print(car_2.color)
#

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
#
#
class Stationery:
    title = 'Название'

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):

    title = 'pen'

    def draw(self):
        print(f'{self.title} Запуск письма')
#
class Pensil(Stationery):
    title = 'pensil'

    def draw(self):
        print(f'{self.title} Штриховка')

class Handle(Stationery):
    title = 'handle'

    def draw(self):
        print(f'{self.title }Обводка контура')

pen_1 = Pen()
pen_1.draw()
handle_1 = Handle()
handle_1.draw()
pensil_1 = Pensil()
pensil_1.draw()
