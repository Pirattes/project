from pprint import pprint


class Store:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.my_store = []
        self.my_store_all = []

    def __str__(self):
        return f'Наименование:{self.name}, цена: {self.price}, количество: {self.quantity}'

    def reception(self):
        while True:
            try:
                unit = input(f'Введите наименование: ')
                unit_p = int(input(f'Введите цену за ед: '))
                unit_q = int(input(f'Введите количество: '))
                unit_a = input('Вид: ')
                unique = {f'Модель устройства': {unit}, 'Цена за ед': unit_p, 'Количество': unit_q, 'Вид': unit_a}
                self.my_store.append((unique))
                self.my_store_all.append(self.my_store)
                print(f'Текущий список:\n {unique}')
            except:
                return f'Ошибка ввода данных!'
            print(f'Для выхода - Q, продолжение - Enter')
            q = input(f'---: ')
            if q == 'Q' or q == 'q':
                for i, item in enumerate(self.my_store, 1):
                    print(f'{i}) {item}')
                print('Весь склад:')
                print('-------------------------------------', end='')
                print('--------------------------------')
                for i, item in enumerate(self.my_store_all, 1):
                    pprint(f'{i}) {item}')
                return f'Выход'
                break
            else:
                continue


class Printer(Store):
    def __init__(self, name, price, quantity, specifications):
        super().__init__(name, price, quantity)
        self.specifications = specifications

    def __str__(self):
        return f'Наименование:{self.name}, цена: {self.price}, количество: {self.quantity}, вид: {self.specifications}'

    def __del__(self):
        return 'Delete object - class Printer'


class Scanner(Store):
    def __init__(self, name, price, quantity, type):
        super().__init__(name, price, quantity)
        self.type = type

    def __del__(self):
        return 'Delete object - class Scanner'

    def __str__(self):
        return f'Наименование:{self.name}, цена: {self.price}, количество: {self.quantity}, описание: {self.type}'


class Copier(Store):
    def __init__(self, name, price, quantity, varieties):
        super().__init__(name, price, quantity)
        self.varieties = varieties

    def __str__(self):
        return f'Наименование:{self.name}, цена: {self.price}, количество: {self.quantity}, описание: {self.varieties}'

    def __del__(self):
        return 'Delete object - class Copier'


unit_1 = Printer('Принтер', 1500, 10, 'Цветной')
print(unit_1)
print(unit_1.reception())
unit_2 = Scanner('Сканер', 1200, 5, 10)
print(unit_2)
print(unit_2.reception())
unit_3 = Copier('Ксерокс', 1500, 1, 15)
print(unit_3)
pprint(unit_3.reception())
a_1 = Store('Print', 100, 10)
print(a_1)
