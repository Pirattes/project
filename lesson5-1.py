try:
    user_file=input('Введите название файла куда будем сохранять данные: ')

    with open(user_file, 'x', encoding='utf-8') as obj_:
        lst = []
        while True:

            str_ = input('Введите строки через Enter,для окончания записи просто нажмите Enter: ')
            if str_ != '':
                lst.append(str_+'\n')

            else:
                obj_.writelines(lst)
                break
    print(f'Файл c вашим текстом сформирован! Просмотрите {user_file}')
    print (f'Количество строк в файле {len(lst)}')
    for i,n in enumerate(lst,1):
        n=n.split()
        print(f'Количество слов в {i} строке равно {len(n)}')

except IOError:
    print('Такой файл уже существует')


