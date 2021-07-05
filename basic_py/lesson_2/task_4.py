#Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
my_list = ['a', '1', 'b', 'c', '2', 'd', '-3']
for i in range(len(my_list)):
    if my_list[i].isdigit() or not my_list[i].isalnum():
        print(f'{int(my_list[i]):+.0f}')

#Дан список, содержащий искажённые данные с должностями и именами сотрудников:
worklist = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for name in range(len(worklist)):
    name = worklist[name][worklist[name].rfind(' ')+1:].title()
    print(f'Привет, {name}!')

# ещё один вариант
for name in worklist:
    name = name.split(' ')[-1].title()
    print(f'Привет, {name}!')