class MyZero(Exception):
    pass

num = input('Числитель: ')
denom = input('Знаменатель: ')
try:
    numerator = int(num)
    denomerator = int(denom)
    if denomerator == 0:
        raise MyZero('На 0 делить нельзя')
except (ValueError, MyZero) as err:
    print(err)
else:
    print(numerator/denomerator)