class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ''
        for row in self.matrix:
            for i in row:
                result += f'{i} '
            result += '\n'
        return result

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix):
            rows = len(self.matrix)
            columns = len(self.matrix[0])
            result = []
            for n in range(rows):
                result.append([])
                for m in range(columns):
                    result[n].append(self.matrix[n][m] + other.matrix[n][m])
            return Matrix(result)
        else:
            raise ValueError ('Неверный формат матриц')

matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)