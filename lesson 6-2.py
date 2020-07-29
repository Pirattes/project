class Road:
    def __init__(self,_length, _width):
        self._length = _length  # заводим атрибут длина дороги, к примеру 5000 метров
        self._width = _width  # заводим атрибут ширина дороги, к примеру 20 метров

    def mass(self):
        # заводим в методе массу асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см, к примеру 25 кг
        mass_square = int(input('Введите массу квадратного метра асфальта толщиной 1 см, кг: '))
        thickness_asph = int(input('Введите толщину асфальта, см: '))  # заводим в методе толщину асфальта, к примеру 5 см
        return f'Понадобится {((self._length * self._width * mass_square * thickness_asph) / 1000)} тонн асфальта'


obj_ = Road(int(input('Введите длину дороги,м: ')), int(input('введите ширину дороги,м: ')))

print(obj_.mass())
