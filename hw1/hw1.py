# первое задание
# ввод/вывод значений, сравнение и вывод ответа
print(f"Первое задание.\n")
city = input("В каком городе вы родились? ")
len = int(input("В каком году умер Ленин? "))
lend = 1924
if len == lend:
    print(f"В городе {city} хорошо знают историю")
else:
    print('Ну не помните и не помните, вы же всё равно хороший человек! :)')

# второе задание
# делим, выводим, ищем остаток от деления, делим, выводим и т.д.
print(f"\nВторое задание.\n")
time = int(input("Сколько секунд вам перевести? "))
hours = time // 3600
premin = time % 3600
minutes = premin // 60
sec = premin % 60
print(f"Ваши секунды на цифровых рабочих часах будут выглядеть так: {hours:02}:{minutes:02}:{sec:02}")

# третье задание
# не сразу дошло, что есть возможность складывать строки, но поняв это пришло понимание
print(f"\nТретье задание.\n")
dgn = int(input("Загадайте число от бесконечности и до куда захотите: "))
dgns = str(dgn)
dgn2 = dgns + dgns
dgn3 = dgn2 + dgns
dgnresult = dgn + int(dgn2) + int(dgn3)
print("Сумма ваших странноватых сложений равна: ", dgnresult)

# четвертое задание
# предположили что последнее число является самым большим и далее в цикле сравниваем его со всеми остальными
# отбрасывая предыдущие
print(f"\nЧетвертое задание.\n")
ch = int(input("Введите целое, положительное число: "))
os = ch % 10
ch = ch // 10
while ch > 0:
    chp = ch % 10
    if chp > os:
        os = chp
    ch = ch // 10
print(f"Самая большая цифра в Вашем числе - {os}")

# пятое задание
print(f"\nПятое задание.\n")
vir = int(input("Введите сумму выручки в долларах: "))
ras = int(input("Введите сумму расходов в долларах: "))
if vir < ras:
    print("Увы Господа, но вы фигово работаете.")
elif vir == ras:
    print("В ноль работать тоже можно, но кому это нужно?")
else:
    sot = int(input("Введите количество сотрудников в человеках: "))
    pribs = vir / ras
    prib = vir - ras
    pribsot = prib / sot
    print(f"Господа! Ваше выгодное предприятие работает с соотношением прибыли к убыткам равным {pribs:.2f}, а если\n"
          f"заработанное вы разделите равными долями между всеми сотрудниками, то каждый получит по {pribsot:.2f}$.")

# шестое задание
print(f"\nШестое задание.\n")
dist = 5
day = 1
tdist = 5
dd = float(input("Бегун в первый день пробежал пятерку и затем ежедневно добавлял 10% к дистанции предыдущего дня.\n"
                 "Если вы скажете на какой дистанции он помрёт от нагрузки, то мы вычислим день когда это случится.\n"
                 "Итак, укажите расстояние в километрах: "))
print(f"1-ый день\n- 5км пробежал сегодня\n- 5км общий километраж\n")
while dist < dd:
    dist = dist * 1.1
    day = day + 1
    tdist = tdist + dist
    print(f"- {day}-ый день\n- {dist:.2f}км пробежал сегодня\n- {tdist:.2f}км общий километраж\n")
print(f"Предыдущая запись сделанная на {day}-ый день оказалась завершающей в карьере нашего бегуна. Он преодолел\n"
      f"отметку Вашего прогноза, выжил, проклял всё и ушел играть в PS5.")