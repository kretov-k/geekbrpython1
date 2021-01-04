class Kletki:
    def __init__(self, x):
        if x >= 0:
            self.x = x
        else:
            print("Отрицательного количества клеток не бывает! Увы.")
            exit()

    def __add__(self, other):
        x =  self.x + other.x
        return Kletki(x)


    def __sub__(self, other):
        x = self.x - other.x
        if x > 0:
            return Kletki(x)
        elif x == 0:
            return "Клеток не осталось! :("
        else:
            return "Клеток аж меньше нуля!"


    def __mul__(self, other):
        x = self.x * other.x
        return Kletki(x)


    def __truediv__(self, other):
        if other.x == 0:
            raise ZeroDivisionError("На ноль делишь!")
        else:
            x = self.x / other.x

        return Kletki(round(x))

    def makeorder(self, k):
        r = ''
        for i in range(self.x // k):
            r += f'{"*" * k}\n'
        r += f'{"*" * (self.x % k)}'
        return r


    def __str__(self):
        return f"{self.x}"


x = Kletki(26)
y = Kletki(5)
a = x + y
s = x - y
m = x * y
t = x / y
print(a, s, m, t)
print(x.makeorder(10))