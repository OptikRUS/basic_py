# Написать декоратор для логирования типов позиционных аргументов функции

def type_logger(func):
    def wrapper(num):
        res = func(num)
        print(f'{num}: {type(num)}')
    return wrapper

@type_logger
def calc_cube(x):
    return x ** 3

a = calc_cube(5)