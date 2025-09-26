x = float(input("Введите значение для переменной X: "))
y = float(input("Введите значение для переменной Y: "))
R = float(input("Введите значение для радиуса R: "))

if x**2 + y**2 <= R**2 and y >= 0 and -R <= x <= R:
    print("Вы вели X= ", x)
    print("Вы ввели Y= ", y)
    print("Вы ввели R= ", R)
    print ("Внутри" )
elif -R <= x <= 0 and y <= x and -R <= y <= 0:
    print("Вы вели X= ", x)
    print("Вы ввели Y= ", y)
    print("Вы ввели R= ", R)
    print("Внутри")
else:
    print ("Вы вели X= ", x)
    print ("Вы ввели Y= ", y)
    print ("Вы ввели R= ", R)
    print("Снаружи")
