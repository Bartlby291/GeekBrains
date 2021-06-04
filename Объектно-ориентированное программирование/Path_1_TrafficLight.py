"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в
режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно
осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и
вызвав описанный метод.
"""
import time


class TrafficLight:
    __color = int

    def __init__(self, color):
        self.__color = color

    def running(self):
        if self.__color == 1:
            print('Красный, ехать нельзя!')
            time.sleep(7)
            self.__color = 2
        elif self.__color == 2:
            print('Желтый, приготовься!')
            time.sleep(2)
            self.__color = 3
        elif self.__color == 3:
            print('Зеленый, доброго пути!')
            time.sleep(7)
            self.__color = 1



print('Примем, что: 1 - красный; 2 - желтый; 3 - зеленый')
try:
    user_input = int(input('Введите число которое означает цвет, с которого необходимо начать >>> '))
except:
    print('Вы ввели не число')


traffic_light = TrafficLight(user_input)
counter = 0
while counter < 15:
    counter += 1
    traffic_light.running()

