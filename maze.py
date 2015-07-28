# This is a maze program
###########################

# description: a description of the current room
# doors: dictionary with door:location sets
def process_user_movement(description, doors):

  # print the description of the current room
  print(description)

  # print the available doors
  print("Here are your options: ")
  for each_door in doors:
    print(">", each_door)

# """
#   # print("You see doors to the: ", end="")
#   # print(*list(doors.keys()), sep=", ")
# """

  # prompt the for what doors they want
  userInput = input("Choose a door: ").lower()

# """
#   choice = ""
# """

  # do things based on user response
  while True:
    # valid response: go to the correct location
    try:
      if doors[userInput] == fakeDoor:
        fakeDoor()
        userInput = input("You have attempted a fake door, try again: ").lower()
      else:
        doors[userInput]()
        break

    # invalid response: ask them again
    except:
      userInput = input("Invalid input, try again: ").lower()

# """
#   # do things based on user response
#   while choice.lower() != "exit":
#     choice = input("Which way would you like to go? >>")

#     # valid response: go to the correct location
#     if choice.lower() in doors:
#       # doors[choice.lower()]()
#       return doors[choice.lower()]()
#     elif choice.lower() == "exit":
#       print("Too tough for you, eh? Good-bye then.")

#     # invalid response: ask them again
#     else:
#       print("I'm sorry, I did not understand.")
#       # exit()
#       return exit()
# """

def fakeDoor():
  print("Ha ha, you ran into a wall!")

def room1():
  description = "\nYou are in ROOM ONE"
  doors = {"north":fakeDoor, "east":room2, "south":room3, "west":fakeDoor}
  process_user_movement(description, doors)

# """
#   return process_user_movement(description, doors)
# """

def room2():
  description = "\nYou are in ROOM TWO"
  doors = {"north":fakeDoor, "east":fakeDoor, "south":room4, "west":room1}
  process_user_movement(description, doors)

# """
#   return process_user_movement(description, doors)
# """

def room3():
  description = "\nYou are in ROOM THREE"
  doors = {"north":room1, "east":room4, "south":fakeDoor, "west":fakeDoor}
  process_user_movement(description, doors)

# """
#   return process_user_movement(description, doors)
# """

def room4():
  description = "\nYou are in ROOM FOUR"
  doors = {"north":room2, "east":fakeDoor, "south":room5, "west":room3}
  process_user_movement(description, doors)

# """
#   return process_user_movement(description, doors)
# """

def room5():
  description = "\nYou are in ROOM FIVE"
  doors = {"north":room4, "east":fakeDoor, "south":fakeDoor, "west":theEnd}
  process_user_movement(description, doors)

# """
#   return process_user_movement(description, doors)
# """

def theEnd():
  print("\nWell done, you have conquered THE MAZE!\n")

def theStart():
  print("\nWelcome to THE MAZE. Dare to escape!")
  room1()

# """
#  currentRoom = room1()
#  while currentRoom != exit:
#    currentRoom = currentRoom()
#  currentRoom()
# """

theStart()



