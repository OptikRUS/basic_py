import sys, csv

if __name__ == '__main__':
    sale = [sys.argv[1]]
    with open('bakery.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(sale)
    exit()