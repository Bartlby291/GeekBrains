"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income
(доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
"""
import random

# Генерируем случайные числа для словоря "_income"
def generate_dict():
    return {'wage': random.randint(15000, 30000), 'bonus': round(random.uniform(1, 2), 2)}


class Worker:
    name = str
    surname = str
    position = str

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = generate_dict()


class Position(Worker):
    def get_full_name(self):
        return f'{self.position}: {self.surname} {self.name}'

    def get_total_income(self):
        return self._income['wage'] * self._income['bonus']


user_name = input('Ведите ваше имя >>> ')
user_surname = input('Введите вашу фамилию >>> ')
user_position = input('Введите вашу должность >>> ')

user_input = Position(user_name, user_surname, user_position)
print(f'Привет, {user_input.get_full_name()}! Твоя зарплата: {user_input.get_total_income()}')
