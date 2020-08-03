class MyOwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def num():
    in_list = []
    while True:
        num = input('Введите целое число, для окончания формирования списка введите stop: ')
        if num == 'stop':
            return in_list
        else:
            try:

                if not num.isdigit() :
                    raise MyOwnError('Вводим только целые числа!')
                in_list.append(int(num))
            except MyOwnError as err:
                print(err)


print(num())
