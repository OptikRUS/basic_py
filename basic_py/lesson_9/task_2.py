class Road:
    def __init__(self, _lenght, _width):
        self._length = _lenght
        self._width = _width

    def count_mass(self, layer):
        print(f'Масса дороги {int((layer * self._length * self._width * 25) / 1000)} т.')

my_road = Road(5000, 20) # длина и ширина дороги
my_road.count_mass(5) # толщина слоя асфальта