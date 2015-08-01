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
      # print(selectedItem)
      print("\ndoor with item:", selectedFakeDoor)
      print("restricted door:", selectedRestrictedDoor, "\n")
      # print("current room:", currentRoom)
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
  selectedFakeDoor = random.choice(['BLUE_north_fake', 'BLUE_west_fake', "RED_north_fake", "RED_east_fake", "GREEN_south_fake", "GREEN_west_fake", "YELLOW_east_fake", "ORANGE_east_fake", "ORANGE_south_fake"])
  # print(selectedFakeDoor)

# selects the door that needs the random item
def selectRestrictedDoor():
  global selectedRestrictedDoor
  selectedRestrictedDoor = random.choice(['BLUE_east', 'BLUE_south', "RED_south", "RED_west", "GREEN_north", "GREEN_east", "YELLOW_north", "YELLOW_south", "YELLOW_west", "ORANGE_north", "ORANGE_west"])
  # print(selectedRestrictedDoor)

def room1():
  description = "You are in the {} ROOM".format("BLUE")
  doors = {'north': fakeDoor, 'east': room2, 'south': room3, 'west': fakeDoor}
  currentRoom = "blue"
  process_user_movement(description, doors, currentRoom)

# """
#   return process_user_movement(description, doors)
# """

def room2():
  description = "You are in the {} ROOM".format("RED")
  doors = {'north': fakeDoor, 'east': fakeDoor, 'south': room4, 'west': room1}
  currentRoom = "red"
  process_user_movement(description, doors, currentRoom)

# """
#   return process_user_movement(description, doors)
# """

def room3():
  description = "You are in the {} ROOM".format("GREEN")
  doors = {'north': room1, 'east': room4, 'south': fakeDoor, 'west': fakeDoor}
  currentRoom = "blue"
  process_user_movement(description, doors, currentRoom)

# """
#   return process_user_movement(description, doors)
# """

def room4():
  description = "You are in the {} ROOM".format("YELLOW")
  doors = {'north': room2, 'east': fakeDoor, 'south': room5, 'west': room3}
  currentRoom = "yellow"
  process_user_movement(description, doors, currentRoom)

# """
#   return process_user_movement(description, doors)
# """

def room5():
  description = "You are in the {} ROOM".format("ORANGE")
  doors = {'north': room4, 'east': fakeDoor, 'south': fakeDoor, 'west': theEnd}
  currentRoom = "orange"
  process_user_movement(description, doors, currentRoom)

# """
#   return process_user_movement(description, doors)
# """

def theEnd():
  print("\nWell done, you have conquered THE MAZE!\n")

def theStart():
  print("\nWelcome to THE MAZE. Dare to escape!\n")
  selectItem()
  selectFakeDoor()
  selectRestrictedDoor()
  room1()

theStart()



