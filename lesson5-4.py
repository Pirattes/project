with open('text_4.txt', 'r', encoding='utf-8') as eng_file:
    with open('rus_file.txt', 'w', encoding='utf-8') as rus_file:
        rus_dict = {'1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре'}
        for i in eng_file:
            i = i.split()
            i[0] = rus_dict.get(i[-1])
            i[-1] += '\n'

            rus_file.writelines(i)

    print(f'Русские числительные сохранены в файле "rus_file.txt"')
