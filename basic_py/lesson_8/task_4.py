def val_checker(condition):
    def _val_checker(func):
        def wrapper(num):

            if condition(num):
                res = func(num)
                print(res)
            else:
                raise ValueError(f'wrong val {num}')

        return wrapper
    return _val_checker

@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

a = calc_cube(5)