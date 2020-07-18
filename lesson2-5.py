user_list = [7, 5, 3, 3, 2]
number = int(input('Введите целов число: '))
i = 0
for n in user_list:
    if number <= n:
        i += 1
user_list.insert(i, float(number))
print(user_list)
