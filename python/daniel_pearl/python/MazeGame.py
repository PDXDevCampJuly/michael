def start():
    print ("You are trapped in a room. ", end="")
    room0()

def process_user_movement(description, doors):
    #Print description of room
    print(description, end=" ")

    #Print available doors
    print("There are %s doors in the room:" %len(doors))
    for key in doors.keys():
        print (str(key)+" door")
    #print(*list(doors.keys()), sep=", ")

    #Prompt for choice
    choice = 0
    while choice != "exit":
        choice = input("Which direction would you like to go? ")

    #Valid input is a key to the doors dictionary
        if choice in doors:
            doors[choice]()
    #If invalid prompt for choice again
        else:
            print("Invalid entry.")

def room0():
    #Description
    description = "This room is large."
    #doors
    doors = {"East":room1, "South":room2}
    #where those doors go
    process_user_movement(description, doors)

def room1():
    #Description
    description = "This room is cramped."
    #doors
    doors = {"West":room0, "South":room3}
    #where those doors go
    process_user_movement(description, doors)

def room2():
    #Description
    description = "This room is musky."
    #doors
    doors = {"North":room0, "East":room3}
    #where those doors go
    process_user_movement(description, doors)

def room3():
    #Description
    description = "This room is moldy."
    #doors
    doors = {"North":room1, "East":room4, "West":room2}
    #where those doors go
    process_user_movement(description, doors)

def room4():
    #Description
    description = "Congratulations! You've made it outside!"
    choice = "exit"

start()
