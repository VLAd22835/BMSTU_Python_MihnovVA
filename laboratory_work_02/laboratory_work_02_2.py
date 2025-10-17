x = float(input("Введите значение для переменной X: "))
y = float(input("Введите значение для переменной Y: "))
R = float(input("Введите значение для радиуса R: "))

if x**2 + y**2 <= R**2 and y >= 0 and -R <= x <= R:
    print("Вы ввели X= {0:.2f}".format(x))
    print("Вы ввели Y= {0:.2f}".format(y))
    print("Вы ввели R= {0:.2f}".format(R))
    print("Внутри")
elif -R <= x <= 0 and y <= x and -R <= y <= 0:
    print("Вы ввели X= {0:.2f}".format(x))
    print("Вы ввели Y= {0:.2f}".format(y))
    print("Вы ввели R= {0:.2f}".format(R))
    print("Внутри")
else:
    print("Вы ввели X= {0:.2f}".format(x))
    print("Вы ввели Y= {0:.2f}".format(y))
    print("Вы ввели R= {0:.2f}".format(R))
    print("Снаружи")