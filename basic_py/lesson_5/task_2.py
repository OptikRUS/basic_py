# *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
from itertools import islice

def odd_nums(n):
    num = (num for num in range(1, n + 1, 2))
    return num

odd_to_15 = odd_nums(15)

print(*islice(odd_to_15, 8))