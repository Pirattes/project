user_number = input('Введите числа через пробел: ')
# new_number =[]
'''for i in range(0,len(user_number),2):
    if user_number[i].isdigit() is True and ord(user_number[i+1]) == 45:
        new_number=user_number[i]+user_number[i+1]
    else:
        user_number=input('Введите числа через пробел еще раз: ')
print(user_number)'''


def sum_func(numb):
    n = 0
    while n < len(numb):
        try:
            for i in range(1, len(numb) // 2, 2):
                if ord(numb[i]) == 32:
                    n += 1
                else:
                    print('что то не то')
                    numb = input('введите заново')
        except ValueError:
            numb = input('введите правильно')
    numb = numb.split()
    result = [int(item) for item in numb]
    return sum(result)


print(sum_func(user_number))
