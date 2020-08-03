class MyOwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


a = input('Введите делимое: ')
b = input('Введите делитель: ')
try:
    a, b = int(a), int(b)
    c = a / b
    print(c)
    if b == 0:
        raise MyOwnError('Деление на ноль невозможно!')
except (ValueError, MyOwnError) as err:
    print(err)
