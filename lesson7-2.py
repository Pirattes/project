from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, guant, h):
        self.guant = guant
        self.h = h

    @abstractmethod
    def fabric_consumption(self):
        pass

    def __add__(self, other):
        return self.fabric_consumption() + other.fabric_consumption


class Coat(Clothes):
    @property
    def fabric_consumption(self):
        return round(((self.h / 6.5 + 0.5) * self.guant), 2)


class Suit(Clothes):
    @property
    def fabric_consumption(self):
        return round(((2 * self.h + 0.3) * self.guant), 2)


w1 = Coat(int(input('Введите количество пальто: ')), int(input('Введите размер для пальто: ')))

w2 = Suit(int(input('Введите количество костюмов: ')), float(input('Введите рост в метрах: ')))
print(f'Для пошива {w1.guant} пальто понадобится {w1.fabric_consumption} метров ткани')
print(f'Для пошива {w2.guant} костюмов понадобится {w2.fabric_consumption} метров ткани')

print(f'Всего потребуется {w1.fabric_consumption + w2.fabric_consumption} метров ткани')
