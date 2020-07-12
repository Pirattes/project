month = int(input('введите месяц от 1 до 12: '))
season = ['зима','весна','лето', 'осень']
dict_season
if month< 3 or month==12:
    print(f'Это {season[0]}')
elif month>2 and month<6:
    print(f'Это {season[1]}')
elif month >5 and month<9:
    print(f'Это {season[2]}')
elif month>8 and month<12:
    print(f'Это {season[2]}')
else:
    print('Введите целое число от 1 до 12, будьте внимательны ')
