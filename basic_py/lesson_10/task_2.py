from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, H, V):
        self.H = H
        self.V = V

    def __str__(self):
        return f'Нужно {self.expense} ткани'

    def __add__(self, other):
        return f'Всего нужно {self.expense + other.expense} ткани'

    @abstractmethod
    def expense(self):
        pass

class Suit(Clothes):
    @property
    def expense(self):
        return 2 * self.H + 0.3

class Coat(Clothes):
    @property
    def expense(self):
        return self.V / 6.5 + 0.5

coat = Coat(50, 1.75)
suit = Suit(50, 1.75)
print(coat)
print(suit)
print(coat + suit)