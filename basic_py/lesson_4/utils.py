from datetime import datetime
from requests import api

def currency_rates(arg):
    user_charcode = arg.upper()
    url_list = api.get("http://www.cbr.ru/scripts/XML_daily.asp").text.split('><')
    date_server_string = api.get("http://www.cbr.ru/scripts/XML_daily.asp").headers['Date']
    date_server = datetime.strptime(date_server_string, '%a, %d %B %Y %H:%M:%S %Z')
    char_val = {}
    for el in url_list:
        if el.find('CharCode') != -1:
            charcode = el[9:-10]
        elif el.find('Value') != -1:
            valute_value = float(el[6:-7].replace(',', '.'))
            char_val[charcode] = valute_value

    print(f'Курс {user_charcode} = {char_val.get(user_charcode)} на {date_server}')