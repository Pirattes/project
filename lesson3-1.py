def func_div(a, b):
    try:
        a = int(a)
        b = int(b)
        c = a / b
        return print(c)
    except ValueError:
        return print('Введите именно числа!')
    except ZeroDivisionError:
        print('На ноль делить нельзя!')


a1 = input('первое ')
b1 = input('второе ')
func_div(a1, b1)
