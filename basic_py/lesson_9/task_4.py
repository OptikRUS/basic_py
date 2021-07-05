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

truck = WorkCar(40, 'Чёрный', 'Мусоровоз', False)
truck.go()
truck.turn('налево')
truck.show_speed()
truck.show_bool()
truck.speed = 59 # изменение скорости мусоровоза
truck.show_speed()
truck.speed = 60
truck.show_bool()
truck.show_speed()
truck.speedlimit = 70 # без _ не меняет лимит скорости
truck.show_bool()
truck.turn('прямо')
truck.speed = 70
truck.show_speed()
truck.stop()
print()

mercedes = TownCar(60, 'Белый', 'Mercedes', False)
mercedes.go()
mercedes.turn('назад')
mercedes.show_speed()
mercedes.show_bool()
mercedes.turn('вперёд')
mercedes.speed = 100
mercedes.show_speed()
mercedes.show_bool()
mercedes.stop()
print()

lamborghini = SportCar(150, 'Жёлтая', 'Lamborghini Aventador', False)
lamborghini.go()
lamborghini.show_speed()
lamborghini.show_bool()
lamborghini.turn('вперёд')
lamborghini.speed = 250
lamborghini.show_speed()
lamborghini.show_bool()
lamborghini.stop()
print()

police = PoliceCar(60, 'Бело-синий', 'Ford Crown Victoria', False)
police.go()
police.show_speed()
police.show_bool()
police.speed = 100
police.show_speed()
police.show_bool()
police.stop()