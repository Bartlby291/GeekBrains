"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""


class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        return 'Машина движется'

    def stop(self):
        return 'Машина остановилась'

    def turn_left(self):
        return 'Машина повернула направо'

    def turn_right(self):
        return 'Машина повернула налево'

    def show_speed(self):
        return f'Скорость автомобиля: {self.speed}км'


class TownCar(Car):
    def show_speed(self):
        if self.speed < 60:
            return f'Скорость автомобиля: {self.speed}км'
        else:
            return f'Скорость автомобиля: {self.speed}км. Вы привысили снорость на: {self.speed - 60}км'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed < 40:
            return f'Скорость автомобиля: {self.speed}км'
        else:
            return f'Скорость автомобиля: {self.speed}км. Вы привысили снорость на: {self.speed - 40}км'


class PoliceCar(Car):
    pass
