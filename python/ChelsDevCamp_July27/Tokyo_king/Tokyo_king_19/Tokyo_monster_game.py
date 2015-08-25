class Monster:

    def __init__(self):
        self.name = "Fwankie"
        self.current_status = 1
        self.status = {1:["Out of Tokyo"],
                       2:["in Tokyo"],
                       3:["K.O'd"],
                       4:["WINNING"]}
        self.health = 10
        self.victory_points = 0
        self.in_tokyo = False
        self.real_status = self.status[self.current_status]




    def reset(self):
        """ resets to inital stats"""
        #TODO find an easier way to do this
        self.current_status = 1
        self.health = 10
        self.victory_points = 0

    def in_tokyo(self):
        """ Set's in_tokyo to true if current_status is two"""

        self.in_tokyo = False
        if self.current_status == 2:
            self.in_tokyo = True



    def flee(self):
        """ Prompts monster to see if they want to flee tokyo. If they do return True, if they dont return False"""

        self.ask = input("Do you want to flee? ")

        if self.ask == "yes":
            self.current_status = 1
        if self.ask == "no":
            self.current_status = 2

    def heal(self):
        """ Adds int to heath as long as it's greater than 0 and less than 10"""


    def attack(self):
        """ Take away int from Monsters health. return Monsters health. If health is less than or equals zero set status to 'K.O.'d"""

    def score(self):
        """ add passed int into victory_points and return victory points. if victory points are greatherthan or equal to 20 set statuse to 'WINNING'"""
