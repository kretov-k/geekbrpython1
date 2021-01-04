class Matrix:
    def __init__(self, x):
        self.x = x


    def __add__(self, other):
        for i in range(len(self.x)):
            for el in range(len(self.x[i])):
                x[i][el] = self.x[i][el] + other.x[i][el]
        return Matrix(x)


    def __str__(self):
        return '\n'.join([' '.join([str(a) for a in i]) for i in self.x])


x = [[1, 2, 3],
     [1, 2, 3]]
y = [[3, 2, 1],
     [3, 2, 1]]
z = [[12, 12, 12],
     [12, 12, 12]]


m1 = Matrix(x)
m2 = Matrix(y)
m3 = Matrix(z)
m4 = m1 + m2 + m3 + m2
print(m4)