# ANGRY Dice is a real-time dice rolling microgame.
# https://boardgamegeek.com/boardgame/144790/ANGRY-dice
# >>>-------------------------------------------------->

from dice_class import Die

die_a = Die(["1", "2", "ANGRY", "4", "5", "6"])
die_b = Die(["1", "2", "ANGRY", "4", "5", "6"])

class Launch():

  def __init__(self, die_a, die_b):
    self.die_a = die_a
    self.die_b = die_b
    print(die_a)
    print(die_b)
    user = Player()
    self.instructions()

  def instructions(self):
    print("Welcome to the ANGRY Dice Arena.")
    print("ANGRY Dice is a real-time dice rolling microgame.")
    print("The object is to be the first to six by rolling your dice in ascending order pairs.")
    print("You and your competitor each have two dice they can roll.")
    print("You can lock a die (except a 6), if it rolls to something they you will need.")
    print("You are required to start at the beginning if you ever roll double ANGRY Faces (the 3).")
    print("The game consists of three rounds.")
    print("Round 1: Roll a 1 and a 2.")
    print("Round 2: Roll an ANGRY (the 3) and a 4.")
    print("Round 3: Roll a 5 then a 6.")
    print("Meet the requirements for each round and move on.")
    input("Good luck {}. Press Enter to continue... ".format(self.player_name))

class Player():

  def __init__(self):
    self.get_name()

  def get_name(self):
    self.player_name = input("Input your name: ")

Launch(die_a, die_b)
player = Player()

