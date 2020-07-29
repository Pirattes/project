class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return print('Запуск отрисовки карандашом')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return print('Запуск отрисовки маркером')


pen_obj = Pen('Рисунок века')
pen_obj.draw()
print(pen_obj.title)
penc_obj = Pencil('Рисунок десятилетия')
penc_obj.draw()
print(penc_obj.title)
handle_obj = Handle('Супер рисунок')
handle_obj.draw()
print(handle_obj.title)
