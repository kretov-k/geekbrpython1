class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"{self.title} запускает отрисовку!")

class Pencil(Stationery):

    def draw(self):
        print("Рисуете карандашом!")

class Pen(Stationery):

    def draw(self):
        print("Рисуете ручкой!")

class Handle(Stationery):

    def draw(self):
        print("Малюете маркером!")

x = Pencil("Карандаш")
y = Pen("Ручка")
z = Handle("Маркер")
zh = Stationery("Ручканашестьдесятстрежней")
x.draw()
y.draw()
z.draw()
zh.draw()

