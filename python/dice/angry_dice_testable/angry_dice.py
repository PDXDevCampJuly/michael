# ANGRY Dice is a real-time dice rolling microgame.
# https://boardgamegeek.com/boardgame/144790/ANGRY-dice
# >>>-------------------------------------------------->

from dice_class import Die


class AngryDice():
    """ A program that lets a Single Player play Angry Dice """

    def __init__(self):
        """ Initializes the AngyDice class """

        self.die_a = Die(["1", "2", "ANGRY", "4", "5", "6"])
        self.die_b = Die(["1", "2", "ANGRY", "4", "5", "6"])
        self.stage = 1
        self.userInput = ""
        self.outcome = ""
        self.finalCheck = False  # breaks the main method upon a win

    def instructions(self):
        """ Output instructions for the user """

        text = "\nWelcome to Angry Dice! Roll the two dice \n"
        text += "until you get through the 3 Stages!\n"
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
        """ Output status of the game """

        print("\nYou are in Stage {}".format(self.stage))
        print("-------------------------------")
        print("You rolled:")
        print("a = [  {}  ]".format(self.die_a))
        print("b = [  {}  ]".format(self.die_b))
        print("{}".format(self.outcome))

    def main(self):
        """ Driving function for the entire game """

        self.instructions()
        self.check_stage() # in the case the game starts with roll [1, 2]
        self.print_results()

        # maintains the game flow until user wins depending on userInput
        while not self.finalCheck:
            self.outcome = ""  # resets the outcome statement
            self.userInput = input("Roll dice: ").lower() + "\n"
            self.check_user_input()
            self.check_stage()
            self.print_results()

    def check_user_input(self):
        """ Check the userInput and if the user is cheating. """

        a = self.die_a.currentValue
        b = self.die_b.currentValue
        valid_userInput = False  # valid input by the user

        # check if the user is cheating
        # call the is_cheating helper function
        is_cheating = self.cheating_status(a, b)

        # if a is input by the user
        if "a" in self.userInput and is_cheating is False:
            self.die_a.roll()
            valid_userInput = True

        # if b is input by the user
        if "b" in self.userInput and is_cheating is False:
            self.die_b.roll()
            valid_userInput = True

        # if a or b not rolled because of incorrect input by the user
        if not valid_userInput and is_cheating is False:
            self.outcome = "\nI do not understand, try again...\n"

    def cheating_status(self, a, b):
        """ Helper for check_userInput: cheating if level 3 currentValue 6 """

        if self.stage == 3 and (a == "6" or b == "6"):
            if (a == "6" and "a" not in self.userInput) or \
                    (b == "6" and "b" not in self.userInput):
                self.outcome = \
                    ("\nYou're cheating! You cannot lock a 6!\n"
                     "You cannot win until you re-roll it!\n")
                return True
        return False

    def check_stage(self):
        """ Determine the current stage of the user """

        a = self.die_a.currentValue
        b = self.die_b.currentValue

        # check for 2 'Angrys', which resets to stage one
        if a == "ANGRY" and b == "ANGRY":
            self.stage = 1
            self.outcome = \
                ("\nWOW, you're ANGRY!\n"
                 "Time to go back to Stage 1!\n")

        # if stage 1, call the stage_1 helper function
        if self.stage == 1:
            self.stage_1(a, b)

        # if stage 2, call the stage_2 helper function
        elif self.stage == 2:
            self.stage_2(a, b)

        # if stage 3, call the stage_3 helper function
        else:
            self.stage_3(a, b)

    def stage_1(self, a, b):
        """ Helper for check_stage: Logic for Stage 1 """

        if (a == "1" and b == "2") or (a == "2" and b == "1"):
            self.stage = 2
            self.outcome = "\n>>> Stage 1 completed!\n"

    def stage_2(self, a, b):
        """ Helper for check_stage: Logic for Stage 2 """

        if (a == "ANGRY" and b == "4") or (a == "4" and b == "ANGRY"):
            self.stage = 3
            self.outcome = "\n>>> Stage 2 completed!\n"

    def stage_3(self, a, b):
        """ Helper for check_stage: Logic for Stage 3 """

        if (a == "5" and b == "6") or (a == "6" and b == "5"):
            self.outcome = \
                ("\n-------------------------------"
                 "\n-------------------------------"
                 "\nYou've won! Calm down!\n")
            self.finalCheck = True


if __name__ == '__main__':
    game = AngryDice()
    game.main()
