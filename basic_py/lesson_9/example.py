"""Здесь примеры использования классов из заданий"""
from trafficlight import TrafficLight
from road import Road
from worker import Position
from cars import TownCar
from stationery import Pen

# 1 задача со светофором
traffic_light = TrafficLight()
traffic_light.running(1)
traffic_light.checklight(0)

# 2 задача с дорогой
my_road = Road(5000, 20)
my_road.count_mass(5)

# 3 задача с сотрудником
me = Position('Optik', 'RUS', 'Chief Of CG', 900, 200)
me.get_full_name()
print(me.name, me.surname)
print(me.position)
me.get_total_income()

# 4 задача с машинами
kia = TownCar(60, 'Белая', 'Kia Optima', False)
kia.go()
kia.turn('вперёд')
kia.show_speed()
kia.show_bool()
kia.speed = 90
kia.show_speed()
kia.show_bool()
kia.stop()

# 5 задача с письменными принадлежностями
pen = Pen('Ручка')
pen.draw()