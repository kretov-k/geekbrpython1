f = open("p6.txt", "r")
l = ""
p = ""
la = ""
v = {}
for i in f:
    pred, lec, prac, lab = i.split()
    for x in lec:
        if x.isdigit():
            l += x
    for y in prac:
        if y.isdigit():
            p += y
    for z in lab:
        if z.isdigit():
            la += z
    v.update({pred: int(l) + int(p) + int(la)})
print(f"Список предметов и кол-во часов по ним ниже:\n{v}")
f.close()

# не знаю как обнулять переменные каждый новый цикл, которыми отделяю цифры от скобок. Вписываю их в цикл, он их
# не считает, а так он на них накапливает значение и получается бред.