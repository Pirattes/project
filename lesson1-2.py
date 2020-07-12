my_seconds = int(input('Введите время в секундах: '))
if my_seconds < 360000:
    hours = "%02d" % (my_seconds // 3600)
    minutes = "%02d" % ((my_seconds % 3600) // 60)
    seconds = "%02d" % ((my_seconds % 3600) % 60)
    print(f'{hours}:{minutes}:{seconds}')
else:
    print('Попробуйте ввести в следующий раз поменьше секунд')
