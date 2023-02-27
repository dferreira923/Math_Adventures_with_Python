from random import randint


# Random Number Generator 3.3
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
