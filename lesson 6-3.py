class Worker:
    def __init__(self, name, surname, position):
        a_dict = {'зарплата': 100000, 'бонус': 50000}
        self.name = name
        self.surname = surname
        self.position = position
        self.income = a_dict.values()


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return sum(self.income)


a = Position(input('Введите имя: '), input('Введите фамилию: '), input('Введите должность: '))
print(f'{a.get_full_name()} в должности {a.position} с с общей зарплатой {a.get_total_income()} рублей')
