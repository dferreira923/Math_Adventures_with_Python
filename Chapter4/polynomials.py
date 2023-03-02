from math import sqrt

#Solving Higher-Degree Equations
#Using Quad() to Solve Quadratic Equations
#form 1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
#form 1 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)

def quad(a, b, c):
    x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
    return x1, x2

print(quad(2,7,-15))

