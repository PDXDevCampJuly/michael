from random import shuffle

class Card:
    """
    Make an individual card.
    """
    dictionary = {
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "Jack": 10,
        "Queen": 10,
        "King": 10,
        "Ace": 11
    }

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.int_value = self.dictionary[value]

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

class Deck:
    """
    Make a Deck from the Class class and actions for the Deck
    """
    def __init__(self):
        self.makeDeck()

    # for each item in 'values' list, it compares to the dictionary and retrieves the value
    def makeDeck(self):
        self.deck = []
        suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
        values = ["two","three","four","five","six","seven","eight","nine","ten","Jack", "Queen", "King","Ace"]

        # fills in deck completing four suits of 13 cards
        for i in suits:
            for j in values:
                self.deck.append(Card(j, i))

        # automatically shuffles the new deck
        shuffle(self.deck)

    # removes card from the deck
    def dealCard(self):
        return self.deck.pop()

class Player:
    """
    Make a Player and the options to hit, pass, show hand.
    """
    def __init__(self, playerName):
        self.playerName = playerName
        self.playerHand = []

    # gets a card from the deck and adds to the player's hand
    def hit(self, card):
        self.playerHand.append(card)

    # displays the player's hand
    def showHand(self):
        print("{}'s hand: ".format(self.playerName), end = " ")
        print(self.playerHand)

    def score(self):
        result = 0
        for card in self.playerHand:
            result += card.int_value
        if result > 21:
            for i in self.playerHand:
                if i.int_value == 11:
                    i.int_value -= 10
                    break
            result = 0
            for card in self.playerHand:
                result += card.int_value
        return result

class Dealer:
    """
    Make a Dealer and the options to hit, pass, show hand
    """
    def __init__(self, dealerName):
        self.dealerName = dealerName
        self.dealerHand = []

    # gets a card from the deck and adds to the dealer's hand
    def hit(self, card):
        self.dealerHand.append(card)


    # displays the dealer's 'partial' hand hiding the first card in the list
    def partialHand(self):
        print("{}'s hand: [Hidden] &".format(self.dealerName), end = " ")
        print(self.dealerHand[1:])

    # displays the dealer's hand
    def showHand(self):
        print("{}'s hand: ".format(self.dealerName), end = " ")
        print(self.dealerHand[:])

    def score(self):
        result = 0
        for card in self.dealerHand:
            result += card.int_value
        if result == 21:
            # print("Dealer has Blackjack.")
            return result
        elif result > 21:
             for i in self.dealerHand:
                 if i.int_value == 11:
                     i.int_value -= 10
                     break
             result = 0
             for card in self.dealerHand:
                 result += card.int_value
        return result #- self.dealerHand[0].int_value

class BlackJack:
    def __init__(self, num_players):
        self.deck = Deck() # making a Deck instance
        self.deck.makeDeck() # making a Deck from the Deck instance
        self.dealer = Dealer("Batman") # making a Dealer instance
        self.playerList = [] # making a list of all players excl. Dealer
        self.makePlayers(num_players) # makes list based on the # of players
        self.startGame() # launches the game

    # asks for names of each player and populates a list of players
    def makePlayers(self, num_players):
        for i in range(num_players):
            playerName = input("Input Name: ")
            newPlayer = Player(playerName)
            self.playerList.append(newPlayer)
        #print(self.playerList)

    def tableResults(self):
        #print(self.dealer.showHand())
        # print("Sum total is {}".format(self.dealer.score()))
        print("-------------------------------------------------")
        print("TABLE STATUS")
        print("-------------------------------------------------")
        for eachPlayer in self.playerList:
            eachPlayer.showHand()
            print(">>> Sum total is {}\n".format(eachPlayer.score()))
        self.dealer.partialHand()
        print("-------------------------------------------------")

    def takeTurn(self, choice, each_player):
        while choice == "hit":
            if each_player.score() == 21:
                print("{} has Twenty one".format(each_player.playerName))
                choice = False
            elif each_player.score() > 21:
                print("{} has busted\n".format(each_player.playerName))
                choice = False
            else:
                choice = input("{}, Hit or Stay >>> ".format(each_player.playerName))
                if choice == "hit":
                    each_player.hit(self.deck.dealCard())
                    each_player.showHand()
                    print(">>> Sum total is {}\n".format(each_player.score()))
                else:
                    print("\n")
                    break
    
    def dealerTurn(self):
        while self.dealer.score() < 17:
            self.dealer.hit(self.deck.dealCard())
        self.dealer.showHand()
        print(">>> Sum total is {}".format(self.dealer.score()))
        if self.dealer.score() > 21:
            print("{} has busted".format(self.dealer.dealerName))

    def tableSummary(self):
        print("-------------------------------------------------")
        print("GAME SUMMARY")
        print("-------------------------------------------------")
        for each_player in self.playerList: # each player alone versus
            if each_player.score() <= 21 and self.dealer.score() <= 21:
                if each_player.score() == self.dealer.score():
                    each_playerOutput = "push!"
                    dealerOutput = "push!"
                if each_player.score() > self.dealer.score():
                    each_playerOutput = "wins!"
                    dealerOutput = "loses!"
                if each_player.score() < self.dealer.score():
                    each_playerOutput = "loses!"
                    dealerOutput = "wins!"
            elif self.dealer.score() > 21 and each_player.score() <= 21:
                each_playerOutput = "wins!"
                dealerOutput = "loses!"
            else:
                each_playerOutput = "loses!"
                dealerOutput = "wins!"

            # player result
            print("{}:".format(each_player.playerName))
            print(">>> Sum total is {}. Player {}".format(each_player.score(), each_playerOutput))

            # dealer result
            print("{}:".format(self.dealer.dealerName))
            print(">>> Sum total is {}. Dealer {}\n".format(self.dealer.score(), dealerOutput))

        print("-------------------------------------------------")





    # launches the game
    def startGame(self):
        for i in range(2): #Deals 2 cards for the first hand
            for each_player in self.playerList: #Deals to each player
                each_player.hit(self.deck.dealCard())
            self.dealer.hit(self.deck.dealCard())

        # run through each player turns

        for each_player in self.playerList:
            #Show Table Results
            self.tableResults()
            choice = "hit"
            self.takeTurn(choice, each_player)

        # automate the dealer's turn
        self.dealerTurn()

        self.tableSummary()



        # Dealer.showHand()
# """
            #dealer.hit()

#

#
#         for each_player in range(playerList):
#             each_player.showHand()
#         dealer.show()
# """


# TESTS
########################

# myDeck = Deck()
# myDeck.makeDeck()

# player1 = Player("Daniel")
# player1.hit(myDeck.dealCard())
# player1.hit(myDeck.dealCard())
#
# dealer = Dealer("Batman")
# dealer.hit(myDeck.dealCard())
# dealer.hit(myDeck.dealCard())
#
# print(len(myDeck.deck))
# player1.showHand()
# dealer.showHand()


newGame = BlackJack(2)
