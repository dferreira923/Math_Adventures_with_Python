from turtle import *
shape('turtle')
speed(0)


def triangle_loop(sidelength=100):
    for i in range(3):
        forward(sidelength)
        left(120)

triangle_loop()
