class Odezhda:
    def __init__(self, t):
        self.t = t


class Palto(Odezhda):
    def __init__(self, v, t):
        super().__init__(t)
        self.v = v

    @property
    def tkan(self):
        tk = self.v / 6.5 + 0.5
        return tk


class Kostum(Odezhda):
    def __init__(self, h, t):
        super().__init__(t)
        self.h = h

    @property
    def tkan(self):
        tk = 2 * self.h +0.3
        return tk

p = Palto(13, "Пальто")
k = Kostum(2, "Костюм")
print(f"Сумма ткани {p.t} и {k.t}a в чём бы она ни измерялась равна {p.tkan + k.tkan}")