from turtle import *
shape('turtle')
speed(0)

def polygon(sides=6,sidelength=100):
    for i in range(sides):
        forward(sidelength)
        right(60)

polygon()
