# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
import os

listdir = ['settings', 'mainapp', 'adminapp', 'authapp']

for dir in listdir:
    if not os.path.exists(dir):
        os.makedirs(f'my_project/{dir}')