import sys
from time import perf_counter

start = perf_counter()
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_list = [i for i in src if src.count(i) == 1]

print(unique_list, type(unique_list), sys.getsizeof(unique_list), perf_counter() - start)