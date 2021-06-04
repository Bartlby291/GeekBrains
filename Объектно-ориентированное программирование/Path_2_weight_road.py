"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса асфальта
для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
"""
class Road:
    _length = int
    _width = int
    wt = int
    depth = int
    def __init__(self, lenght, widht, wt = 25, depth = 3):
        self._length = lenght
        self._width = widht
        self.wt = wt
        self.depth = depth
    def calculate(self):
        weight = self._length * self._width * self.wt * self.depth
        return weight
weight_road = Road(529, 8)
print(f'Масса покрытия состовляет: {weight_road.calculate()}кг')
