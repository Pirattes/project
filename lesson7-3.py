class Org_cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        return self.cell - other.cell if (self.cell - other.cell) >= 0 else 'Ошибка, получается отрицательное число'

    def __mul__(self, other):
        return self.cell * other.cell

    def __truediv__(self, other):
        return round(self.cell / other.cell) if other.cell != 0 else 'Число клеток не может равняться нулю'

    def make_order(self, row):
        str_ = ''
        while len(str_) < self.cell:
            str_ += row * '*' + '\n'
        str_ += '*' * (self.cell % row)
        return str_


cell_1 = Org_cell(20)
cell_2 = Org_cell(0)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(3))
