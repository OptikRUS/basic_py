# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы
# слов в шутках (когда каждое слово можно использовать только в одной шутке)

from random import randrange

def get_jokes(n, repeat):
    joke_list = []
    if repeat == True:
        for joke in range(n):
            rand_num_nouns = randrange(len(nouns))
            rand_num_adv = randrange(len(adv))
            rand_num_adj = randrange(len(adj))
            joke = ' '.join([nouns.pop(rand_num_nouns), adv.pop(rand_num_adv), adj.pop(rand_num_adj)])
            joke_list.append(joke)
        print(joke_list)
    else:
        for joke in range(n):
            joke = ' '.join([nouns[randrange(len(nouns))], adv[randrange(len(adv))], adj[randrange(len(adj))]])
            joke_list.append(joke)
        print(joke_list)

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adv = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adj = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

"""
True - повторы запрещены
False - повторы разрешены
"""

get_jokes(5, True)