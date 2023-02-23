from turtle import *
shape('turtle')
speed(0)

def star_spiral(sides=60,sidelength=5):
    for i in range(sides):
        forward(sidelength)
        right(144)
        forward(sidelength)
        right(144)
        forward(sidelength)
        right(144)
        forward(sidelength)
        right(144)
        forward(sidelength)
        right(144)
        right(5)
        sidelength += 5
        
star_spiral()
