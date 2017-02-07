# This is a guess the number game

import random
secretNumber = random.randint(1, 20)
print('Im thinking about a number betweeen 1 and 20')

# Ask the player to guess 6 times

for guessTaken in range (1, 7):
    print('Take the guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is to low.')
    elif guess > secretNumber:
        print('Your guess is to high.')
    else:
        break # This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessTaken) + ' guesses!')
else:
    print('Nope, the number I was thinking of was ' + str(secretNumber))