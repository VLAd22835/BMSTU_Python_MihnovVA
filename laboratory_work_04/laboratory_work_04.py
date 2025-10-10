from math import*
from random import uniform

from pygame.examples.eventlist import last_key

n = int(input("Элементов в массиве (N<=30) N: ")) #запрос кол-ва элементов
if n > 30:
    n = 30
elif n < 5:
    n = 5
# Генерация массива и вывод
print ("Начальное состояние")
mas = []
for i in range (n):
    mas.append(uniform(-5, 5))
    if mas[i] >= 0:
        print ("{0: 7.3f}".format(mas[i]), end=" ")
    else:
        print("{0: 7.3f}".format(mas[i]), end=" ")
print ()
# Нахождение суммы
# Обнуление элементов превысших порог
asum = 0.0
for i in range (1, n, 2):
    print ("mas [{0}] = {1:7.3f}".format(i,mas[i]))
    asum += mas[i]
if asum >= 0:
    print ("Сумма элементов с нечетными номерами:   {0:7.3f}".format(asum), end="")
else:
    print ("Сумма элементов с нечетными номерами:   {0:7.3f}".format(asum), end="")


