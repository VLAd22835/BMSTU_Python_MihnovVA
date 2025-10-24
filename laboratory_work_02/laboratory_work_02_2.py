x = float(input("Введите значение для переменной X: "))
y = float(input("Введите значение для переменной Y: "))
R = float(input("Введите значение для радиуса R: "))

if x**2 + y**2 <= R**2 and y >= 0 and -R <= x <= R:
    flag = False
elif -R <= x <= 0 and y <= x and -R <= y <= 0:
    flag = False
else:
    flag = True

if flag:
    print ("Точка снаружи")
else:
    print ("Точка внутри")