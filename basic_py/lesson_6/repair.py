import sys

if __name__ == '__main__':
        n, num = sys.argv[1:]
        with open('bakery.csv', 'r+', encoding='utf-8') as f:
                for line in range(int(n) - 1):
                        line = f.readline().strip()
                f.seek(f.tell())
                f.write(num)
        print(f'значение № {n} заменено на {num}')
        exit()