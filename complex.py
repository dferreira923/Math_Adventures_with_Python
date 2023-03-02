from math import sqrt


# Adding two complex numbers
def c_add(a, b):
    return [a[0] + b[0], a[1] + b[1]]


# Product of two complex numbers
def c_mult(u, v):
    return [u[0] * v[0] - u[1] * v[1], u[1] * v[0] + u[0] * v[1]]


# Writing the Magnitude() Fuction
def magnitude(z):
    return sqrt(z[0] ** 2 + z[1] ** 2)


# Creating the mandelbrot set
def mandelbrot(z, num):
    count = 0
    z1 = z
    while count <= num:
        if magnitude(z1) > 2.0:
            return count
        z1 = c_add(c_mult(z1, z1), z)
        count += 1
    return num

