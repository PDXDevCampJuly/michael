#global 
key = {}

def start():
	#Start Discription
#	print("Welcom to the A-maz")
	#Calling the first room
	room0()

def proces_user_movement(description, doors):

	#Making a string of whatever the doors names are
	doorsname = ""
	# Puts key in dict into string
	for x in doors.keys():	
		doorsname += x + " "
	#Printing The discription + the exits are and the exits names
	print(description, "What you can do: " + doorsname)
	#prints and lets you choose where to move
	move = input("What do you want to do? If you want to quit write 'Quit' and press enter: ")
#	wand = 0
	#making it either loop or quit
	if move.lower() in doors:
		doors[move.lower()]()
	elif move.lower() != "quit":
	#Calls funtion
		proces_user_movement(description, doors)



def room0():
	#This variable defines the description of the room
	description = """You wake up in your dorm ready for your first day at Hogwarts! \nYou look around for your map of the school but OH NO! It seams that you've lost it!\nYou guess you'll just have to go around the school and hope for the best."""
	#This is the dict that holds the direction of the room and where to go
	doors = {"go north":room2, "go west":room1}
	#Calling funtion
	proces_user_movement(description, doors)


def room00():
	#This variable defines the description of the room
	description = """You're in your dorm."""
	#This is the dict that holds the direction of the room and where to go
	doors = {"go north":room2, "go west":room1}
	#Calling funtion
	proces_user_movement(description, doors)



def room1():

	description = "It looks like the room you enterd is a closet! There's nothing in here but clothes and a piece of paper."

	doors = {"go east":room00, "pick up and read paper":room10}

	#if move.lower == "pickup key":
		#key['hallwaykey'] = 'hallkey'

	proces_user_movement(description, doors)

#	if pickup.lower == "yes":
#		wand + 1

def room10():
	global key

	#key['hallwaykey'] = 'hallkey'
	key['hallkey'] = 'hallwaykey'

	description = "You pick up the paper and read 'tardis'.\nYou don't know what that could mean but you'll keep it just incase. Now what?"

	doors = {"go east":room00}

	proces_user_movement(description, doors)



def room2():

	description = "You go into the schools hall. It's full of kids rushing to and from class. There's a few promising looking doors in here!\nThere's a big picture that goes to another hall, you need a password to get in though."

	doors = {"go south":room00, "go west":room3, "go north":roomkey}

#	if move.lower == "go north" and wand > 0:
#		room4()
#	if move.lower == "go north" and wand < 0:
#		print("Oh no! You know remember they locked this door! If only you had a key ):")
#	else:
	proces_user_movement(description, doors)


def roomkey():
	global key

	if "hallkey" in key:
		room4()
	else:
		print("")
		roomnokey()


def roomnokey():

	description = "You walk up the the picture, an old man in a tan jacket and a deerskin suitcase looks down at you and asks in a deep voice 'Password?'\n You try tell him that you don't know what it is but you think your class is in there so you reaally need in but he just glares at you and dissapers in a cloud of smoke"

	doors = {"go south":room00, "go west":room3}

	proces_user_movement(description, doors)




def room3():

	description = "You walk into a Divination! The lecture sounds intresting but sadly this isnt a class for first years."

	doors = {"go east":room2}

	proces_user_movement(description, doors)



def room4():

	description = "You walk up the the picture, an old man in a tan jacket and a deerskin suitcase looks down at you and asks in a deep voice 'Password?' \n You remember the piece of paper in your pocket and read it out to the man. \nAfter a minute he lets you into the other hallway. There's more doors to go though in here here."

	doors = {"go east":room5, "go south":room2, "go west":room6}

	proces_user_movement(description, doors)



def room5():

	description = "You've found your class!! You quickly go over to sit with your friends and wait for class to start"

	doors = {"start over":room0}

	proces_user_movement(description, doors)


def room6():

	description = "You walk right outside Hogwarts into the ccourtyard! You don't think your class is going to be out here."

	doors = {"go east":room4}

	proces_user_movement(description, doors)

#def cla1():
#	description = "Today in class you're lerning how to duel for the first time! Try to win againt your enemy Mraco Dalfoy!"

#	from random import randint 

#WHAT I WANT TO HAPPEN: You and your en start off with 100 HP 
#I want there to be a list of spells and every time you pick a spell it rolls two random numbers.
# It prints he take's x amount of damage and you take y amount of damage. When you get to zero. It will say you lose. If your 



start()