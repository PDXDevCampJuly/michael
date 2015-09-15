from random import choice

class Die:

	def __init__(self, possableValue):
		"""
		This fution makes the possableValue which is all values the person can roll.
		Then it makes the currentValue a random value from possableValue.

		"""
		self.possableValue = possableValue
		self.currentValue = choice(possableValue)


	def roll(self):
		"""
		This funtion will take the imput that person puts (so new_die) and puts it in currentValue.
		Then it takes a random value from that list and returns it
		"""
		self.currentValue = choice(self.possableValue)
		return self.currentValue


	def __repr__(self):
		"""
		This funtion will print what the person rolled
		"""
		return self.currentValue
		#pass

new_die = Die([1, 2, "angry face", 4, 5, 6])