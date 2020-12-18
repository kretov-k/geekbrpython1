f = open("p2.txt", "r")
txt = f.readlines()
f.close()
st = 0
n = 0
for l in txt:
    st += 1
    n += 1
    l = l.split()
    print(f"{n}){l} - это текст каждой строки и в ней вот столько слов - {len(l)}.")
print(f"Общее количество строк - {st}")