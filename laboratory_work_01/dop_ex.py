from math import cos, sin, tan

alfa = float(input("введите значение aльфа: "))

z1 = float (2*cos(alfa)*sin(2*alfa)-sin(alfa)/cos(alfa)-2*sin(alfa)*sin(2*alfa))
z2 = float (tan(3*alfa))

print ("вы дали значение альфа:", alfa)
print ("вы получили: ", z1)
print ("вы получили: ", z2)