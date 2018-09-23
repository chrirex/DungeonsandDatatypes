# HW 1 - A Guess the Number game
import random

guessesTaken = 0

print('Hello! WHat is your name?')
myName = input()

#TODO: create a variable called 'number' and set it to a random number
# between 1 and 20

print('Well, ' + myName + 'I am thinking of a number between 1 and 20.')
for guessesTaken in range(6):
    print ('Take a guess.')
    
    #TODO: create a variable called 'guess' and set it to be what the player
    #enters. You will then need to cast it to be an int to use later in the game
    
    if guess < number:
        print('Your guess is too low!')

    #TODO: check if the guess is too high. If it is, let the player know
    # Be careful on how much this is indented

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print ('Good job, '+myName+'! You guessed my number in '+guessesTaken+' guesses!')

#TODO: Check if the current guess is not the number. If so, tell the player what
#the number was. Becareful of the indentation here as well.
