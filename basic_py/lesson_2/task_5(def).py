def cost(prices):
    for p in prices:
        print(f'{int(p):02d} руб {int(p * 100 % 100):02d} коп', end=', ')

prices = [4.5, 5.45, 3.74, 7.93, 1.25, 7.5, 3, 4.8, 0.74, 57.8, 46.51, 97, 195.74, 76.68, 92.45]

cost(prices)

# *Создать новый список, содержащий те же цены, но отсортированные по убыванию.
print('\nСортировка по убыванию:')
cost(sorted(prices, reverse=True))

# * Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
print('\nПять самых дорогих товаров:')
cost(sorted(prices)[-5:])