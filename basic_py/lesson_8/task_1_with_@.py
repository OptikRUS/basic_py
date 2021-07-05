def valid(func):
    def wrapper(*args):
        import re
        check = re.match(r'\w+\@\w+\.\w+', *args)
        if check:
            pars = func(*args)
            result = {'username': pars[0], 'domain': pars[1]}
            print(result)
        else:
            raise ValueError(f'wrong email')
    return wrapper

# декоратор для наглядности показывает, что можно в нём преобразовать в словарь и отфильтровать
@valid
def email_parse(email):
    import re
    name_domain = re.split(r'@', email)
    return name_domain[0], name_domain[1]

email_parse('someone21@geekbrains.ru')