# первое задание
# pycharm попросил сделать две пустых строки после функции. так и надо?
# не понял для чего делать рэйз ошибки. она же так и так отрубается?
def delenie(a, b):
    return a / b


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
if b == 0:
    raise ZeroDivisionError
print(f'Результат деления данных чисел = {delenie(a, b)}')

# второе задание
def bio(name, surname, age, city):
    return f'Вас зовут {name} {surname}, вам {age} лет и вы из города {city}. И чет вы долговато живёте.'


info = dict(name='Влад', surname='Дракула', age=376, city='ТрансильванЪск сити')
print(bio(**info))

# третье задание
def summax(q, w, e):
    sum1 = [q, w, e]
    s1 = min(sum1)
    sum1.remove(s1)
    return sum(sum1)


print('Введите три числа')
q = int(input("1)"))
w = int(input("2)"))
e = int(input("3)"))
print(f'Сумма наибольших двух равна - {summax(q, w, e)}')

# четвертое задание
# вариант с оператором **
def my_func(x, y):
    return x ** y
# вариант без него
def my_funcbezoperatora(x,y):
    st = 1
    for i in range(abs(y)):
        st = st * x
    return 1 / st


x = int(input('Введите положительное число: '))
y = int(input('В какую отрицательную степень его возвести? '))
if y < 0 and x > 0:
    print(f'С оператором звёздочки - {my_func(x, y)}')
    print(f'Без него - {my_funcbezoperatora(x,y)}')
else:
    print('Число положительное, а степень отрицательная! Вы чёт напутали.')

# пятое задание
# бился долго, пока не нагуглил цикл try-except. без него на вводе символа всё время отваливалась.
sumch = 0
while True:
    strch = input('Введите числа через пробел, а когда надоест введите знак доллара $: ')
    lstrch = strch.split(" ")
    for i in lstrch:
        try:
            ch = int(i)
            sumch += ch
        except:
            if i == '$':
                print(f'Cумма чисел равна {sumch} finish')
                exit()
                # к сожалению из за этого exit он прерывается до начала шестого задания. а как обойти я не придумал.
    print(f'Сумма чисел равна {sumch}')


# шестое задание
def int_func(word):
    return word.title()


word = input('Введите строку: ')
print(int_func(word))
