from math import *

alfa = float(input("введите значение aльфа: "))

z1 = float(sin(2*alfa)+sin(5*alfa)-sin(3*alfa)/cos(alfa)+1-2*sin(2*alfa)**2)
z2 = float(2*sin(alfa))

print ("вы дали значение альфа:", alfa)
print ("вы получили: ", z1)
print ("вы получили: ", z2)