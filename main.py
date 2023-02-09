#ax^2 + bx + c = 0
a = float(input())
b = float(input())
c = float(input())

D = b**2 - 4*a*c

if D > 0:
    x1 = (b*(-1) + D**0.5)/(2*a)
    x2 = (b*(-1) - D**0.5)/(2*a)
    print(x1, x2)
elif D == 0:
    x = (b * (-1)) / (2 * a)
    print(x)
else:
    print("Корней нет")
