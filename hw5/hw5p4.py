f = open("p4.txt", "r")
txt = f.readlines()
print(txt)
f.close()
perevod = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
nov = []
for i in txt:
    i = i.split(" ")
    if i[0] in perevod:
        slov = perevod[i[0]]
        nov.append(slov + " - " + i[2])
f = open("p4p2.txt", "w")
f.writelines(nov)
f.close()