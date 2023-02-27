from random import randint


# Random Number Generator 3.3
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
