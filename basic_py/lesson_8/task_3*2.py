# Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

def type_logger(func):
    def wrapper(num):
        print (f'{func.__name__}({num}: {type(num)}')
    return wrapper

@type_logger
def calc_cube(x):
    return x ** 3

a = calc_cube(5)