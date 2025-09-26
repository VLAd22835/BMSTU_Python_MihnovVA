from math import *
from random import *
R = float(input("Введите радиус R: "))
flag = 0
print ("     X      Y       Res")
print ("_______________________")
for n in range (10):
    x = uniform (-R,R)
    y = uniform (-R,R)
    if (x < -R) or (x > R):
        flag = 0 #False
    if ((-R <= x <= R) and (y >= 0) and (x**2 + y**2 <= R**2)):
        flag = 1 #true
    elif ((-R <= x <= 0) and (y <= x) and (-R <= y <= 0)):
        flag = 1 #true
    else:
        flag = 0
    print ("{0: 7.2f} {1: 7.2f}"
           .format(x,y), end=" ")
    if flag:
        print ("  Попадание")
    else:
        print ("  Промах")
