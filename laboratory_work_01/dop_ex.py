from math import *

y = float(input("введите значение для y: "))

z1 = float(sin(2*y)+sin(5*y)-sin(3*y)/cos(y)+1-2*sin(2*y)**2)
z2 = float(2*sin(y))

print ("вы дали значение y:", y )
print ("вы получили: ", z1)
print ("вы получили: ", z2)