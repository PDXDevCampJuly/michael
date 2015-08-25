#def start():
#	print"""You wake up in the lobby of a in door petting zoo with a paplet for a whole room full of 100 cats! 
#	You have no idea how you got there but you would be crazy not to find the room full of cats and snuggle. 
#	But before you get to the cats you need to find the room with them... There are doors to your left and front."""

#	first = input "Do you walk through the left or front? "

#	if input += "left":
#		print halltocow()
#	if input += "front":
#		print hall()

#def halltocow():
#	print """The door leads you to a diagonal hall, when you get to the end it leads you to a room full of cows!! 
#	This is amazing but but the room you had in mind.. you decide to continue on your quest. There's a door to your right and in front of you"""

#	first = input "Do you walk through the right or front? "

#	if input += "right":
#		print starttwo()
#	if input += "front":
#		print hall()

def start():
	#Start Discription
#	print("Welcom to the A-maz")
	#Calling the first room
	room0()

#def spells_for_wand(description, doors):
#
#	#Making a string of whatever the spells names are
#	spellsname = ""
#	# Puts key in dict into string
#	for x in doors.keys():	
#		doorsname += x + " "
#	#Printing The discription + the exits are and the exits names
#	print(description, "The exits are " + doorsname)
#	#prints and lets you choose where to move
#	move = input("What direction do you want to go? If you want to quit write 'Quit' and press enter: ")
#	#Calls funtion
#	if move in doors:
#		doors[move]()
#	elif move != "Quit":
#		proces_user_movement(description, doors)
#	#input is not equel to key put 
#	#while move not in 



def proces_user_movement(description, doors):

	#Making a string of whatever the doors names are
	doorsname = ""
	# Puts key in dict into string
	for x in doors.keys():	
		doorsname += x + " "
	#Printing The discription + the exits are and the exits names
	print(description, "The exits are " + doorsname)
	#prints and lets you choose where to move
	move.lower = input("What direction do you want to go? If you want to quit write 'Quit' and press enter: ")
	#Calls funtion
	if move.lower in doors:
		doors[move]()
	elif move != "Quit":
		proces_user_movement(description, doors)
	#input is not equel to key put 
	#while move not in 



def room0():
	#This variable defines the description of the room
	description = """You wake up in your dorm ready for your first day at Hogwarts! 
	You look around for your map of the school but OH NO! It seams that you've lost it!
	 You guess you'll just have to go around the school and hope for the best."""
	#This is the dict that holds the direction of the room and where to go
	doors = {"north":room2, "west":room1}
	#Calling funtion
	proces_user_movement(description, doors)


def room00():
	#This variable defines the description of the room
	description = """You're in your dorm."""
	#This is the dict that holds the direction of the room and where to go
	doors = {"north":room2, "west":room1}
	#Calling funtion
	proces_user_movement(description, doors)



def room1():

	description = "It looks like the room you enterd is a clost! There's nothing in here but clothes."

	doors = {"east":room00, "east":room00}

	proces_user_movement(description, doors)



def room2():

	description = "You go into the schools hall. It's full of kids rushing to and from class. There's a few promising looking doors in here!"

	doors = {"south":room00, "west":room3, "north":room4}

	proces_user_movement(description, doors)



def room3():

	description = "You walk into a Divination! The lecture sounds intresting but sadly this isnt a class for first years."

	doors = {"east":room2}

	proces_user_movement(description, doors)



def room4():

	description = "You walk into another part of the hallway. There's more doors to go though over here."

	doors = {"east":room5, "south":room2, "south":room6}

	proces_user_movement(description, doors)



def room5():

	description = "You've found your class!! You quickly go over to sit with your friends right before the bell rings"

	doors = {"start over":room0}

	proces_user_movement(description, doors)


def room6():

	description = "You walk right outside Hogwarts into the ccourtyard! You don't think your class is going to be out here."

	doors = {"east":room4}

	proces_user_movement(description, doors)

#def cla1():
#	description = "Today in class you're lerning how to duel for the first time! Try to win againt your enemy Mraco Dalfoy!"

#	from random import randint 

#WHAT I WANT TO HAPPEN: You and your en start off with 100 HP 
#I want there to be a list of spells and every time you pick a spell it rolls two random numbers.
# It prints he take's x amount of damage and you take y amount of damage. When you get to zero. It will say you lose. If your 



start()




#def room1():