#3. Создать класс калькулятор и описать в нём методы для базовых математических операций для двух чисел

class Calculator:

    @classmethod
    def check(cls, a, b):
        if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
            raise TypeError("ошибка: неверный тип данных")

    @staticmethod
    def sum(a, b):
        Calculator.check(a, b)
        return a + b

    @staticmethod
    def dif(a, b):
        Calculator.check(a, b)
        return a - b

    @staticmethod
    def composition(a, b):
        Calculator.check(a, b)
        return a*b

    @staticmethod
    def division(a,b):
        Calculator.check(a, b)
        if b!=0:
            return a/b
        else:
            return "ошибка деления на 0"


print(Calculator.sum(3,4))
print(Calculator.dif(3,4))
print(Calculator.composition(3,4))
print(Calculator.division(3,4))
#4. Изучить метод  __str__, создать класс с данным методом, продемонстрировать его выполнение
class Dog:
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return f"{self.__name}"

max = Dog("Max")
print(max)