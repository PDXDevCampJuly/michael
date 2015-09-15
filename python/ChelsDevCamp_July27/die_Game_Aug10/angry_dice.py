from random import choice

from Die_two_point_whoa import Die

class Angry_dice:

	def __init__(self):
		self.a = Die(["1","2","ANGRY","4","5","6"])
		self.b = Die(["1","2","ANGRY","4","5","6"])
		self.both_die =  [self.a.currentValue , self.b.currentValue]
		self.current_stage = 1
		self.stage_1_goal = ["1","2"]
		self.stage_2_goal = ["ANGRY","4"]
		self.stage_3_goal = ["5","6"]	
		# both_values = [self.a.currentValue, self.b.currentValue]



	def start_game(self):
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
		self.turn()




	def score(self):
		current_score = self.both_die

	def turn(self):
		self.print_turn()

		self.check_stage()

		self.check_angry()
		# Get Input
		roll = input("Roll dice: ")

		# Eval input
		if self.a.currentValue == "6":
			if 'a' not in roll:
				self.cheat_a()

		if self.b.currentValue == "6":
			if 'b' not in roll:
				self.cheat_b()

		if 'a' in roll:
			self.a.roll()
		if 'b' in roll:
			self.b.roll()


	def print_turn(self):
		print("------------------------------------------------------------------------------------------------------")
		print("You rolled:")
		print("   a = [" + str(self.a) + "]")
		print("   b = [" + str(self.b) + "]")
		print("You are in Stage " + str(self.current_stage))

	def check_stage(self):
		if self.current_stage == 1 and self.a.currentValue in self.stage_1_goal:
			if self.b.currentValue in self.stage_1_goal:
				if self.b.currentValue != self.a.currentValue:
					print("You got it! Your next goal is angry and 4")
					self.current_stage += 1

		if self.current_stage == 2 and self.a.currentValue in self.stage_2_goal:
			if self.b.currentValue in self.stage_2_goal:
				if self.b.currentValue != self.a.currentValue:
					print("You got it! Your next goal is 5 and 6")
					self.current_stage  +=1
		
		if self.current_stage == 3 and self.a.currentValue in self.stage_3_goal:
			if self.b.currentValue in self.stage_3_goal:
				if self.b.currentValue != self.a.currentValue:
					print("You've won! Calm down!")
					exit()


	def check_angry(self):
		if self.a.currentValue == "ANGRY":
			if self.b.currentValue == "ANGRY":
				self.current_stage = 1

	


	def cheat_a(self):
		print("You're cheating! You cannot lock that number!")
		print("Rerolling for you:")
		self.a.roll()

		self.turn()

	def cheat_b(self):
		print("You're cheating! You cannot lock that number!")
		print("Rerolling for you:")
		self.b.roll()

		self.turn()







