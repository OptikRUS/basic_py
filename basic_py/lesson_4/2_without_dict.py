from requests import api

url_list = api.get("http://www.cbr.ru/scripts/XML_daily.asp").text.split('><')
user_charcode = input('Введи код валюты: ').upper()
valute_value = None

for el in url_list:
    if el == f'CharCode>{user_charcode}</CharCode':
        idx_of_el = url_list.index(el)
        valute_value = url_list[idx_of_el + 3][6:-7].replace(',', '.')

if valute_value == None:
    print(None)
else:
    print(float(valute_value))