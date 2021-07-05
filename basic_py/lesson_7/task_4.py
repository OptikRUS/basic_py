# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,но больше предыдущей (начинаем с 0)

import os

for root, dirs, files in os.walk('some_data'):
    size_100000 = [file for file in files if os.stat(os.path.join(root, file)).st_size > 10000]
    size_10000 = [file for file in files if 1000 < os.stat(os.path.join(root, file)).st_size < 10000]
    size_1000 = [file for file in files if 100 < os.stat(os.path.join(root, file)).st_size < 1000]
    size_100 = [file for file in files if os.stat(os.path.join(root, file)).st_size < 100]

print({100000: len(size_100000), 10000: len(size_10000), 1000: len(size_1000), 100: len(size_100)})