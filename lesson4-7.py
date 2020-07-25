from math import factorial


def func_fact():
    n = int(input('Введите число: '))
    yield [factorial(el) for el in range(1, n + 1)]


for i in func_fact():
    print(i)
