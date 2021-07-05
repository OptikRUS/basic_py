a = []                      # создаём пустой список
for i in range(1000):       # цикл генерирующий список от 1 до 1000
    if i % 2 != 0:          # добавляем в него только нечётные числа
        a.append(i ** 3)    # добавляем нечётное число в список a и возводим это число в куб
print(a)

for i in range(len(a)):
    a[i] += 17
print(a)

sum = 0
for num in a:
    i = num
    while num != 0:
        sum += num % 10
        num = num // 10
    if sum % 7 == 0:
        a[a.index(i)] = i
    sum = 0
print(a)

#142, 1367648, 1860884, 3581594, 4019696, 6751286, 7414892