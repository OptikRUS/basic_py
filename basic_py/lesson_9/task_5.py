class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pen(Stationery):
    def draw(self):
        print(f'{self.title} пишет')

class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} рисует')

class Handle(Stationery):
    def draw(self):
        print(f'{self.title} выделяет')

write = Stationery('фломастером')
write.draw()

pen = Pen('Ручка')
pen.draw()

pencil = Pencil('Карандаш')
pencil.draw()

handle = Handle('Маркер')
handle.draw()