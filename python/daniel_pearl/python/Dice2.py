from random import choice

class Die:
    def __init__(self, listSides):
        self.currentValue = listSides[0] #side of dice rolled
        self.possibleValues = listSides  #potential sides of dice
    def roll(self):
        #randomly selects an index from the list
        self.currentValue = choice(self.possibleValues)
        return self.currentValue
    def __repr__(self):
        return self.currentValue

# Catch list of values for dice
#new_die = Die(["hearts", "clubs", "diamond"])
#print(new_die.roll())
