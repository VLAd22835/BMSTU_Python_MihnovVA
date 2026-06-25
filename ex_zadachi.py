import math


def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True


num = int(input("Enter number: "))
if is_prime(num):
    print(f"{num} True")
else:
    print(f"{num} False")