
#1. Создать класс для геометрической фигуры на выбор и
# добавить в него два метода – первый для расчета площади,
# второй для расчета периметра
class Rectangle:
    def __init__(self, a,b):
        self.check_value(a)
        self.check_value(b)
        self.a = a
        self.b = b

    def check_value(self, v):
        if type(v) not in (int, float):
            raise TypeError("неверный тип данных")

    def calc_square(self):
        return self.a * self.b

    def calc_perimetr(self):
        return 2* (self.a + self.b)

#2. Создать класс “Человек” с полями: имя, город проживания и год рождения.
# Написать метод, который будет возвращать возраст человека в годах
from datetime import datetime

class Person:
    def __init__(self, name, city, year_birth):
        self.name = name
        self.city = city
        self.year_birth = year_birth

    def age(self):
        return datetime.now().year - self.year_birth

p = Person('igor', 'Ufa',2000)
