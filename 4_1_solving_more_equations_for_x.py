#Exercise 4-1

def four_dot_one(a, b, c, d):
    # Orig. formula = 12x + 18 = -34x + 67
    # Rewritten formula: (67 - 18) / (12 + 34)
    return (d - b) / (a + c)


print("x \u2248 ", round(four_dot_one(12, 18, 34, 67), 3))
