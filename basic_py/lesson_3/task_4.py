# Написать функцию thesaurus_adv(), принимающую в качестве аргументов
# строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы
# фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие
# записи, в которых фамилия начинается с соответствующей буквы.

def thesaurus_adv(*args):
    namelist = list(map(str, args))
    dict_surnames = {}
    dict_main = {}
    for name in namelist:
        surname = name.split(' ')[-1].title()
        first_letter_surname = surname[0]
        dict_surnames[first_letter_surname] = dict_surnames.get(first_letter_surname, []) + [name]
    for namelist in dict_surnames.values():
        dict_names = {}
        for name in namelist:
            surname = name.split(' ')[-1].title()
            first_letter_surname = surname[0]
            first_letter = name[0]
            dict_names[first_letter] = sorted(dict_names.get(first_letter, []) + [name])
            dict_main[first_letter_surname] = dict_main.get(first_letter_surname, dict_names)
    return print(dict(sorted(dict_main.items()))) # сортировка по ключам

thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Иван Афанасьев", "Дмитрий Уланов", "Петр Илямаков")