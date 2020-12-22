from time import sleep

class Traffic_light:
    __color = ["Красный", "Желтый", "Зеленый"]

    def perekl(self):
        x = 0
        while x <= 2:
            print(f"Сейчас горит: {Traffic_light.__color[x]}")
            if x == 0:
                sleep(7)
            elif x == 1:
                sleep(2)
            elif x == 2:
                sleep(4)
                print("Закончили переключение")
            x += 1

tl = Traffic_light()
tl.perekl()