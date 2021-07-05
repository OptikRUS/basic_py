class NotInt(Exception):
    pass

my_list = []
el = None
while el != 'stop':
    try:
        el = input('Добавиль элемент списка: ')
        if el.isdigit():
            my_list.append(el)
        else:
            raise NotInt(f'Не удалось добавить элемент. Можно вводить только числа. \nСписок \n{my_list}')
    except NotInt as err:
        print(err)
print(f'Полученный список \n{my_list}')