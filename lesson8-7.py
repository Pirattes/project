class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def comlex_num(self):
        num = complex(self.a, self.b)
        return num

    def __add__(self, other):
        self.a = self.a + other.a
        self.b = self.b + other.b
        return self.a, self.b

    def __mul__(self, other):
        self.a = self.a * other.a - self.b * other.b
        self.b = self.a * other.b + self.b * other.a
        return self.a, self.b


a = Complex(3, 1)
b = Complex(2, -3)
print(a.comlex_num())
print(b.comlex_num())
print(a.comlex_num() + b.comlex_num())
print(a.comlex_num() * b.comlex_num())
