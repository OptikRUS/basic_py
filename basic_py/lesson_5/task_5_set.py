import sys
from time import perf_counter

start = perf_counter()
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_set = set()
tmp = set()

for i in src:
   if i not in tmp:
       unique_set.add(i)
   else:
       unique_set.discard(i)
   tmp.add(i)

unique_list = list(unique_set)
unique_list.sort(key=src.index)

print(unique_list, type(unique_list), sys.getsizeof(unique_list), perf_counter() - start)