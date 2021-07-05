class Road:
    def __init__(self, _lenght, _width):
        self._length = _lenght
        self._width = _width

    def count_mass(self, layer):
        print(f'Масса дороги {int((layer * self._length * self._width * 25) / 1000)} т.')