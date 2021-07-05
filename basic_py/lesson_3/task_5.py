# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех
# случайных слов, взятых из трёх списков (по одному из каждого):

from random import randrange

def get_jokes(n):
    joke_list = []
    for joke in range(n):
        joke = ' '.join([nouns[randrange(len(nouns))], adv[randrange(len(adv))], adj[randrange(len(adj))]])
        joke_list.append(joke)
    print(joke_list)

nouns = ["автомобиль", "лес", "огонь", "город", "дом", "столб", "монитор"]
adv = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "днём", "послезавтра"]
adj = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "красный", "грустный"]

get_jokes(3)