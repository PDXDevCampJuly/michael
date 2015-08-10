# this is a dice making module utilizing classes
# the user will have options to customize the make of each die
# ---------------------------------->

from random import choice

class Die():
  """
  makes a Die Class and returns a random face value from the roll()
  """

  def __init__(self, possibleValues):
    """
    make a new die based on the list passed by the user
    """
    self.possibleValues = possibleValues
    self.roll()

  def roll(self):
    """
    returns randomly selected face value
    """
    self.currentValue = choice(self.possibleValues)
    return self.currentValue

  def __repr__(self):
    """
    overrides the object style output and converts to actual
    values initially passed by the user
    """
    return self.currentValue

myDie = Die(["heart", "club", "diamond", "spade"])
print(myDie)



