# Finding the sum from natural numbers 1 through 100
def new_sum(num):
    running_sum = 0
    for i in range(1, 101):
        running_sum += i
    return running_sum


print(new_sum(1))


# Finding the sum from natural numbers 1 through 1,000
def new_sum2(num2):
    running_sum2 = 0
    for i in range(1, 1001):
        running_sum2 += i
    return running_sum2


print(new_sum2(1))
