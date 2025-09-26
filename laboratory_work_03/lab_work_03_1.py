from math import *
xb = float(input("Введите значение для Xbeg="))
xe = float(input("Введите значение для Xend="))
dx = float(input("Введите значение для Dx="))

y = 0
xt = xb
print ("I   X   I    Y   I ")
print ("+---------+-------+")
while xt < xe:
    if xt <= 0:
        y = 0.5*xt- 3
    elif 0 <= xt <3:
        y = -sqrt(9-xt**2)
    elif  3<= xt <= 6:
        y = sqrt(9-(xt-6)**2)
    print ("I{0: 7.2f} I{1: 7.2f} I"
           .format( xt, y))

    xt += dx
print ("+---------+-------+")
