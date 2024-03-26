import math
print ('Введите коэффициенты квадратного уравнения:')
a = int(input("введите коэффициент a "))
b = int(input("введите коэффициент b "))
c = int(input("введите коэффициент c "))
first = b * b
second = 4 * a * c
A = a * 2
d = first - second
if d >= 1:
    D = math.sqrt(d)
    y1 = b * -1 + D 
    y2 = b * -1 - D
    x1 = y1 / A
    x2 = y2 / A
    print('корни квадратного уравнения:', x1, x2)
elif d == 0:
    x1 = b * -1 / A
else:
    mmm = 1