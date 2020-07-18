user_str = input('Введите строку разделенную пробелами').split()
for i, n in enumerate(user_str, 1):
    print(f'{i} {n[:10]}')
