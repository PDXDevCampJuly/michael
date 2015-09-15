from Die_two_point_whoa import Die

class Angry_dice:


	def __init__(self):
		self.die_a = Die(["1","2","ANGRY","4","5","6"])
		self.die_b = Die(["1","2","ANGRY","4","5","6"])
		self.current_stage = 1
		self.stage_goals = {1:["1","2"],
							2:["ANGRY", "4"],
							3:["5","6"]}
		self.cheating = False


	def main(self):
		print("------------------------------------------------------------------------------------------------------")
		print("Welcome to Angry Dice!")
		print("------------------------------------------------------------------------------------------------------")
		print("Roll the two dice until you get thru the 3 Stages!")
		print("Stage 1 you need to roll 1 & 2")
		print("Stage 2 you need to roll ANGRY & 4")
		print("Stage 3 you need to roll 5 & 6")
		print("You can lock a die needed for your current stage and just roll the other one, but beware!")
		print("If you ever get 2 ANGRY's at once, you have to restart to Stage 1!")
		print("Also, you can never lock a 6! That's cheating!")
		print("To roll the dice, simply input the name of the die you want to roll.")
		print("Their names are a and b.")
		print("\n")
		input("press ENTER to start!")
		print("------------------------------------------------------------------------------------------------------")
		self.check_stage()
		self.check_angry()
		while self.current_stage < 4:
			self.turn()
		else: print("You've won! Calm down!")
		exit()




	def turn(self):

		# Get Input
		roll = input("Roll dice: ")

		# Eval input
		self.is_cheat(roll)

		if 'a' in roll:
			self.die_a.roll()
		if 'b' in roll:
			self.die_b.roll()


		self.check_stage()

		self.check_angry()

		self.print_turn()


	def print_turn(self):
		print("------------------------------------------------------------------------------------------------------")
		print("You rolled:")
		print("   a = [" + str(self.die_a) + "]")
		print("   b = [" + str(self.die_b) + "]")
		print("You are in Stage " + str(self.current_stage))


	def check_stage(self):
		self.goals = self.stage_goals[self.current_stage]

		if self.die_a.currentValue in self.goals and self.die_b.currentValue in self.goals and self.cheating == False:
			if self.die_a.currentValue != self.die_b.currentValue:
				self.current_stage +=1


	def check_angry(self):
		if self.die_a.currentValue == "ANGRY":
			if self.die_b.currentValue == "ANGRY":
				self.current_stage = 1
				print("You're very angry, you need to calm down")


	def is_cheat(self, roll):
		self.cheating = False
		if self.die_a.currentValue == "6" and self.current_stage == 3:
			if 'a' not in roll:
				print("You're cheating! You cannot lock a six!")
				self.cheating = True

		if self.die_b.currentValue == "6" and self.current_stage == 3:
			if 'b' not in roll:
				print("You're cheating! You cannot lock a six!")
				self.cheating = True



if __name__ == '__main__':
	test_game = Angry_dice()
	test_game.main()




