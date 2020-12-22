class Worker:

    def __init__(self, name, lastname, pos, zp, bn):
        self.name = name
        self.lastname = lastname
        self.pos = pos
        inc = {"wage": zp, "bonus": bn}
        self._income = inc

class Position(Worker):

    def getfullname(self):
        return print(f"{self.name} {self.lastname}")

    def getfincome(self):
        return print(self._income.get("wage") + self._income.get("bonus"))

petrov = Position("Ignatiy", "Petrov", "Baker", 10000, 5000)
petrov.getfullname()
print(petrov.pos)
petrov.getfincome()