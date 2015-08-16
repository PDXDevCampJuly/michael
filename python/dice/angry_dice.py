# ANGRY Dice is a real-time dice rolling microgame.
# https://boardgamegeek.com/boardgame/144790/ANGRY-dice
# >>>-------------------------------------------------->

from dice_class import Die

class AngryDice():
  """
  The logic and output to play a game of Angy Dice
  """

  def __init__(self):
    self.level = 1
    self.userInput_list = []
    self.die_a = Die(["1", "2", "ANGRY", "4", "5", "6"])
    self.die_b = Die(["1", "2", "ANGRY", "4", "5", "6"])


  def instructions(self):
    print("Welcome to Angry Dice! Roll the two dice until you get thru the 3 Stages!")
    print("Stage 1 you need to roll 1 & 2")
    print("Stage 2 you need to roll ANGRY & 4")
    print("Stage 3 you need to roll 5 & 6")
    print("You can lock a die needed for your current stage and")
    print("just roll the other one, but beware!")
    print("If you ever get 2 ANGRY's at once, you have to restart")
    print("to Stage 1! Also, you can never lock a 6! That's cheating!")
    print("To roll the dice, simply input the name of the die")
    print("you want to roll. Their names are a and b.\n")
    input("Press ENTER to start!\n")


  def print_results(self):
    print("-------------------------------")
    print("You rolled:")
    print("a = [  {}  ]".format(self.die_a))
    print("b = [  {}  ]".format(self.die_b))
    self.user_input()


  def user_input(self):
    """
    Take the user input and allow for the user to stay or roll
    """
    if self.level == 4:
      exit()

    userInput = ""
    while "a" not in userInput or "b" not in userInput:
      userInput = input("\nDecision: ")
      self.userInput_list.append(userInput)
      print(self.userInput_list)

      if "a" in userInput and "b" in userInput:
        self.die_a.roll()
        self.die_b.roll()
        self.test_input(self.die_a, self.die_b)
        break
      elif "a" in userInput:
        self.die_a.roll()
        self.test_input(self.die_a, self.die_b)
        break
      elif "b" in userInput:
        self.die_b.roll()
        self.test_input(self.die_a, self.die_b)
        break
      else:
        print("I do not understand, try again: ")

    self.print_results()


  def test_input(self, a, b):
    """
    Test the userInput for each roll to determine the status of game
    """
    a = self.die_a.currentValue
    b = self.die_b.currentValue
    userInput = self.userInput_list[-1] # test recent userInput

    # always test for a reset to level one
    if a == "ANGRY" and b == "ANGRY":
      print("\nWOW, you're ANGRY!")
      print("Time to go back to Stage 1!")
      self.level = 1
      return

    if self.level == 3 and (a == "6" or b == "6"):
      while (a == "6" and "a" not in userInput) or (b == "6" and "b" not in userInput):
        print("You're cheating! You cannot lock a 6! You cannot win until you reroll it!")
        self.print_results()
    self.test_stage(self.level)


  def test_stage(self, level):
    """
    Determine the current stage of the user
    """
    a = self.die_a.currentValue
    b = self.die_b.currentValue

    if self.level == 1:
      self.stage_1(a, b)

    elif self.level == 2:
      self.stage_2(a, b)

    else:
      self.stage_3(a, b)


  def stage_1(self, a, b):
    a = self.die_a.currentValue
    b = self.die_b.currentValue

    print("\nStage 1!")
    if (a == "1" and b == "2") or (a == "2" and b == "1"):
      self.level = 2
      print("\nStage 2!")


  def stage_2(self, a, b):
    a = self.die_a.currentValue
    b = self.die_b.currentValue

    print("\nStage 2!")
    if (a == "ANGRY" and b == "4") or (a == "4" and b == "ANGRY"):
      self.level = 3
      print("\nStage 3!")


  def stage_3(self, a, b):
    a = self.die_a.currentValue
    b = self.die_b.currentValue

    print("\nStage 3!")
    if (a == "5" and b == "6") or (a == "6" and b == "5"):
      print("\nStage 3!")
      print("-------------------------------")
      print("-------------------------------")
      print("You've won! Calm down!")
      self.level = 4


# if I am the global namespace, then I am in control
# otherwise, I will defer to whoever called me
if __name__ == "__main__":
  launchGame = AngryDice()
  launchGame.instructions()
  launchGame.print_results()

