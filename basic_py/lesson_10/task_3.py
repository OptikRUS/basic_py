class Cell:
    def __init__(self, block):
        self.block = int(block)

    def __add__(self, other):
        return self.block + other.block

    def __sub__(self, other):
        return self.block - other.block if self.block - other.block > 0 else "Ошибка"

    def __mul__(self, other):
        return self.block * other.block

    def __floordiv__(self, other):
        return self.block // other.block

    def make_order(self, row):
        block_row = self.block // row
        res = ''
        for i in range(block_row):
            res += '*' * row + '\n'
        return res + '*' * (self.block % row)

cell_1 = Cell(29)
cell_2 = Cell(17)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1.make_order(5))