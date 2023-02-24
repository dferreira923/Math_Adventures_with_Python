d = [53, 28, 54, 84, 65, 60, 22, 93, 62, 27, 16, 25, 74, 42, 4, 42, 15, 96, 11, 70, 83, 97, 75]


def average_list(d):
    return sum(d) / len(d)


print(average_list(d))  # Non-rounded, complete calculation
print(round(average_list(d), 3))  # Rounded to 3 decimal places
