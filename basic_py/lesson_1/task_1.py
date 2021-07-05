time = int(input('Веедите количество секунд: '))

seconds = time % 60
minutes = time // 60 % 60
hours = time // 3600 % 24
days = time // 86400 % 24

print(f'{days} д {hours} ч {minutes} мин {seconds} сек')