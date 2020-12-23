p1 = open("p1.txt", "w")
p1l = []
while True:
    p1lt = input("Введите что вздумается и повторите. Когда надоест ставьте пробел.")
    if p1lt == " ":
        break
    else:
        p1l.append(p1lt)
p1.writelines(p1l)
p1.close()
p1 = open("p1.txt", "r")
r = p1.readlines()
print(r)
p1.close()