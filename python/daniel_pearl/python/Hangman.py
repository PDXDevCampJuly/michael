#Hangman
#A program about hanging people if you don't spell things correctly.

from random import randint

words = ["this is a sentence", "hello my name is", "keep playing"]
numWrong = 0
listedWord = [None]

# A function that starts and plays the hangperson game.
# Users can be wrong a maximum of 5 times before they lose,
# the 6th wrong guess triggering Game Over.
def hangperson():
#global listedWord

    # Greet the user
    print("Let's play a game of hangperson!")

    # Randomly select a word from the list of words
    selectedWord = words[randint(0,len(words)-1)]

    # Make the randomly selected word into a list object
    letters = []

    currentState = []
    savedGuess = []
    for i,s in enumerate(selectedWord):
        # Place letters in word into a list
        letters.append(s)
        # Make another list the same length as the word, but with
        # '_' instead of letters. This will track the user's progress.
        # Use the variable name currentState
        if letters[i] != " ":
            currentState.append("_")
        else:
            currentState.append(" ")
    # Print the initial state of the game
    printHangperson(currentState)

    # Start the game! Loop until the user either wins or loses
    while currentState != letters and numWrong < 6:
        savedGuess=[]
        guess = userGuess(savedGuess)

        updateState(guess, currentState, letters)
        printHangperson(currentState)


    victory(currentState, letters, numWrong)

    # Determine if the user won or lost, and then tell them accordingly


# This helpful function prompts the user for a guess,
# accepting only single letters.
# DO NOT CHANGE
#
# returns a letter
def userGuess(lsavedGuess):
    guess = ""

    while not guess:
        guess = input("Guess a letter in the word! (Say 'exit' to stop playing) ")
        if len(guess) > 1:
            print("Too many letters. Try again. ")
            continue
        elif guess in lsavedGuess:
            print("You've already tried that letter. Try again. ")
        else:
            if guess == "exit":
                break
    lsavedGuess.append(guess)
    return guess


# Update the state of the game based on the user's guess.
#
# guess: a character guessed by the user
# currentState: the current state of the word/game
#
# return currentState
def updateState(guess, currentState, lletters):
    global numWrong

    # First, determine if the letter guessed is in the word.
    # If it isn't, tell the user and update the numWrong var
    # If it is, congratulate them and update the state of the game.
    #    To update the state, make sure to replace ALL the '_' with
    #    the guessed letter.

    #numInWord = listedWord.count(guess)
    for index, char in enumerate(lletters):
        if char == guess:
            currentState[index] = guess

    if guess not in lletters:
        numWrong += 1


    #print(currentState)
    return currentState

# A helpful function to print the hangman.
# DO NOT CHANGE
#
# state: current state of the word
def printHangperson(state):
    person = [" O "," | \n | ", "\| \n | ", "\|/\n | ", "\|/\n | \n/  ", "\|/\n | \n/ \\"]
    print()

    if numWrong > 0:
        print(person[0])

    if numWrong > 1:
        print(person[numWrong-1])

    print("\n\n")

    for i in state:
        print(i, end=" ")

    print("\n")

#Set victory conditions
def victory(lcurrentState, lletters, lnumWrong):
    if lcurrentState == lletters:
        print("You win!")
    else:
        print("You lose!")
# This line runs the program on import of the module

hangperson()
