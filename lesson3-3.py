def func_sum(a, b, c):
    res = sum([a, b, c]) - min([a, b, c])
    return res


a1 = int(input('Введите первое целое число '))
b1 = int(input('Введите второе целое число '))
c1 = int(input('Введите третье целое число '))
print(f'Суммой двух наибольших чисел среди  {a1}, {b1}, {c1}  является {func_sum(a1, b1, c1)}')
