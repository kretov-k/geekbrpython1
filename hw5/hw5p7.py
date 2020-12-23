import json
f = open("p7.txt", "r")
prib = 0
dict = {}
sumpr = 0
kolvo = 0
for i in f:
    name, form, prof, exp = i.split()
    prib = int(prof) - int(exp)
    if prib > 0:
        sumpr += prib
        kolvo += 1
    dict.update({name: prib})
f.close()
dict2 = {"average_prof": sumpr // kolvo}
spisok = [dict, dict2]
print(spisok)
with open("p7.json", "w") as js:
    json.dump(spisok, js)
