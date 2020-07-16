while True:
    month = input('введите месяц от 1 до 12: ')
    if month.isdigit() and 0 < int(month) <= 12:
        season_dic = {0: 'зима', 1: 'весна', 2: 'лето', 3: 'осень', 4: 'зима'}
        print(f'{season_dic[int(month) // 3]}')
        break
    else:
        print('Введите целое число от 1 до 12, будьте внимательны ')
