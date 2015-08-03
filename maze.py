# This is a maze program
###########################

import random
import time

selectedItem = ""
selectedFakeDoor = ""
selectedRestrictedDoor = ""
fakeDoors_items ={}
inventory = []
userInput = ""
currentRoom = ""

# description: a description of the current room
# doors: dictionary with door:location sets
def process_user_movement(description, doors, currentRoom):

  global fakeDoors_items
  global inventory
  global userInput
  fakeDoors_items[selectedFakeDoor] = selectedItem

  # print the description of the current room
  print(description)

  # print the available doors
  print("Here are your options: ")
  for each_door in doors:
    print(">", each_door)

  # prompt the for what doors they want
  userInput = input("Choose a door: ").lower()

  # do things based on user response
  while userInput != "exit":

    # valid response: go to the correct location
    try:
      print("---> currentRoom:", currentRoom)
      # # print("user input:", userInput)
      # # print(currentRoom in selectedFakeDoor)
      # # print(userInput in selectedFakeDoor)
      # # print(currentRoom in selectedRestrictedDoor)
      # # print(userInput in selectedRestrictedDoor)

      # test for fake door with inventory item
      if currentRoom in selectedFakeDoor and userInput in selectedFakeDoor:
        if not selectedItem in inventory:
          inventory.append(selectedItem)
          # print(inventory)
          print("\nAdded to your inventory: {}".format(selectedItem))

      # test for restricted access and item in inventory
      if currentRoom in selectedRestrictedDoor and userInput in selectedRestrictedDoor:
        if selectedItem in inventory:
          print("Granted access for having the {}.".format(selectedItem))
        else:
          print("This door is restricted. You need a {}.".format(selectedItem))
          userInput = input("Try again: ").lower()
          continue

      if doors[userInput] == fakeDoor:
        fakeDoor()
        userInput = input("Try again: ").lower()
      else:
        doors[userInput]()
        break

      if userInput == "exit":
        print("shutting down...")
        time.sleep(2)
        print("bye.")
        exit()

    # invalid response: ask them again
    except:
      userInput = input("Invalid input, try again: ").lower()

def fakeDoor():
  print("You have found a fake door.")

# selects are random item
def selectItem():
  global selectedItem
  selectedItem = random.choice(['SKELETON KEY'])
  # print(selectedItem)

# selects the fake door to hold the item
def selectFakeDoor():
  global selectedFakeDoor
  selectedFakeDoor = random.choice(['BLUE_north', 'BLUE_west', "RED_north", "RED_east", "GREEN_south", "GREEN_west", "YELLOW_east", "ORANGE_east", "ORANGE_south"])
  # print(selectedFakeDoor)

# selects the door that needs the random item
def selectRestrictedDoor():
  global selectedRestrictedDoor
  selectedRestrictedDoor = random.choice(['BLUE_east', 'BLUE_south', "RED_south", "RED_west", "GREEN_north", "GREEN_east", "YELLOW_north", "YELLOW_south", "YELLOW_west", "ORANGE_west"])
  # print(selectedRestrictedDoor)

def room1():
  global currentRoom
  currentRoom = "BLUE"
  description = "\nYou are in the {} ROOM".format(currentRoom)
  doors = {'north': fakeDoor, 'east': room2, 'south': room3, 'west': fakeDoor}
  process_user_movement(description, doors, currentRoom)

# """
#   return process_user_movement(description, doors)
# """

def room2():
  global currentRoom
  currentRoom = "RED"
  description = "\nYou are in the {} ROOM".format(currentRoom)
  doors = {'north': fakeDoor, 'east': fakeDoor, 'south': room4, 'west': room1}
  process_user_movement(description, doors, currentRoom)

# """
#   return process_user_movement(description, doors)
# """

def room3():
  global currentRoom
  currentRoom = "GREEN"
  description = "\nYou are in the {} ROOM".format(currentRoom)
  doors = {'north': room1, 'east': room4, 'south': fakeDoor, 'west': fakeDoor}
  process_user_movement(description, doors, currentRoom)

# """
#   return process_user_movement(description, doors)
# """

def room4():
  global currentRoom
  currentRoom = "YELLOW"
  description = "\nYou are in the {} ROOM".format(currentRoom)
  doors = {'north': room2, 'east': fakeDoor, 'south': room5, 'west': room3}
  process_user_movement(description, doors, currentRoom)

# """
#   return process_user_movement(description, doors)
# """

def room5():
  global currentRoom
  currentRoom = "ORANGE"
  description = "\nYou are in the {} ROOM".format(currentRoom)
  doors = {'north': room4, 'east': fakeDoor, 'south': fakeDoor, 'west': theEnd}
  process_user_movement(description, doors, currentRoom)

# """
#   return process_user_movement(description, doors)
# """

def theEnd():
  print("\nWell done, you have conquered THE MAZE!")

def theStart():
  print("\nWelcome to THE MAZE. Dare to escape!\n")
  selectItem()
  selectFakeDoor()
  selectRestrictedDoor()
  print("---> {} in the {}".format(selectedItem, selectedFakeDoor))
  print("---> Restricted:", selectedRestrictedDoor)
  room1()

theStart()



