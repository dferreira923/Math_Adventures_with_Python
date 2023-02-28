#Exercise 4-2 Fractions as Coefficients

def four_dot_two(a, b, c, d):
    # Orig. formula = 1/2x + 2/3 = 1/5x + 7/8
    # Rewritten formula: (7/8 - 2/3) / (1/2 - 1/5)
    return (d - b) / (a - c)


x = four_dot_two(1 / 2, 2 / 3, 1 / 5, 7 / 8)
print(x)
