with open('text_6.txt','r',encoding='utf-8') as lessons:
    user_dict = dict()
    for stroka in lessons: #перебор строк из файла
        stroka=stroka.split() #перевод очередной строки в список
        # print(stroka)
        # print(stroka[0])

        dig={stroka[0]: el  for el in stroka if el[0].isdigit()} #выделение элементов списка, который начинается с числа
        print(dig)



        print(dig)
        for sl in dig: #перебор
            slovo1=str()
            for i in sl:
                if i.isdigit():
                    slovo1+=i

                else:
                    break
        user_dict[stroka[0]]=slovo1
    print(user_dict)

