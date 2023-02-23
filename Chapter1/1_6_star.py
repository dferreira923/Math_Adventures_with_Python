from turtle import *
shape('turtle')
speed(0)

def star(sides=5,sidelength=200):
    for i in range(sides):
        forward(sidelength)
        right(144)

star()
