#hangman.py
# A program about hanging people if you don't spell things correctly.

from random import randint

words = ["test","round","rhyme","hello","awesome"]
numWrong = 0
listedWord = [None]

#listedWord = ranodm.choice(words)
#word = words[randint(0,len(words)-1)]

def main():
	welcome = input("Welcome to Hangman! would you like you play?")
	if welcome.lower() == "yes":
		hangperson()
#	elif:
#		exit()


# A function that starts and plays the hangperson game.

	if listWord != userGuess:
		numWrong = +1

	if numWrong == 5:
		print("Game over (x_x)")
	hangperson()

# Users can be wrong a maximum of 5 times before they lose,

# the 6th wrong guess triggering Game Over.
def hangperson():
   global listedWord

	# Greet the user
	#print("Let's play a game")
	#print("Let's play a game of hangperson")

	# Randomly select a word from the list of words
word = words[randint(0,len(words)-1)]
	#eachletter = word.deepcopy(word)
user_letter = input("Enter a letter: ")

	#status = ['_' for i in xrange(len(word))]
	#for index, ltr in enumerate(word):
	#if ltr == user_letter:
	#		status[index] = user_letter

	# Make the randomly selected word into a list object
	
	# Make another list the same length as the word, but with
	# '_' instead of letters. This will track the user's progress.
	# Use the variable name currentState
   currentState = ""
	currentState += str(status)

	# Print the initial state of the game
	print(Hangperson(currentState))

	# Start the game! Loop until the user either wins or loses
	while currentState != listedWord and numWrong < 6:
			pass

	# Determine if the user won or lost, and then tell them accordingly


	# This helpful function prompts the user for a guess,
	# accepting only single letters.
	# DO NOT CHANGE
	#
	# returns a letter
def userGuess():
	guess = input("Guess a letter in the word! (Say 'exit' to stop playing) ")
	while len(guess) != 1:
		pass

	return guess


	# Update the state of the game based on the user's guess.
	#
	# guess: a character guessed by the user
	# currentState: the current state of the word/game
	#
	# return currentState
def updateState(guess, currentState):
	global numWrong

	numInWord = listedWord.count(guess)
	for index, char in enumerate(listedWord):
		if char == guess:
			currentState[index] = guess

	# First, determine if the letter guessed is in the word.
	# If it isn't, tell the user and update the numWrong var
	# If it is, congratulate them and update the state of the game.
	#    To update the state, make sure to replace ALL the '_' with
	#    the guessed letter.
	numInWord = listedWord.count(guess)

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

# This line runs the program on import of the module
hangperson()