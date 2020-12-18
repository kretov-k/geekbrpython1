f = open("p3.txt", "r")
txt = f.read().split("\n")
print(txt)
f.close()
men = []
bol = []
sal = 0
sot = 0
for i in txt:
    i = i.split(",")
    sal += int(i[1])
    sot += 1
    if int(i[1]) < 20000:
        men.append(i[0])
    else:
        bol.append(i[0])
print(f"Всего {sot} сотрудников. Меньше 20 получают: {men}. Больше 20 получают: {bol}. А средняя зп: {sal // sot}")
