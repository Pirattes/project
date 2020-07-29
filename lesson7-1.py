class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        sum_ = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in
                range(len(self.matrix))]
        return Matrix(sum_)

    def __str__(self):
        list_str = ''
        for stroka in self.matrix:
            bad_chars = ["[", "]", "'", ","]
            list_str += '    '.join(str(n) for n in stroka if not n in bad_chars) + '\n'
        return list_str


matrix = Matrix([[1, 2,5], [3, 4,5], [5, 6,6]])
matrix1 = Matrix([[5, 6,1], [7, 8,4], [9, 10,3]])

print(matrix + matrix1)
