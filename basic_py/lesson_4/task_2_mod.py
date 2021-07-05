from requests import api

def currency_rates():
    #user_charcode = arg.upper()
    url_list = api.get("http://www.cbr.ru/scripts/XML_daily.asp").text.split('><')
    char_val = {}
    valute_list = []
    for el in url_list:
        if el.find('CharCode') != -1:
            charcode = el[9:-10]
            valute_list.append(charcode)
        elif el.find('Value') != -1:
            valute_value = float(el[6:-7].replace(',', '.'))
            valute_list.append(valute_value)
        elif el.find('Name') != -1:
            valute_name = el[5:-6]
            char_val[valute_name] = char_val.get(valute_name, []) + [valute_list]


    print(char_val)

currency_rates()

