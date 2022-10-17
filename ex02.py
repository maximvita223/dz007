# Масса  асфальта

class Road:
    __length = None
    __width = None
    weigth = None
    tickness = None
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def intake(self):
        self.weigth = 25
        self.tickness = 0.05
        intake = self.length * self.width * self.weigth * self.tickness / 1000
        print(f'Требуется {intake} тонн для покрытия 1 кв. метра')

road_to_village = Road(100, 5)
road_to_village.intake()