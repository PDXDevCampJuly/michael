#hangman.py
# A program about hanging people if you don't spell things correctly.

import random
import time

words = ["test"]
numWrong = 0
listedWord = [None]

# A function that starts and plays the hangperson game.
# Users can be wrong a maximum of 5 times before they lose,
# the 6th wrong guess triggering Game Over.g
def hangperson():
  global listedWord

  # Greet the user
  print("Let's play a game of hangperson!")

  # Randomly select a word from the list of words
  randWord = random.choice(['BLUE', 'RED', 'GREEN', 'YELLOW', 'SMALL', 'BIG', 'ORANGE', 'LIVING', 'LAUNDRY', 'ASSEMBLY', 'WAITING', 'UTILITY', 'HOTEL', 'MEETING', 'SKY', 'RECREATION', 'PANTRY', 'MECHANICAL']).lower()
  print("\n", randWord)

  # Make the randomly selected word into a list object
  listedWord = list(randWord)
  # print(listedWord)

  # Make another list the same length as the word, but with
  # '_' instead of letters. This will track the user's progress.
  # Use the variable name currentState
  currentState = []
  for each_item in listedWord:
    each_item = "_"
    currentState.append(each_item)
  # print(currentState)

  # Print the initial state of the game
  printHangperson(currentState)

  # Start the game! Loop until the user either wins or loses
  while currentState != listedWord and numWrong < 6:
    guess = userGuess()
    updateState(guess, currentState)
    printHangperson(currentState)

  # Determine if the user won or lost, and then tell them accordingly

  if currentState == listedWord and numWrong < 6:
    print("Congratulations! Let's try again...\n")
  else:
    print("Nice try. Let's try again...\n")

# This helpful function prompts the user for a guess,
# accepting only single letters. validator.
# DO NOT CHANGE
#
# returns a letter
def userGuess():
  guess = input("Guess a letter! (Type 'exit' to quit) >>> ").lower()
  # print(listedWord)
  while len(guess) != 1:
    if len(guess) > 1:
      if guess == "exit":
        print("shutting down...")
        time.sleep(2)
        print("bye.")
        exit()
      print(">>> Input a single letter. Try again...")
      break
  return guess

# Update the state of the game based on the user's guess.
#
# guess: a character guessed by the user
# currentState: the current state of the word/game
#
# return currentState
def updateState(guess, currentState):
  global numWrong

  # First, determine if the letter guessed is in the word.
  # If it isn't, tell the user and update the numWrong var
  # If it is, congratulate them and update the state of the game.
  #   To update the state, make sure to replace ALL the '_' with
  #   the guessed letter.
  numInWord = listedWord.count(guess)

  # indices = [i for i, x in enumerate(listedWord) if x == guess]
  # print(indices)
  # for i in indices:
  #   currentState[i] = guess
  # print(' '.join(currentState))

  if guess in listedWord:
    for index, char in enumerate(listedWord):
      if char == guess:
        currentState[index] = guess
    # print(' '.join(currentState))
    print(">>> Nice guess!")
    return currentState

  else:
    numWrong += 1
    print(">>> Bummer! Guess {} of 6.".format(numWrong))
    return numWrong


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
    print(person[numWrong - 1])

  print("\n\n")

  for i in state:
    print(i, end=" ")

  print("\n")

# This line runs the program on import of the module
hangperson()
