import sys

if __name__ == '__main__':
    sale = sys.argv[1]
    with open('bakery.csv', 'a') as f:
        f.write(sale + '\n')
    exit()