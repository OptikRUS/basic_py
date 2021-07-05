# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или
# «руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку
# templates, например:
import os, shutil

folder = 'my_project'
dst = 'my_project/templates'

for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith('.html'):
            path = os.path.split(root)[0]
            shutil.copytree(path, dst, dirs_exist_ok=True)