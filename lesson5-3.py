with open('text_3.txt','r',encoding='utf-8') as sal_emp:
    content=sal_emp.readlines()

    sum_zp=0
    for i in content:
        i = i.replace('/n', '')
        item = i.split()
        sum_zp+=float(item[1])

        if float(item[1]) <20000.00:
            print(f'сотрудник {item[0]} имеет зарплату меньше 20000.00, а именно {float(item[1])}')
    print(f'Средняя зарплата по фирме составляет {sum_zp/len(content)}')

