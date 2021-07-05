# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и
# возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы. Например:

def thesaurus(*args):
    namelist = list(map(str, args))
    dict_names = {}
    for name in namelist:
        first_letter = name[0]
        dict_names[first_letter] = dict_names.get(first_letter, []) + [name] # в словаре ищет ключ равный Первой букве
    return print(dict_names)

thesaurus("Артур", "Артём", "Иван", "Мария", "Петр", "Илья", "Михаил", "Григорий", "Георгий")