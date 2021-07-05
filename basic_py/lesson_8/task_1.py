# Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя
# и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден,
# выбросить исключение ValueError.

def email_parse(email):
    import re
    check = re.match(r'\w+\@\w+\.\w+', email)
    if check:
        pars = re.split(r'@', email)
        print({'username': pars[0], 'domain': pars[1]})
    else:
        raise ValueError(f'wrong email: {email}')

email_parse('someone21@geekbrains.ru')