# Светофор

import time


class TrafficLight:
    COLOR_TIME = {'Red': 7, 'Yelloy': 2, 'Green': 4}
    __color = None
    __c_index = 0
    change = 3
    def __init__(self, init_color = 'Red', change = 3):
        self.__color = init_color if self.COLOR_TIME.get(
            init_color) else list(self.COLOR_TIME.keys())[self.__c_index]
        self.__c_index = list(self.COLOR_TIME.keys()).index(self.__color)
        self.change = change

    def running(self):
        print(self.__color)
        while self.change:
            time.sleep(self.COLOR_TIME.get(self.__color))
            self.__c_index = (self.__c_index + 1) % 3
            self.__color = list(self.COLOR_TIME.keys())[self.__c_index]
            print(self.__color)
            self.change -= 1


while True:
    shift = input('Сколько будет смен цветов?')
    try:
        shift = int(shift)
        break
    except ValueError:
        print('Ожидаем целое число')
lights = TrafficLight('Red', shift)
lights.running()
