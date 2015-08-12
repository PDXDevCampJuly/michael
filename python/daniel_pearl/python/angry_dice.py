from Dice2 import Die

class Angry_roll:
    def __init__(self):
        self.dice_a = Die([1,2,"angry",4,5,6]) #Creates dice a
        self.dice_b = Die([1,2,"angry",4,5,6]) #Creates dice b
        self.stage = 1
        self.prompt_user()

    def describe_game(self):
        print("Welcome to angry dice.")

    def prompt_user(self):
        #Tells user to press enter to continue
        input("Press Enter to begin ")

    def display(self,a,b):
        #Displays the sides of the die
        print("You rolled:")
        print("   a = [ {} ]".format(a))
        print("   b = [ {} ]".format(b))

    def roll_choice(self):
        #Prompts user to roll dice
        dice=input("Please choose which dice you'd like to roll (a or b). Type 'ab' to roll both die: ")
        return dice

    def roll_dice(self,a,b):

        dice = self.roll_choice()
        if dice == "a":
            if self.cheat(a,b,dice) == True:
                b = 0
            else:
                a = self.dice_a.roll()
        elif dice == "b":
            if self.cheat(a,b,dice) == True:
                a = 0
            else:
                b = self.dice_b.roll()
        elif dice == "ab":
            a = self.dice_a.roll()
            b = self.dice_b.roll()

        return a, b


    def count_stage(self,a,b):
        print("Stage {}".format(self.stage))
        if (a=="angry" and b=="angry"):
            print("Oh no! You've gone back to stage 1")
            a,b = 0,0
            return 1

        else:
            if self.stage == 1:
                if (a == 1 and b ==2) or (b == 1 and a == 2):
                    print("You are in stage 2")
                    return 2
                else:
                    return self.stage
            elif self.stage == 2:
                if (a == "angry" and b == 4) or (b == "angry" and a == 4):
                    print("You are in stage 3")
                    return 3
                else:
                    return self.stage
            elif self.stage == 3:
                if (a == 6 and b != 5):
                    a = 0
                    return self.stage
                elif (b == 6 and a != 5):
                    b = 0
                    return self.stage
                elif (a == 5 and b == 6) or (b == 5 and a == 6):
                    return 4
                    return self.stage
                else:
                    return self.stage

    def cheat(self, a,b, choice):
        if self.stage == 3 and a == 6 and b != 5 and choice == "b":
            print ("Cheater!")
            return True
        elif self.stage == 3 and b == 6 and a != 5 and choice == "a":
            print ("Cheater!")
            return True

    #Initiates Game
    def start(self):
        a=0
        b=0

        self.describe_game()
        while self.stage != 4:
            #Rolls dice

            a, b = self.roll_dice(a, b)
            self.display(a, b)
            self.stage = self.count_stage(a, b)

        print("You win! calm down")

aroll = Angry_roll()
aroll.start()
