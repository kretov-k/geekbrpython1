f = open("p5.txt", "w")
f.write(input("Введите сколько хотите чисел через пробел: "))
f.close()
f = open("p5.txt", "r")
v = f.read().split()
print(v)
sum = 0
for i in v:
    sum += int(i)
print(f"Сумма введённых чисел равна: {sum}")