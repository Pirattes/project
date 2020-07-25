user_number = int(input('Введите целое число: '))
max_number = 0
while user_number != 0:
    number = user_number % 10
    user_number = user_number // 10
    if number > max_number:
        max_number = number
print(f'Максимальная цифра в заданном числе {max_number}')
