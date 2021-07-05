from time import sleep

class TrafficLight:
    __color = ['Красный', 'Жёлтый', 'Зелёный']
    count = 1

    def running(self, n):
        repeat = 0
        while repeat != n:
            for TrafficLight.count in range(1, 4):
                print(f'{TrafficLight.__color[TrafficLight.count - 1]}')
                if TrafficLight.count == 1:
                    sleep(7)
                elif TrafficLight.count == 2:
                    sleep(2)
                elif TrafficLight.count == 3:
                    sleep(10)
                TrafficLight.count += 1
            repeat += 1

    def checklight(self, n):
        try:
            if n > 0:
                print(f'Будет {TrafficLight()._TrafficLight__color[n % 3 - 1]} цвет')
            else:
                print('Светофор выключен!')
        except:
            print(f'Должно быть целое число, а не {n}')