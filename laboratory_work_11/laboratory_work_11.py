#4
# a = input("Введите четырёхзначное число: ")
# b = [int(c) for c in a]
# print("Сумма чисел числа равняется " + str(sum(b)))

# 5
# n = int(input("Введите число прошедших минут: "))
# if n >=0:
#     print("Кол-во прошедших: часов -", str(n // 60) + "; минут -", n % 60)
# else:
#     print("Введены некорректные данные")

# 6
# d = float(input("введите толщину кольца: "))
# R = float(input("введите радиус кольца: "))
# n = int(input("введите количество колец: "))
#
# L = int(n * (2 * R + d) - d)
# print("длина цепи составляет", L)

#7
# n = int(input("введите километры в день: "))
# m = int(input("введите длину маршрута: "))
# days = int((m + n ) // n)
# print("кол-во дней", days)

#8
# a = int(input("введите кол-во учеников в классе а : "))
# b = int(input("введите кол-во учеников в классе b : "))
# c = int(input("введите кол-во учеников в классе с : "))
#
# def desks(students):
#     if students % 2 == 0:
#         return students // 2
#     else:
#         return students // 2 + 1
#
# total = desks(a) + desks(b) + desks(c)
# print("нужно закупить", total,"парт")