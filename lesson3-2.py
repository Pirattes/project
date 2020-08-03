def func_data(name, lastname, bday, city, email, phone):
    return f'Информация о пользователе: имя: {name}, фамилия: {lastname}, день рождения: {bday}, город проживания: {city}, email: {email}, телефон: {phone}'


print(func_data(bday='09.02.80', email='pirat@aa.ru', lastname='Kosmin', phone='92272772', name='Pavel', city='Moscow'))
