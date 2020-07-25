my_list = list(input('Введите через пробел список элементов: ').split())
print(f'Было {my_list}')

for i in range(0, len(my_list) - 1, 2):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(f'Стало {my_list}')
