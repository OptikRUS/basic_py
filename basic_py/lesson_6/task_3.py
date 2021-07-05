from itertools import zip_longest
import json

with open('users.csv', 'r', encoding='utf-8') as name,\
        open('hobby.csv', 'r', encoding='utf-8') as hobby:
            names = name.read().splitlines()
            hobbys = hobby.read().splitlines()

if len(names) < len(hobbys):
    print(1)
else:
    users_hobby = dict(zip_longest(names, hobbys, fillvalue=None))
    with open('users_hobby_dict(3_задание).txt', 'w') as f:
        json.dump(users_hobby, f, ensure_ascii=False)