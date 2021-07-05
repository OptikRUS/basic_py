a = []                      # создаём пустой список
for i in range(1000):       # цикл генерирующий список от 1 до 1000
    if i % 2 != 0:          # добавляем в него только нечётные числа
        a.append(i ** 3)    # добавляем нечётное число в список a и возводим это число в куб
print(a)

b = []
sum = 0
for num in a:
    i = num
    while num != 0:       # цикл, который считает сумму цифр числа
        sum += num % 10
        num = num // 10
    if sum % 7 == 0:        # если сумма цифр числа делется на 7, то число добавляется в список b
        b.append(i)
    sum = 0
print(b)

c = []
sum = 0
for num in a:
    num += 17
    i = num
    while num != 0:
        sum += num % 10
        num = num // 10
    if sum % 7 == 0:
        c.append(i)
    sum = 0
print(c)