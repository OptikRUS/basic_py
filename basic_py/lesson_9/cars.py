class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(f'{self.color} {self.name} начинает движение...')

    def stop(self):
        print(f'{self.color} {self.name} стоит на месте.')

    def turn(self, direction):
        self.direction = direction
        print(f'{self.color} {self.name} движется {self.direction}')

    def show_speed(self):
        if self.speed > self._speedlimit:
            if self.speed - self._speedlimit > 19:
                self.is_police = True
            else:
                self.is_police = False
            print(f'{self.color} {self.name} движется со скоростью {self.speed} км/ч, превышение: {self.speed - self._speedlimit} км/ч')
        else:
            print(f'{self.color} {self.name} движется со скоростью {self.speed} км/ч')

    def show_bool(self):
        print(f'{self.color} {self.name} в розыске: {self.is_police}')

class TownCar(Car):     # для городской машины ограничение скорости 60 км/ч
    _speedlimit = 60    # привышение свыше 19 км/ч машина в розыске

class WorkCar(Car):     # для рабочей машины ограничение скорости 60 км/ч
    _speedlimit = 40    # привышение свыше 19 км/ч машина в розыске

class SportCar(Car):    # для спортивной нет ограничения скорости
    def show_speed(self):
        print(f'{self.color} {self.name} движется со скоростью {self.speed} км/ч')

class PoliceCar(Car):   # для городской машины ограничение скорости 60 км/ч
    _speedlimit = 60    # но нет розыска при привышении скорости
    _is_police = False
    def show_speed(self):
        if self.speed > self._speedlimit:
            print(f'{self.color} {self.name} движется со скоростью {self.speed} км/ч, превышение: {self.speed - self._speedlimit} км/ч')
        else:
            print(f'{self.color} {self.name} движется со скоростью {self.speed} км/ч')