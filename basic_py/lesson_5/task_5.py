# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке
import sys
from time import perf_counter

start = perf_counter()
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

i = 0
unique_list = []
while i != len(src):
    if src.count(src[i]) == 1:
        unique_list.append(src[i])
    i+=1

print(unique_list, type(unique_list), sys.getsizeof(unique_list), perf_counter() - start)