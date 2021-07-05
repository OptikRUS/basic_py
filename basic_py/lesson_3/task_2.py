# Доработать предыдущую функцию в num_translate_adv(): реализовать
# корректную работу с числительными, начинающимися с заглавной буквы — результат тоже
# должен быть с заглавной.

def num_translate_adv():
    number = input('Введите число на англ: ')
    if number.isdigit():
        num = {}
        for key, val in enumerate(numbers.values(), 1): # заполняем новый словарь num = {1: один ....}
            num[key] = val
        print(num.get(int(number)).title())
    elif number.istitle():
        number = numbers.get(number.lower()).title()
        print(number)
    else:
        print(numbers.get(number))

numbers = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}

num_translate_adv()