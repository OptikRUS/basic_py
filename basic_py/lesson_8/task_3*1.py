# если аргументов несколько - выводить данные о каждом через запятую

def type_logger(func):
    def wrapper(*args):
       for num in args:
           print(num, type(num), end=', ')
    return wrapper

@type_logger
def calc_cube(x):
    return x ** 3

a = calc_cube(5, 6.5, '7')