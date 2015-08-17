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

    self.die_a = Die(["1", "2", "ANGRY", "4", "5", "6"])
    self.die_b = Die(["1", "2", "ANGRY", "4", "5", "6"])
    self.stage = 1
    self.userInput = ""
    self.outcome = ""
    self.finalCheck = False


  def instructions(self):
    """
    Output instructions for the user
    """

    text = "\nWelcome to Angry Dice! Roll the two dice until you get thru the 3 Stages!\n"
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
    input("Press ENTER to start! ") + "\n"


  def print_results(self):
    """
    Output status of the game
    """

    print("\nYou are in Stage {}".format(self.stage))
    print("-------------------------------")
    print("You rolled:")
    print("a = [  {}  ]".format(self.die_a))
    print("b = [  {}  ]".format(self.die_b))
    print("{}".format(self.outcome))


  def main(self):
    """
    Driving function for the entire game
    """

    # ! need to extract get_user_input() call under print_results()
    # ! need to pull driving type function out of get_user_input()

    self.instructions()
    self.print_results()


    # maintains the game flow until user wins depending on userInput
    while self.finalCheck == False:
      self.outcome = "" # resets the outcome statement
      self.userInput = input("Roll dice: ") + "\n"
      self.check_userInput(self.die_a, self.die_b)
      self.check_stage()
      self.print_results()


  def check_userInput(self, a, b):
    """
    Check the userInput for each roll to determine the status of game.
    Determines if the user rolls 2 Angrys.
    Determines if the user is cheating.
    """

    a = self.die_a.currentValue
    b = self.die_b.currentValue
    invalid_userInput = True # invalid input by the user

    # is the user cheating by holding a "6" on Level 3
    if self.stage == 3 and (a == "6" or b == "6"):
      if (a == "6" and "a" not in self.userInput) or (b == "6" and "b" not in self.userInput):
        self.outcome = \
          ("\nYou're cheating! You cannot lock a 6!\n"
          "You cannot win until you reroll it!\n")
        return

    if "a" in self.userInput:
      self.die_a.roll()
      invalid_userInput = False

    if "b" in self.userInput:
      self.die_b.roll()
      invalid_userInput = False

    # if a or b not rolled because of incorrect input by the user
    if invalid_userInput:
      self.outcome = "\nI do not understand, try again...\n"


  def check_stage(self):
    """
    Determine the current stage of the user
    """

    a = self.die_a.currentValue
    b = self.die_b.currentValue

    # check for 2 Angrys, which resets to stage one
    if a == "ANGRY" and b == "ANGRY":
      self.stage = 1
      self.outcome = \
        ("\nWOW, you're ANGRY!\n"
        "Time to go back to Stage 1!\n")

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

    a = self.die_a.currentValue
    b = self.die_b.currentValue

    if (a == "1" and b == "2") or (a == "2" and b == "1"):
      self.stage = 2
      self.outcome = "\n>>> Stage 1 completed!\n"


  def stage_2(self, a, b):
    """
    Logic for Stage 2 after call from check_stage()
    """

    a = self.die_a.currentValue
    b = self.die_b.currentValue

    if (a == "ANGRY" and b == "4") or (a == "4" and b == "ANGRY"):
      self.stage = 3
      self.outcome = "\n>>> Stage 2 completed!\n"


  def stage_3(self, a, b):
    """
    Logic for Stage 3 after call from check_stage()
    """

    a = self.die_a.currentValue
    b = self.die_b.currentValue

    if (a == "5" and b == "6") or (a == "6" and b == "5"):
      self.outcome = \
      ("\n-------------------------------"
      "\n-------------------------------"
      "\nYou've won! Calm down!\n")
      self.finalCheck = True


# if I am the global namespace, then I am in control
# otherwise, I will defer to whoever called me
if __name__ == '__main__':
  game = AngryDice()
  game.main()

