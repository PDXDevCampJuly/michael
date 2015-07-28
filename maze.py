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


  # prompt the for what doors they want
  userInput = input("Choose a door: ").lower()

  # do things based on user response
  while True:
    # valid response: go to the correct location
    try:
      doors[userInput]()
      break

    # invalid response: ask them again
    except:
      userInput = input("Invalid input, try again: ").lower()

def room1():
  description = "\nYou are in ROOM ONE"
  doors = {"east": room2, "south": room3}
  process_user_movement(description, doors)

def room2():
  description = "\nYou are in ROOM TWO"
  doors = {"west": room1, "south": room4}
  process_user_movement(description, doors)

def room3():
  description = "\nYou are in ROOM THREE"
  doors = {"north": room1, "east": room4}
  process_user_movement(description, doors)

def room4():
  description = "\nYou are in ROOM FOUR"
  doors = {"north": room2, "south": room5, "west": room3}
  process_user_movement(description, doors)

def room5():
  description = "\nYou are in ROOM FIVE"
  doors = {"north": room4, "west": theEnd}
  process_user_movement(description, doors)

def theEnd():
  print("\nWell done, you have exited THE MAZE!\n")

def start():
  print("\nWelcome to THE MAZE. Dare to escape!")
  room1()

start()



