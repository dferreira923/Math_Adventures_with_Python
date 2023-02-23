from turtle import *
shape('turtle')
speed(0)

def square_spiral(sides=60,sidelength=5):
    for i in range(sides):
        forward(sidelength)
        right(90)
        forward(sidelength)
        right(90)        
        forward(sidelength)
        right(90)
        forward(sidelength)
        right(90)
        right(5)
        sidelength += 5

square_spiral()
