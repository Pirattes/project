from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


my_list = [el for el in range(100, 1001, 2)]
print(f'Произведение элементов списка {my_list}\nравно очень большому числу: {reduce(my_func, my_list)}')


