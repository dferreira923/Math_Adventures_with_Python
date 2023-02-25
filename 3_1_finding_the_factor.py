# Exercise 3-1: Finding the Factor
def gcf(num_a, num_b):
    if num_a > num_b:
        num_a, num_b = num_b, num_a

    for x in range(num_a, 0, -1):
        if num_a % x == 0 and num_b % x == 0:
            return x


num_a = 150
num_b = 138
print(str(gcf(num_a, num_b)))
