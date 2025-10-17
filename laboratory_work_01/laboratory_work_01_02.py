from math import cos, sin, tan

alfa = float(input("введите значение aльфа: "))

z1 = float(2*cos(alfa)*sin(2*alfa)-sin(alfa)/cos(alfa)-2*sin(alfa)*sin(2*alfa))
z2 = float(tan(3*alfa))

print("Вы дали значение альфа: {0:.2f}\nВы получили z1: {1:.2f}\nВы получили z2: {2:.2f}"
      .format(alfa, z1, z2))