def func_exp(a, b):
    if a <= 0 or b >= 0:
        return f'Вы ошиблись! Введите одно действительное положительное число и одно целое отрицательное'
    else:
        c = 1 / (a ** abs(b))
        return c


def func_exp1(a, b):
    if a <= 0 or b >= 0:
        return f'Вы ошиблись! Введите одно действительное положительное число и одно целое отрицательное'
    else:
        i = 1
        c = 1 / abs(a)
        while i < abs(b):
            c = c / abs(a)
            i += 1
    return c


try:
    a_user = float(input('Введите действительное положительное число '))
    b_user = int(input('Введите целое отрицательное число '))
    print(func_exp(a_user, b_user))
    print(func_exp1(a_user, b_user))
except ValueError:
    print('Введите именно числа!')
