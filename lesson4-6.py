from itertools import count, cycle


def func_1():
    while True:

        c = int(input(
            'С какого числа начать от одного до девяти? Будут по порядку вводиться числа до 10 и повторяться три раза: '))
        if c < 10:
            for i in count(c):
                if i != 11:
                    yield i
                else:
                    return i

        else:
            continue


def func_2():
    lst = []
    c = 0

    for i in func_1():
        lst.append(i)

    for el in cycle(lst):

        if c > len(lst) * 3 - 1:
            break
        print(el)
        c += 1


func_2()
