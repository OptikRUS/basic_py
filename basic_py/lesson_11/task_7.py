# Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число».
# Реализовать перегрузку методов сложения и умножения комплексных чисел.
# Проверить работу проекта. Для этого создать экземпляры класса (комплексные числа), выполнить сложение и умножение созданных экземпляров.
# Проверить корректность полученного результата.

class MyComplex:
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return MyComplex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return MyComplex(self.real * other.real - self.imag * other.imag, self.imag * other.real + self.real * other.imag)

    def __str__(self):
        return f'({self.real} + i{self.imag})' if self.imag >= 0 else f'{self.real} - i{abs(self.imag)}'

c1 = MyComplex(1, 2)
c2 = MyComplex(2, 3)
print(c1)
print(c2)
print(c1 + c2)
print(c1 * c2)