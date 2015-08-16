# ANGRY Dice is a real-time dice rolling microgame.
# https://boardgamegeek.com/boardgame/144790/ANGRY-dice
# >>>-------------------------------------------------->

from dice_class import Die

class AngryDice():
  """
  A program that lets a Single Player play Angry Dice
  """

  def __init__(self):
    """
    Intializes the AngyDice class
    """

    self.stage = 1
    self.userInput = ""
    self.a = Die(["1", "2", "ANGRY", "4", "5", "6"])
    self.b = Die(["1", "2", "ANGRY", "4", "5", "6"])


  def instructions(self):
    """
    Output instructions for the user
    """

    text = ""
    text += "Welcome to Angry Dice! Roll the two dice until you get thru the 3 Stages!\n"
    text += "Stage 1 you need to roll 1 & 2\n"
    text += "Stage 2 you need to roll ANGRY & 4\n"
    text += "Stage 3 you need to roll 5 & 6\n"
    text += "You can lock a die needed for your current stage and\n"
    text += "just roll the other one, but beware!\n"
    text += "If you ever get 2 ANGRY's at once, you have to restart\n"
    text += "to Stage 1! Also, you can never lock a 6! That's cheating!\n"
    text += "To roll the dice, simply input the name of the die\n"
    text += "you want to roll. Their names are a and b.\n"
    print(text)
    input("Press ENTER to start!\n")


  def play(self):
    """
    Driving function for the entire game
    """

    # ! need to extract get_user_input() call under print_results()
    # ! need to pull driving type function out of get_user_input()

    self.instructions()
    self.print_results()

    # self.get_user_input()

    # while True:
      # if "a" in self.userInput:
      #   self.a.roll()

    """
    Take the user input and allow for the user to stay or roll
    """

    # stage 4 exits the game
    if self.stage == 4:
      exit()

    # maintains the game flow until user wins depending on userInput
    while True:
      self.userInput = input("\nRoll dice: ")


      if "a" in self.userInput and "b" in self.userInput:
        self.a.roll()
        self.b.roll()
        self.check_input(self.a, self.b)
        self.print_results()

      elif "a" in self.userInput:
        self.a.roll()
        self.check_input(self.a, self.b)
        self.print_results()

      elif "b" in self.userInput:
        self.b.roll()
        self.check_input(self.a, self.b)
        self.print_results()

      else:
        print("I do not understand, try again: ")


  def print_results(self):
    """
    Outputs status of the game
    """

    print("\nYou are in Stage {}".format(self.stage))
    print("-------------------------------")
    print("You rolled:")
    print("a = [  {}  ]".format(self.a))
    print("b = [  {}  ]".format(self.b))
    # print("\n {}".format(next_action))
    # self.get_user_input() #

  # def next_action(self):


  def check_input(self, a, b):
    """
    Check the userInput for each roll to determine the status of game.
    Determines if the user rolls 2 Angrys.
    Determines if the user is cheating.
    """

    a = self.a.currentValue
    b = self.b.currentValue
    userInput = self.userInput[-1] # check recent userInput

    # always check for a reset to stage one
    if a == "ANGRY" and b == "ANGRY":
      print("\nWOW, you're ANGRY!")
      print("Time to go back to Stage 1!\n")
      self.stage = 1
      return

    # is the user cheating by holding a "6" on Level 3
    if self.stage == 3 and (a == "6" or b == "6"):
      while (a == "6" and "a" not in userInput) or (b == "6" and "b" not in userInput):
        print("You're cheating! You cannot lock a 6! You cannot win until you reroll it!")
        self.print_results()
    self.check_stage(self.stage)


  def check_stage(self, stage):
    """
    Determine the current stage of the user
    """

    a = self.a.currentValue
    b = self.b.currentValue

    if self.stage == 1:
      self.stage_1(a, b)

    elif self.stage == 2:
      self.stage_2(a, b)

    else:
      self.stage_3(a, b)


  def stage_1(self, a, b):
    """
    Logic for Stage 1 after call from check_stage()
    """

    a = self.a.currentValue
    b = self.b.currentValue

    if (a == "1" and b == "2") or (a == "2" and b == "1"):
      self.stage = 2


  def stage_2(self, a, b):
    """
    Logic for Stage 2 after call from check_stage()
    """

    a = self.a.currentValue
    b = self.b.currentValue

    if (a == "ANGRY" and b == "4") or (a == "4" and b == "ANGRY"):
      self.stage = 3


  def stage_3(self, a, b):
    """
    Logic for Stage 3 after call from check_stage()
    """

    a = self.a.currentValue
    b = self.b.currentValue

    if (a == "5" and b == "6") or (a == "6" and b == "5"):
      print("-------------------------------")
      print("-------------------------------")
      print("You've won! Calm down!")
      self.stage = 4 # exits the game


# if I am the global namespace, then I am in control
# otherwise, I will defer to whoever called me
if __name__ == '__main__':
  game = AngryDice()
  game.play()

