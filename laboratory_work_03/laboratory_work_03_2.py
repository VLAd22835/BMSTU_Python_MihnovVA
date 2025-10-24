from random import uniform
R = float(input("Введите радиус R: "))
flag = False
print ("     X      Y       Res")
print ("_______________________")
for n in range (10):
    x = uniform (-R,R)
    y = uniform (-R,R)
    if (x < -R) or (x > R):
        flag = False #False
    if ((-R <= x <= R) and (y >= 0) and (x**2 + y**2 <= R**2)):
        flag = True #true
    elif ((-R <= x <= 0) and (y <= x) and (-R <= y <= 0)):
        flag = True#true
    else:
        flag = False
    print ("{0: 7.2f} {1: 7.2f}"
           .format(x,y), end=" ")
    if flag:
        print ("  Попадание")
    else:
        print ("  Промах")
