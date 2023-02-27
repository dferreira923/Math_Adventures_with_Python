from math import sqrt


def find_sqroot(num1, num2, num3):
    for i in range(3):
        a = sqrt(num1)
        b = sqrt(num2)
        c = sqrt(num3)
    print(a, b, c)


find_sqroot(200, 1000, 50000)
