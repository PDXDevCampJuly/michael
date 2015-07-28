# this is a dice making module
# max is the max of the range
# it will run the function roll(max) numOfDice times
# ---------------------------------->

from random import randint

def roll(max):
  r = randint(1, max)
  print(r)
  return r

def roll_a_bunch(max, numOfDice):
  rolls = []
  for i in range(numOfDice):
    rolls.append(roll(max))

  return rolls

def roll_distro(max, numOfDice=4):
  # roll a bunch of die or number of times
  rolls = roll_a_bunch(max, numOfDice)

  distribution = {}

  # count what is rolled
  # if key in dict: return dict[key] else: return default
  for each in rolls:
    currentCount = distribution.get(each, 0)
    print("Current count of", each, ":", currentCount)
    currentCount += 1
    distribution[each] = currentCount

  output = ""
  for roll in distribution:
    output += "Number " + str(roll) + " was rolled " + str(distribution[roll]) + " times\n"

  print(output)










