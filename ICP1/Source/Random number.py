import random

Number = random.choice([0,9])

while True:

    Guess = int(input("Guess a number:"))
    if Number>Guess:
         print('Your answer is lower than required')

    elif Number<Guess:

        print('Your answer is greater than required')

    else:
        print('You got the right one!!')
        break




