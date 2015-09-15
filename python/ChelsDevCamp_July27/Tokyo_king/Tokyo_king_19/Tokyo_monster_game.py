"""The whole Monster game"""

class Monster:

    def __init__(self):
        """"""
        self.name = "Fwankie"
        self.current_status = 1
        self.status = {1:["Out of Tokyo"],
                       2:["in Tokyo"],
                       3:["K.O'd"],
                       4:["WINNING"]}
        self.health = 10
        self.victory_points = 0
        self.In_Tokyo = False
        self.real_status = self.status[self.current_status]




    def reset(self):
        """ resets to inital stats"""
        # TODO find an easier way to do this
        self.current_status = 1
        self.health = 10
        self.victory_points = 0

    def in_tokyo(self):
        """ Set's in_tokyo to true if current_status is two"""
        #Works
        self.In_Tokyo = False
        if self.current_status == 2:
            self.In_Tokyo = True


    def flee(self):
        """ Prompts monster to see if they want to flee tokyo. If they do return True, if they dont return False"""
        #Works
        ask = input("Do you want to flee? ")

        if ask == "yes":
            return False
        if ask == "no":
            return True

    def heal(self, heal_roll):
        """ Adds int to heath as long as it's greater than 0 and less than 10"""
        #Half works
        # TODO findout a way to make it stop at 10
        if heal_roll > 0 and heal_roll < 10:
            self.health += heal_roll
        if heal_roll + heal_roll > 10:
            self.health = 10


    def attack(self, attack_roll):
        """ Take away int from Monsters health. return Monsters health. If health is less than or equals zero set status
         to 'K.O.'d"""

        self.health -= attack_roll

    def score(self):
        """ add passed int into victory_points and return victory points. if victory points are greatherthan or equal to
         20 set statuse to 'WINNING'"""
        # TODO make a while loop that continues until you either K.O or win.(Where it would update status(Maybe not in this-
        # TODO function..) and than print's that you lost or won and exits(Maybe ask if they want to play again)
