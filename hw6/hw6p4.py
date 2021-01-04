class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} поехала!")

    def stop(self):
        print(f"{self.name} остановилась!")

    def turn(self, dir):
        if dir == "Налево" or dir == "налево":
            print(f"{self.name} повернула налево!")
        elif dir == "Направо" or dir == "направо":
            print(f"{self.name} повернула направо!")
        else:
            print(f"{self.name} в камень въехала!")

    def showspeed(self):
        print(f"{self.name} едет со скоростью {self.speed}")

    def ispolice(self):
        if self.is_police == True:
            print(f"{self.name} коп.")
        else:
            print(f"{self.name} не коп.")

class Towncar(Car):
    def showspeed(self):
        if self.speed > 60:
            print(f"{self.name} стала капсулой скорости!")

class Workcar(Car):
    def showspeed(self):
        if self.speed > 40:
            print(f"{self.name} может обогнать лошадь с повозкой!")

class Sportcar(Car):
    pass


class Policecar(Car):
    pass

t = Towncar(70, "Желтый", "Ока", False)
w = Workcar(50, "Серый", "Фура", False)
s = Sportcar(100, "Синий", "А7", False)
p = Policecar(15, "Камуфляж", "Девятка", True)

t.go()
w.go()
s.go()
p.go()
t.stop()
w.stop()
s.stop()
p.stop()
t.turn("Налево")
w.turn("Направо")
s.turn("налево")
p.turn("Заблудился")
t.showspeed()
w.showspeed()
s.showspeed()
p.showspeed()
t.ispolice()
w.ispolice()
s.ispolice()
p.ispolice()
print(t.name, w.color, s.speed)

