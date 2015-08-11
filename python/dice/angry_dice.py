# ANGRY Dice is a real-time dice rolling microgame.
# https://boardgamegeek.com/boardgame/144790/ANGRY-dice
# >>>-------------------------------------------------->

from dice_class import Die

class Launch():
  """
  Launches the game of ANGRY dice
  """

  def __init__(self):
    self.die_a = Die(["1", "2", "ANGRY", "4", "5", "6"])
    self.die_b = Die(["1", "2", "ANGRY", "4", "5", "6"])
    self.instructions()
    self.initial_values()
    # self.test_stage(die_a, die_b)

  def instructions(self):
    print("Welcome to Angry Dice! Roll the two dice until you get thru the 3 Stages!")
    print("Stage 1 you need to roll 1 & 2")
    print("Stage 2 you need to roll ANGRY & ")
    print("Stage 3 you need to roll 5 & 6")
    print("You can lock a die needed for your current stage and just roll the other one, but beware!")
    print("If you ever get 2 ANGRY's at once, you have to restart to Stage 1! Also, you can never lock a 6! That's cheating!")
    print("To roll the dice, simply input the name of the die you want to roll. Their names are a and b.")
    input("Press ENTER to start! ")

  def initial_values(self):
    print("-------------------------------\n")
    print("Initial Values:")
    print("a = ", self.die_a)
    print("b = ", self.die_b)
    print("-------------------------------\n")
    self.user_input()

  def print_results(self):
    print("-------------------------------\n")
    print("You rolled:")
    print("a = ", self.die_a)
    print("b = ", self.die_b)
    print("-------------------------------\n")
    self.user_input()

  def user_input(self):
    """
    Take the user input and allow for the user to stay or roll
    """
    userInput_list = []
    userInput = ""
    while "a" not in userInput or "b" not in userInput:
      userInput = input("Decision: ")
      userInput_list.append(userInput)
      if "a" in userInput and "b" in userInput:
        self.die_a.roll()
        self.die_b.roll()
        self.test_stage(self.die_a, self.die_b)
        break
      elif "a" in userInput:
        self.die_a.roll()
        self.test_stage(self.die_a, self.die_b)
        break
      elif "b" in userInput:
        self.die_b.roll()
        self.test_stage(self.die_a, self.die_b)
        break
      else:
        print("I do not understand, try again: ")
    self.print_results()


  def test_stage(self, die_a, die_b):
    """
    Test the userInput for each roll to determine the status of game
    """
    a = self.die_a.currentValue
    b = self.die_b.currentValue
    # print(type(a))
    # print(type(b))

    # always test for a reset to level one
    if a == "ANGRY" and b == "ANGRY":
      print("reset game")

    # stage 1
    if (a == "1" and b == "2") or (a == "2" and b == "1"):
      print("move on to stage 2")

  # def stage_2(die_a, die_b):
  #   if a == 3 and b == 4:


  # def stage_3(die_a, die_b):
  #   if a == 5 and b == 6:




launchGame = Launch()

