with open('1.txt', 'w+', encoding='utf-8') as gener_file:
    try:
        new_numb = input('Введите числа через пробел: ')
        gener_file.write(new_numb)
        gener_file.seek(0)
        dig = gener_file.read()

        int_dig = dig.split()
        result = [int(item) for item in int_dig]
        print(f' Сумма чисел в файле 1.txt {sum(result)}')
    except ValueError:
        print('Введите именно цифры')
