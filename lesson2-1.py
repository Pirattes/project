my_list = [55, 7, 6.3, True, [1, 2], 'age', (5, 6, 8), {1, 2, 9}]
for i, val in enumerate(my_list, 1):
    print(f'{i} - {val} -  {type(val)}')
