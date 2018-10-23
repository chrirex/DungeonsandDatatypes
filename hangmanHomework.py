import random

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']

words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
lion lizard llama mole monkey moose mouse mule newt otter owl panda
parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
skunk sloth snake spider stork swan tiger toad trout turkey turtle
weasel whale wolf wombat zebra'''.split()

def getRandomWord(wordList):
    #TODO: Get a random string (word) from the list of strings
    #that's passed into it

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed Letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # Replace blanks with correct guess letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: #Show the secret word with spaces in between letters
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    #Returns the letter the player entered. 
    while True:
        print('Guess a letter')
        guess = input()
        guess = guess.lower()
        #TODO: Write code to make sure the user entered only one character,
        # that the character has not been guessed already, and that the
        # character is an actual letter, if so, return the guess

def playAgain():
    # This function returns True if the player wants to play again;
    # otherwise, it returns False
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player enter a letter
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won
        foundAllLetters = True

        #TODO: Check to see if all of the letters have been found.
        # If not, set foundAllLetters to False;

        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You\'ve won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        #TODO: Check to see if the player has guessed too many times.
        # If so, give the user the number of correct and incorrect
        # guesses, and the secret word, then set gameIsDone to True


    # Ask the player if they want to play again (only if game is done)
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
