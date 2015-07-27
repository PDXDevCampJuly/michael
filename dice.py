# this is a dice making module
# ---------------------------------->

from random import randint

def roll(max):
  theRoll = randint(1, max)
  print("The roll is:", theRoll)

roll(550)
roll(10550)
roll(4922)
