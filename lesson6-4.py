class Car:
    def __init__(self, name, color, ispolice):

        self.color = color
        self.name = name
        self.ispolice = ispolice

    def go(self):
        return 'в движении'

    def stop(self):
        return 'остановилась'

    def turn(self, direction):
        if direction == '<':
            return print('повернула влево')
        elif direction == '>':
            return print('повернула вправо')

    def show_speed(self, speed):
        return print(f'едет со скоростью {speed} км/ч')


class TownCar(Car):
    def __init__(self, name, color, ispolice):
        super().__init__(name, color, ispolice)

    def show_speed(self, speed):
        if speed < 60:
            return print(f'едем со скоростью  {speed} км/ч')
        else:
            return print(f'Ваша скорость {speed} км/ч, снизьте ее до 60 км/ч')


class WorkCar(Car):
    def __init__(self, name, color, ispolice):
        super().__init__(name, color, ispolice)

    def show_speed(self, speed):
        if speed < 40:
            return print(f'едем со скоростью {speed} км/ч')
        else:
            return print(f'Ваша скорость {speed} км/ч, снизьте ее до 40 км/ч')


class SportCar(Car):
    def __init__(self, name, color, ispolice):
        super().__init__(name, color, ispolice)


class PoliceCar(Car):
    def __init__(self, name, color, ispolice):
        super().__init__(name, color, ispolice)
        print('Это полицейская машина')


def car_func(obj):
    move = None
    while move != 'q':
        move = input(
            'Если хотите двигаться вперед наберите go,повернуть turn, остановиться stop, набрать скорость speed, для выхода нажмите q ')
        if move == 'go':
            print(f' {obj.color} {obj.name} {obj.go()}')
        elif move == 'stop':
            print(f' {obj.color} {obj.name} {obj.stop()}')
        elif move == 'turn':
            obj.turn(input('нажмите < или > '))
        elif move == 'speed':
            obj.show_speed(int(input('Введите скорость, какую надо набрать: ')))


my_car = input('Введите какая у вас машина: T-городская, W-рабочая, S-спортивная, P-полицейская: ')
if my_car == 'T':
    my_towncar = TownCar(input('my_car.name '), input('my_car.color '), bool(input('ispolice, "Enter" if not ')))
    if my_towncar.ispolice is True:
        print('У Вас городская, а не полицейская машина!')
    car_func(my_towncar)

elif my_car == 'W':
    my_workcar = WorkCar(input('my_car.name '), input('my_car.color '), bool(input('ispolice, "Enter" if not ')))
    if my_workcar.ispolice is True:
        print('У Вас рабочая, а не полицейская машина!')
    car_func(my_workcar)
elif my_car == 'S':
    my_sportcar = SportCar(input('my_car.name '), input('my_car.color '), bool(input('ispolice, "Enter" if not ')))
    if my_sportcar.ispolice is True:
        print('У Вас спортивная, а не полицейская машина!')
    car_func(my_sportcar)
elif my_car == 'P':
    my_policecar = PoliceCar(input('my_car.name '), input('my_car.color '),
                             bool(input('ispolice, "Enter" if not ')))
    if my_policecar.ispolice is False:
        print('Вы ошиблись, у Вас полицейская машина!')
    car_func(my_policecar)
