#conditionals
from turtle import *
from random import randint
from math import sqrt

'''
y = 6
if y > 7:
    print("yes!")
else:
    print("no!")
    
age = 50
if age < 10:
    print("What school do you go to?")
elif 11 < age < 20:
    print("You're cool!")
elif 20 <= age < 30:
    print("What kind of job do you have?")
elif 30 <= age < 40:
    print("Are you married?")
else:
    print("Wow, you're old!")
'''



#Using Conditions to Find Factors
'''
def factors(num):
    factor_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            factor_list.append(i)
    return factor_list


print(factors(120))
'''



'''
# Exercise 3-1: Finding the Factor
def gcf(num_a, num_b):
    if num_a > num_b:
        num_a, num_b = num_b, num_a

    for x in range(num_a, 0, -1):
        if num_a % x == 0 and num_b % x == 0:
            return x


num_a = 150
num_b = 138
print(str(gcf(num_a, num_b)))
'''



#The Wandering Turtle
'''
speed(0)
def wander():
    while True:
        fd(3)
        if xcor() >= 200 or xcor() <= -200 or ycor() <= -200 or ycor() >= 200:
            lt(randint(90,180))
wander()
'''


# Random Number Generator 3.3
'''
def rand_number():
    number = randint(1, 100)
    print("I'm thinking of a number between 1 and 100!")
    guess = int(input("What do you think it is?"))

    if number == guess:
        print("Oh snap, you got it!")
    elif number > guess:
        print("Nope, higher")
    else:
        print("Nope, lower")


rand_number()
'''

'''
def rand_number():
    number = randint(1, 100)
    print("I'm thinking of a number between 1 and 100!")
    guess = int(input("What do you think it is?"))

    while guess:
        if number == guess:
            print("Good job, champ! You guessed it!")
            break
        elif number > guess:
            print("Sorry bud, too loo. Go higher!")
        else:
            print("Bruh... Too high, try a lower number!")
        guess = int(input("Number???"))

rand_number()
'''



'''
def average(a, b):
    return (a + b) / 2


def square_root(num, low, high):
    for i in range(20):
        guess = average(low, high)
        if guess ** 2 == num:
            print(guess)
        elif guess ** 2 > num:
            high = guess
        else:
            low = guess
    print(guess)


square_root(60, 7, 8)
'''



def find_sqroot(num1, num2, num3):
    for i in range(3):
        a = sqrt(num1)
        b = sqrt(num2)
        c = sqrt(num3)
    print(a, b, c)


find_sqroot(200, 1000, 50000)
















































