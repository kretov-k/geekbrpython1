class Road:

    def __init__(self, _width, _length):
        self._width = _width
        self._length = _length

    def formula(self, m, t):
        r = self._width * self._length * m * t
        return print(f"Итак путем перемножения всех значений получаем: {r} кг асфальта")


m = int(input("Введите массу одного квадратного метра дороги в кг: "))
t = int(input("Введите необходимую толщину дорожного полотна в см: "))
w = int(input("Введите ширину дороги: "))
l = int(input("Введите длину дороги: "))
doroga = Road(w, l)
doroga.formula(m, t)
