class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for work car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


masserati = SportCar(400, 'Red', 'Masserati', False)
toyota = TownCar(30, 'White', 'Toyota', False)
volkswagen = WorkCar(70, 'Rose', 'Volksvagen', False)
matiz = PoliceCar(240, 'Blue',  'Matiz', True)
print(volkswagen.turn_left())
print(f'{toyota.turn_right()},{masserati.stop()}')
print(f'{volkswagen.go()} {volkswagen.show_speed()}')
print(f'{volkswagen.name} {volkswagen.color}')
print(f'{masserati.name} {masserati.is_police}')
print(f'{volkswagen.name} {volkswagen.is_police}')
print(masserati.show_speed())
print(toyota.show_speed())
print(matiz.police())
print(matiz.show_speed())
