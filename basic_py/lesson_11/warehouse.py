class Warehouse:
    def __init__(self, capacity, security):
        self.capacity = capacity
        self.security = security

    def __str__(self):
        return f'Вместимость {self.capacity}, охрана: {self.security}'

    def receive(self, department, types, name, amount):
        args = [department, types, name, amount]
        if Warehouse.valid(*args):
            self.capacity -= amount
            products = f'Подразделение: {department}\n  Тип: {types}\n  Наименование: {name}\n  Количество: +{amount}'
            return products
        else:
            raise ValueError('Неверный формат данных')

    def sale(self, department, types, name, amount):
        args = [department, types, name, amount]
        if Warehouse.valid(*args):
            self.capacity += amount
            products = f'Подразделение: {department}\n  Тип: {types}\n  Наименование: {name}\n  Количество: -{amount}'
            return products
        else:
            raise ValueError('Неверный формат данных')

    @staticmethod
    def valid(department, types, name, amount):
        if department == 'Первое' or department == 'Второе' or department =='Третье':   # у нас всего три подразделения
            if types == 'Принтеры' or types == 'Сканеры' or types == 'Ксероксы':        # и только данные типы техники
                if type(amount) is int:
                    return True
        return False

class Orgtech:
    def __init__(self, price, color, name):
        self.price = price
        self.color = color
        self.name = name

    def __str__(self):
        return f'Цена: {self.price}\n Модель: {self.name}\n Цвет: {self.color}'

class Printer(Orgtech):
    def __init__(self, price, color, model, print_technology, speed):
        super().__init__(price, color, model)
        self.print_technology = print_technology
        self.speed = speed

class Scanner(Orgtech):
    def __init__(self, price, color, model, resolution, scan_format):
        super().__init__(price, color, model)
        self.resolution = resolution
        self.scan_format = scan_format

class Copier(Orgtech):
    def __init__(self, price, color, model, max_format, scaling):
        super().__init__(price, color, model)
        self.max_format = max_format
        self.scaling = scaling