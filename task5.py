#5. Создать базовый класс сотрудник и два дочерних класса – менеджер и работник.
# В базовый класс добавить get_paid(), который в дальнейшем переопределить в дочерних, чтобы сотрудники разных должностей получали различную зарплату

class Employe:
    def get_paid(self):
        return "зарплата сотрудника"

class Manager(Employe):
    def __init__(self, salary):
        self.salary = salary

    def get_paid(self):
        return f"Зарплата менеджера: {self.salary}"

class Worker(Employe):
    def __init__(self, salary):
        self.salary = salary

    def get_paid(self):
        return f"Зарплата работника: {self.salary}"

m = Manager(222222)
w = Worker(111)
print(m.get_paid())
print(w.get_paid())